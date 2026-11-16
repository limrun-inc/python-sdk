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
        assert form["audience"] == ["federation_builds"]
        assert "authorization" not in request.headers
        identities.append(form["subject_token"][0])
        return httpx.Response(200, json={"access_token": "lim_st_session", "token_type": "Bearer", "expires_in": 300})

    identity = WorkloadIdentity(str(path), "federation_builds", "https://sts.example.com")
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

    identity = AsyncWorkloadIdentity(str(path), "federation_builds", "https://sts.example.com")
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
    monkeypatch.setenv("LIMRUN_FEDERATION_BINDING_ID", "federation_builds")
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
            copied = client.with_options()
            await copied.android_instances.list()
            await copied.android_instances.list()
    else:
        with Limrun(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as sync_client:
            sync_copy = sync_client.with_options()
            sync_copy.android_instances.list()
            sync_copy.android_instances.list()
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
        federation_binding_id="federation_builds",
        sts_base_url="https://sts.example.com",
        http_client=httpx.Client(transport=httpx.MockTransport(handle)),
    ) as client:
        with pytest.raises(RuntimeError, match="[Ww]orkload token exchange") as error:
            client.android_instances.list()
        assert "external.jwt" not in str(error.value)
        assert "secret" not in str(error.value)
