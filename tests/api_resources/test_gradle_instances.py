# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from limrun_api import Limrun, AsyncLimrun
from tests.utils import assert_matches_type
from limrun_api.types import GradleInstance
from limrun_api.pagination import SyncItems, AsyncItems

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGradleInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.create()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.create(
            reuse_if_exists=True,
            wait=True,
            metadata={
                "display_name": "displayName",
                "labels": {"foo": "string"},
            },
            spec={
                "clues": [
                    {
                        "kind": "ClientIP",
                        "client_ip": "clientIp",
                    }
                ],
                "hard_timeout": "hardTimeout",
                "inactivity_timeout": "inactivityTimeout",
                "jurisdiction": "us",
                "region": "region",
            },
        )
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Limrun) -> None:
        response = client.gradle_instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = response.parse()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Limrun) -> None:
        with client.gradle_instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = response.parse()
            assert_matches_type(GradleInstance, gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.list()
        assert_matches_type(SyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.list(
            ending_before="endingBefore",
            label_selector="env=prod,version=1.2",
            limit=50,
            starting_after="startingAfter",
            state="assigned,ready",
        )
        assert_matches_type(SyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Limrun) -> None:
        response = client.gradle_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = response.parse()
        assert_matches_type(SyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Limrun) -> None:
        with client.gradle_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = response.parse()
            assert_matches_type(SyncItems[GradleInstance], gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.delete(
            "id",
        )
        assert gradle_instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Limrun) -> None:
        response = client.gradle_instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = response.parse()
        assert gradle_instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Limrun) -> None:
        with client.gradle_instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = response.parse()
            assert gradle_instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Limrun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gradle_instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Limrun) -> None:
        gradle_instance = client.gradle_instances.get(
            "id",
        )
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Limrun) -> None:
        response = client.gradle_instances.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = response.parse()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Limrun) -> None:
        with client.gradle_instances.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = response.parse()
            assert_matches_type(GradleInstance, gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Limrun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gradle_instances.with_raw_response.get(
                "",
            )


class TestAsyncGradleInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.create()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.create(
            reuse_if_exists=True,
            wait=True,
            metadata={
                "display_name": "displayName",
                "labels": {"foo": "string"},
            },
            spec={
                "clues": [
                    {
                        "kind": "ClientIP",
                        "client_ip": "clientIp",
                    }
                ],
                "hard_timeout": "hardTimeout",
                "inactivity_timeout": "inactivityTimeout",
                "jurisdiction": "us",
                "region": "region",
            },
        )
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLimrun) -> None:
        response = await async_client.gradle_instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = await response.parse()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLimrun) -> None:
        async with async_client.gradle_instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = await response.parse()
            assert_matches_type(GradleInstance, gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.list()
        assert_matches_type(AsyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.list(
            ending_before="endingBefore",
            label_selector="env=prod,version=1.2",
            limit=50,
            starting_after="startingAfter",
            state="assigned,ready",
        )
        assert_matches_type(AsyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLimrun) -> None:
        response = await async_client.gradle_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = await response.parse()
        assert_matches_type(AsyncItems[GradleInstance], gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLimrun) -> None:
        async with async_client.gradle_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = await response.parse()
            assert_matches_type(AsyncItems[GradleInstance], gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.delete(
            "id",
        )
        assert gradle_instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLimrun) -> None:
        response = await async_client.gradle_instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = await response.parse()
        assert gradle_instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLimrun) -> None:
        async with async_client.gradle_instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = await response.parse()
            assert gradle_instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLimrun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gradle_instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLimrun) -> None:
        gradle_instance = await async_client.gradle_instances.get(
            "id",
        )
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLimrun) -> None:
        response = await async_client.gradle_instances.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gradle_instance = await response.parse()
        assert_matches_type(GradleInstance, gradle_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLimrun) -> None:
        async with async_client.gradle_instances.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gradle_instance = await response.parse()
            assert_matches_type(GradleInstance, gradle_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLimrun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gradle_instances.with_raw_response.get(
                "",
            )
