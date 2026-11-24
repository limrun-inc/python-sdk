from __future__ import annotations

import asyncio
from pathlib import Path
from urllib.parse import parse_qs
from concurrent.futures import ThreadPoolExecutor

import httpx
import pytest

from limrun_api import Limrun, AsyncLimrun
from limrun_api._workload_identity import WorkloadIdentity, AsyncWorkloadIdentity


def test_rotation_and_concurrent_exchange(tmp_path: Path) -> None:
    path = tmp_path / "identity.jwt"
    path.write_text("first.jwt\n")
    identities: list[str] = []

    def exchange(request: httpx.Request) -> httpx.Response:
        form = parse_qs(request.content.decode())
        assert form["audience"] == ["binding_builds"]
        assert "authorization" not in request.headers
        identities.append(form["subject_token"][0])
        return httpx.Response(200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300})

    identity = WorkloadIdentity(str(path), "binding_builds", "https://sts.example.com")
    with httpx.Client(transport=httpx.MockTransport(exchange)) as client:

        def get_session(_: int) -> str:
            return identity.get(client)

        with ThreadPoolExecutor(max_workers=8) as pool:
            assert list(pool.map(get_session, range(16))) == ["lim_st_session"] * 16
        assert identities == ["first.jwt"]
        path.write_text("rotated.jwt")
        identity.refresh_at = 0
        assert identity.get(client) == "lim_st_session"
        assert identities == ["first.jwt", "rotated.jwt"]


async def test_async_rotation_and_concurrent_exchange(tmp_path: Path) -> None:
    path = tmp_path / "identity.jwt"
    path.write_text("first.jwt")
    identities: list[str] = []

    def exchange(request: httpx.Request) -> httpx.Response:
        identities.append(parse_qs(request.content.decode())["subject_token"][0])
        return httpx.Response(200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300})

    identity = AsyncWorkloadIdentity(str(path), "binding_builds", "https://sts.example.com")
    async with httpx.AsyncClient(transport=httpx.MockTransport(exchange)) as client:
        assert await asyncio.gather(*(identity.get(client) for _ in range(16))) == ["lim_st_session"] * 16
        assert identities == ["first.jwt"]
        path.write_text("rotated.jwt")
        identity.refresh_at = 0
        await identity.get(client)
        assert identities == ["first.jwt", "rotated.jwt"]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_sdk_uses_session_and_copy_preserves_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, asynchronous: bool
) -> None:
    monkeypatch.delenv("LIM_API_KEY", raising=False)
    path = tmp_path / "identity.jwt"
    path.write_text("external.jwt")
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE", str(path))
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_BINDING_ID", "binding_builds")
    monkeypatch.setenv("LIMRUN_STS_BASE_URL", "https://sts.example.com")
    exchanges = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal exchanges
        if request.url.host == "sts.example.com":
            assert request.url.path == "/v1/access_tokens"
            assert parse_qs(request.content.decode())["subject_token"] == ["external.jwt"]
            exchanges += 1
            return httpx.Response(
                200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300}
            )
        assert request.headers["authorization"] == "Bearer lim_st_session"
        assert b"external.jwt" not in request.content
        return httpx.Response(200, json={"items": []})

    if asynchronous:
        async with AsyncLimrun(http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
            await client.android_instances.list()
            await client.with_options(timeout=5).android_instances.list()
            await client.with_options(timeout=10).android_instances.list()
            assert client.with_options(binding_id="binding_other")._workload_identity is not client._workload_identity
            assert (
                client.with_options(workload_token_file="other.jwt")._workload_identity is not client._workload_identity
            )
            assert (
                client.with_options(sts_base_url="https://other.example")._workload_identity
                is not client._workload_identity
            )
            assert client.with_options(api_key="key")._workload_identity is None
    else:
        with Limrun(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as sync_client:
            sync_client.android_instances.list()
            sync_client.with_options(timeout=5).android_instances.list()
            sync_client.with_options(timeout=10).android_instances.list()
            assert (
                sync_client.with_options(binding_id="binding_other")._workload_identity
                is not sync_client._workload_identity
            )
            assert (
                sync_client.with_options(workload_token_file="other.jwt")._workload_identity
                is not sync_client._workload_identity
            )
            assert (
                sync_client.with_options(sts_base_url="https://other.example")._workload_identity
                is not sync_client._workload_identity
            )
            assert sync_client.with_options(api_key="key")._workload_identity is None
    assert exchanges == 1


@pytest.mark.parametrize(
    "status,body",
    [
        (400, {}),
        (200, {"access_token": "secret"}),
        (200, {"access_token": "secret", "token_type": "Bearer", "expires_in": 0}),
        (302, {}),
    ],
)
def test_failed_exchange_never_calls_api(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, status: int, body: dict[str, object]
) -> None:
    monkeypatch.delenv("LIM_API_KEY", raising=False)
    path = tmp_path / "identity.jwt"
    path.write_text("external.jwt")

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.host == "sts.example.com"
        return httpx.Response(status, json=body)

    with Limrun(
        workload_token_file=str(path),
        binding_id="binding_builds",
        sts_base_url="https://sts.example.com",
        http_client=httpx.Client(transport=httpx.MockTransport(handle)),
    ) as client:
        with pytest.raises(RuntimeError, match="[Ww]orkload token exchange") as error:
            client.android_instances.list()
        assert "external.jwt" not in str(error.value)
        assert "secret" not in str(error.value)


@pytest.mark.parametrize("client_class", [Limrun, AsyncLimrun])
@pytest.mark.parametrize("missing", ["binding_id", "workload_token_file"])
def test_incomplete_identity_configuration(
    monkeypatch: pytest.MonkeyPatch, client_class: type[Limrun] | type[AsyncLimrun], missing: str
) -> None:
    for name in (
        "LIM_API_KEY",
        "LIMRUN_WORKLOAD_IDENTITY_BINDING_ID",
        "LIMRUN_WORKLOAD_IDENTITY_TOKEN",
        "LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE",
    ):
        monkeypatch.delenv(name, raising=False)
    message = "binding_id" if missing == "binding_id" else "workload_token, workload_token_file"
    with pytest.raises(ValueError, match=f"Federation requires {message}"):
        client_class(
            binding_id=None if missing == "binding_id" else "binding_builds",
            workload_token_file=None if missing == "workload_token_file" else "identity.jwt",
        )


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_api_key_bypasses_incomplete_identity_configuration(
    monkeypatch: pytest.MonkeyPatch, asynchronous: bool
) -> None:
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE", "missing.jwt")
    monkeypatch.delenv("LIMRUN_WORKLOAD_IDENTITY_BINDING_ID", raising=False)
    if asynchronous:
        async with AsyncLimrun(api_key="key") as client:
            assert client._workload_identity is None
    else:
        with Limrun(api_key="key") as sync_client:
            assert sync_client._workload_identity is None


def _subject_transport(subjects: list[str]) -> httpx.MockTransport:
    """Records exchanged subject tokens and answers API calls with an empty list."""

    def handle(request: httpx.Request) -> httpx.Response:
        if request.url.host == "sts.example.com":
            subjects.append(parse_qs(request.content.decode())["subject_token"][0])
            return httpx.Response(
                200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300}
            )
        assert request.headers["authorization"] == "Bearer lim_st_session"
        return httpx.Response(200, json={"items": []})

    return httpx.MockTransport(handle)


@pytest.fixture
def federation_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    for name in (
        "LIM_API_KEY",
        "LIMRUN_WORKLOAD_IDENTITY_TOKEN",
        "LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE",
        "LIMRUN_WORKLOAD_IDENTITY_TOKEN_INJECTED",
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_BINDING_ID", "binding_builds")
    monkeypatch.setenv("LIMRUN_STS_BASE_URL", "https://sts.example.com")
    path = tmp_path / "identity.jwt"
    path.write_text("from-file")
    return path


@pytest.mark.usefixtures("federation_env")
def test_sync_client_accepts_token_string_and_callable() -> None:
    subjects: list[str] = []
    with Limrun(
        workload_token=" from-string\n", http_client=httpx.Client(transport=_subject_transport(subjects))
    ) as client:
        client.android_instances.list()
    issued = iter(["jwt-1", "jwt-2"])
    with Limrun(
        workload_token=lambda: next(issued), http_client=httpx.Client(transport=_subject_transport(subjects))
    ) as client:
        client.android_instances.list()
        assert client._workload_identity is not None
        client._workload_identity.refresh_at = 0
        client.android_instances.list()
    assert subjects == ["from-string", "jwt-1", "jwt-2"]


@pytest.mark.usefixtures("federation_env")
async def test_async_client_accepts_sync_and_async_callables() -> None:
    subjects: list[str] = []

    async def fetch_token() -> str:
        return "async-jwt"

    for token in (fetch_token, lambda: "sync-jwt", "plain-jwt"):
        async with AsyncLimrun(
            workload_token=token, http_client=httpx.AsyncClient(transport=_subject_transport(subjects))
        ) as client:
            await client.android_instances.list()
    assert subjects == ["async-jwt", "sync-jwt", "plain-jwt"]


@pytest.mark.parametrize(
    "explicit,env_token,env_file,expected",
    [
        ({}, "env-jwt", False, "env-jwt"),
        ({}, "env-jwt", True, "env-jwt"),
        ({"workload_token": "explicit-jwt"}, "env-jwt", True, "explicit-jwt"),
        ({"workload_token_file": True}, "env-jwt", False, "from-file"),
        ({}, None, True, "from-file"),
    ],
)
def test_identity_source_precedence(
    federation_env: Path,
    monkeypatch: pytest.MonkeyPatch,
    explicit: dict[str, object],
    env_token: str | None,
    env_file: bool,
    expected: str,
) -> None:
    if env_token:
        monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN", env_token)
    if env_file:
        monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE", str(federation_env))
    options = {k: (str(federation_env) if k == "workload_token_file" else v) for k, v in explicit.items()}
    subjects: list[str] = []
    with Limrun(http_client=httpx.Client(transport=_subject_transport(subjects)), **options) as client:  # type: ignore[arg-type]
        client.android_instances.list()
    assert subjects == [expected]


def test_copy_with_a_new_file_drops_the_current_token(federation_env: Path) -> None:
    with Limrun(workload_token="from-string") as client:
        copied = client.with_options(workload_token_file=str(federation_env))
        assert copied.workload_token is None
        assert copied.workload_token_file == str(federation_env)
        assert client.with_options(timeout=5)._workload_identity is client._workload_identity


@pytest.mark.usefixtures("federation_env")
def test_blank_token_is_refused_before_the_exchange() -> None:
    def refuse(_: httpx.Request) -> httpx.Response:
        raise AssertionError("exchange must not run")

    with Limrun(workload_token=lambda: "  ", http_client=httpx.Client(transport=httpx.MockTransport(refuse))) as client:
        with pytest.raises(ValueError, match="Workload identity token must be a JWT"):
            client.android_instances.list()


def _injected_transport(forms: list[dict[str, list[str]]]) -> httpx.MockTransport:
    def handle(request: httpx.Request) -> httpx.Response:
        if request.url.host == "sts.example.com":
            assert "authorization" not in request.headers
            assert "x-limrun-subject-token" not in request.headers
            forms.append(parse_qs(request.content.decode()))
            return httpx.Response(
                200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300}
            )
        assert request.headers["authorization"] == "Bearer lim_st_session"
        return httpx.Response(200, json={"items": []})

    return httpx.MockTransport(handle)


@pytest.mark.parametrize("source", ["option", "environment"])
@pytest.mark.usefixtures("federation_env")
async def test_injected_token_sends_no_subject(monkeypatch: pytest.MonkeyPatch, source: str) -> None:
    if source == "environment":
        monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN_INJECTED", "true")
    injected = True if source == "option" else None
    forms: list[dict[str, list[str]]] = []
    with Limrun(
        workload_token_injected=injected, http_client=httpx.Client(transport=_injected_transport(forms))
    ) as client:
        client.android_instances.list()
    async with AsyncLimrun(
        workload_token_injected=injected, http_client=httpx.AsyncClient(transport=_injected_transport(forms))
    ) as async_client:
        await async_client.android_instances.list()
    assert len(forms) == 2
    for form in forms:
        assert "subject_token" not in form
        assert form["audience"] == ["binding_builds"]


@pytest.mark.parametrize("client_class", [Limrun, AsyncLimrun])
@pytest.mark.parametrize("source", [{"workload_token": "jwt"}, {"workload_token_file": "identity.jwt"}])
@pytest.mark.usefixtures("federation_env")
def test_injected_token_refuses_another_source(
    client_class: type[Limrun] | type[AsyncLimrun], source: dict[str, str]
) -> None:
    with pytest.raises(ValueError, match="workload_token_injected cannot be combined"):
        client_class(workload_token_injected=True, **source)  # type: ignore[arg-type]


@pytest.mark.usefixtures("federation_env")
def test_api_key_wins_over_conflicting_injected_configuration(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN_INJECTED", "true")
    monkeypatch.setenv("LIMRUN_WORKLOAD_IDENTITY_TOKEN", "jwt")
    with Limrun(api_key="key") as client:
        assert client._workload_identity is None


@pytest.mark.parametrize("client_class", [Limrun, AsyncLimrun])
@pytest.mark.usefixtures("federation_env")
def test_copy_switches_identity_sources(client_class: type[Limrun] | type[AsyncLimrun]) -> None:
    injected = client_class(workload_token_injected=True)
    to_token = injected.with_options(workload_token="jwt")
    assert (to_token.workload_token, to_token.workload_token_injected) == ("jwt", False)
    to_file = injected.with_options(workload_token_file="identity.jwt")
    assert (to_file.workload_token_file, to_file.workload_token_injected) == ("identity.jwt", False)

    token = client_class(workload_token="jwt")
    to_injected = token.with_options(workload_token_injected=True)
    assert (to_injected.workload_token, to_injected.workload_token_file) == (None, None)
    assert to_injected.workload_token_injected is True

    unchanged = injected.with_options(timeout=5)
    assert unchanged.workload_token_injected is True
    assert unchanged._workload_identity is injected._workload_identity
