from __future__ import annotations

import time
import threading
from typing import Dict, Tuple
from pathlib import Path

import anyio
import httpx
from anyio.to_thread import run_sync


def _identity_form(path: str, binding: str) -> Dict[str, str]:
    with Path(path).open(encoding="utf-8") as source:
        token = source.read(32769).strip()
    if not token or len(token) > 32768:
        raise ValueError("Workload identity file must contain a JWT of at most 32768 characters")
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
    def __init__(self, token_file: str, binding: str, endpoint: str) -> None:
        self.token_file = token_file
        self.binding = binding
        self.endpoint = endpoint.rstrip("/") + "/v1/token"
        self.token = ""
        self.refresh_at = 0.0
        self.lock = threading.Lock()

    def get(self, client: httpx.Client) -> str:
        with self.lock:
            if time.monotonic() < self.refresh_at:
                return self.token
            form = _identity_form(self.token_file, self.binding)
            started = time.monotonic()
            response = client.post(self.endpoint, data=form, timeout=30, follow_redirects=False)
            self.token, self.refresh_at = _session(response, started)
            return self.token


class AsyncWorkloadIdentity:
    def __init__(self, token_file: str, binding: str, endpoint: str) -> None:
        self.token_file = token_file
        self.binding = binding
        self.endpoint = endpoint.rstrip("/") + "/v1/token"
        self.token = ""
        self.refresh_at = 0.0
        self.lock = anyio.Lock()

    async def get(self, client: httpx.AsyncClient) -> str:
        async with self.lock:
            if time.monotonic() < self.refresh_at:
                return self.token
            form = await run_sync(_identity_form, self.token_file, self.binding)
            started = time.monotonic()
            response = await client.post(self.endpoint, data=form, timeout=30, follow_redirects=False)
            self.token, self.refresh_at = _session(response, started)
            return self.token
