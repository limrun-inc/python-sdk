# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from limrun_api import Limrun, AsyncLimrun
from tests.utils import assert_matches_type
from limrun_api.types import ScopedToken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScopedTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Limrun) -> None:
        scoped_token = client.scoped_tokens.create(
            scopes=["string"],
        )
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Limrun) -> None:
        scoped_token = client.scoped_tokens.create(
            scopes=["string"],
            ttl_seconds=1,
        )
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Limrun) -> None:
        response = client.scoped_tokens.with_raw_response.create(
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoped_token = response.parse()
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Limrun) -> None:
        with client.scoped_tokens.with_streaming_response.create(
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoped_token = response.parse()
            assert_matches_type(ScopedToken, scoped_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScopedTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLimrun) -> None:
        scoped_token = await async_client.scoped_tokens.create(
            scopes=["string"],
        )
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLimrun) -> None:
        scoped_token = await async_client.scoped_tokens.create(
            scopes=["string"],
            ttl_seconds=1,
        )
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLimrun) -> None:
        response = await async_client.scoped_tokens.with_raw_response.create(
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoped_token = await response.parse()
        assert_matches_type(ScopedToken, scoped_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLimrun) -> None:
        async with async_client.scoped_tokens.with_streaming_response.create(
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoped_token = await response.parse()
            assert_matches_type(ScopedToken, scoped_token, path=["response"])

        assert cast(Any, response.is_closed) is True
