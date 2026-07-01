# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from limrun_api import Limrun, AsyncLimrun
from tests.utils import assert_matches_type
from limrun_api.types import (
    AnalyticsResponse,
    AnalyticsInstancesResponse,
)
from limrun_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Limrun) -> None:
        analytics = client.analytics.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Limrun) -> None:
        analytics = client.analytics.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            bucket="hour",
            labels="labels",
            region="region",
            timezone="timezone",
        )
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Limrun) -> None:
        response = client.analytics.with_raw_response.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Limrun) -> None:
        with client.analytics.with_streaming_response.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instances(self, client: Limrun) -> None:
        analytics = client.analytics.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instances_with_all_params(self, client: Limrun) -> None:
        analytics = client.analytics.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            labels="labels",
            region="region",
            timezone="timezone",
        )
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instances(self, client: Limrun) -> None:
        response = client.analytics.with_raw_response.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instances(self, client: Limrun) -> None:
        with client.analytics.with_streaming_response.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLimrun) -> None:
        analytics = await async_client.analytics.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLimrun) -> None:
        analytics = await async_client.analytics.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            bucket="hour",
            labels="labels",
            region="region",
            timezone="timezone",
        )
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLimrun) -> None:
        response = await async_client.analytics.with_raw_response.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLimrun) -> None:
        async with async_client.analytics.with_streaming_response.get(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instances(self, async_client: AsyncLimrun) -> None:
        analytics = await async_client.analytics.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instances_with_all_params(self, async_client: AsyncLimrun) -> None:
        analytics = await async_client.analytics.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            labels="labels",
            region="region",
            timezone="timezone",
        )
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instances(self, async_client: AsyncLimrun) -> None:
        response = await async_client.analytics.with_raw_response.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instances(self, async_client: AsyncLimrun) -> None:
        async with async_client.analytics.with_streaming_response.get_instances(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsInstancesResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True
