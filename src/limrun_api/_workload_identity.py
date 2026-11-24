from __future__ import annotations

import os
import time
import inspect
import threading
from typing import Dict, Tuple, Union, TypeVar, Callable, Optional, Awaitable
from pathlib import Path

import anyio
import httpx
from anyio.to_thread import run_sync

WorkloadToken = Union[str, Callable[[], str]]
"""A workload JWT, or a callable that returns the current one for every exchange."""

AsyncWorkloadToken = Union[str, Callable[[], Union[str, Awaitable[str]]]]
"""A workload JWT, or a callable, sync or async, that returns the current one for every exchange."""


_Token = TypeVar("_Token")


def resolve_identity(
    token: Optional[_Token], token_file: Optional[str]
) -> Tuple[Union[_Token, str, None], Optional[str]]:
    """Explicit options before environment variables, and a token before a file."""
    if token:
        return token, None
    if token_file:
        return None, token_file
    env_token = os.environ.get("LIMRUN_WORKLOAD_IDENTITY_TOKEN")
    if env_token:
        return env_token, None
    return None, os.environ.get("LIMRUN_WORKLOAD_IDENTITY_TOKEN_FILE") or None


def _read_token_file(path: str) -> str:
    with Path(path).open(encoding="utf-8") as source:
        return source.read(32769)


def _identity_form(identity: object, binding: str) -> Dict[str, str]:
    token = identity.strip() if isinstance(identity, str) else ""
    if not token or len(token) > 32768:
        raise ValueError("Workload identity token must be a JWT of at most 32768 characters")
    return {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
        "subject_token": token,
        "audience": binding,
    }


def _session(response: httpx.Response, started: float) -> Tuple[str, float]:
    if response.status_code != 200:
        raise RuntimeError(f"Workload token exchange returned HTTP {response.status_code}")
    try:
        result = response.json()
        token = result["access_token"]
        ttl = result["expires_in"]
        if not isinstance(token, str) or not token or result["token_type"] != "Bearer":
            raise ValueError()
        if type(ttl) is not int or not 1 <= ttl <= 14400:
            raise ValueError()
    except (KeyError, ValueError, TypeError):
        raise RuntimeError("Invalid workload token exchange response") from None
    expires = started + ttl
    if expires <= time.monotonic():
        raise RuntimeError("Exchanged workload token has already expired")
    return token, expires - min(60, ttl / 5)


class WorkloadIdentity:
    def __init__(
        self, token_file: Optional[str], binding: str, endpoint: str, token: Optional[WorkloadToken] = None
    ) -> None:
        self.token = token
        self.token_file = token_file
        self.binding = binding
        self.endpoint = endpoint.rstrip("/") + "/v1/access_tokens"
        self.session = ""
        self.refresh_at = 0.0
        self.lock = threading.Lock()

    def _identity(self) -> str:
        if self.token is not None:
            return self.token() if callable(self.token) else self.token
        if not self.token_file:
            raise ValueError("Workload identity requires a token or token file")
        return _read_token_file(self.token_file)

    def get(self, client: httpx.Client) -> str:
        with self.lock:
            if time.monotonic() < self.refresh_at:
                return self.session
            form = _identity_form(self._identity(), self.binding)
            started = time.monotonic()
            response = client.post(self.endpoint, data=form, timeout=30, follow_redirects=False)
            self.session, self.refresh_at = _session(response, started)
            return self.session


class AsyncWorkloadIdentity:
    def __init__(
        self, token_file: Optional[str], binding: str, endpoint: str, token: Optional[AsyncWorkloadToken] = None
    ) -> None:
        self.token = token
        self.token_file = token_file
        self.binding = binding
        self.endpoint = endpoint.rstrip("/") + "/v1/access_tokens"
        self.session = ""
        self.refresh_at = 0.0
        self.lock = anyio.Lock()

    async def _identity(self) -> object:
        if self.token is not None:
            if not callable(self.token):
                return self.token
            result = self.token()
            return await result if inspect.isawaitable(result) else result
        if not self.token_file:
            raise ValueError("Workload identity requires a token or token file")
        return await run_sync(_read_token_file, self.token_file)

    async def get(self, client: httpx.AsyncClient) -> str:
        async with self.lock:
            if time.monotonic() < self.refresh_at:
                return self.session
            form = _identity_form(await self._identity(), self.binding)
            started = time.monotonic()
            response = await client.post(self.endpoint, data=form, timeout=30, follow_redirects=False)
            self.session, self.refresh_at = _session(response, started)
            return self.session
