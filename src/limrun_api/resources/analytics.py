# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import analytics_get_params, analytics_get_instances_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.analytics_response import AnalyticsResponse
from ..types.analytics_instances_response import AnalyticsInstancesResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/limrun-inc/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/limrun-inc/python-sdk#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        bucket: Literal["hour", "day", "week", "minute"] | Omit = omit,
        labels: str | Omit = omit,
        region: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsResponse:
        """
        Get analytics for the authenticated organization

        Args:
          from_: Start of the time range (inclusive, RFC3339)

          to: End of the time range (exclusive, RFC3339)

          bucket: Time bucket granularity for the analytics series

          labels: Label selector to filter instances (e.g., "env=prod,team=backend")

          region: Optional region filter

          timezone: Optional IANA timezone used for time bucket grouping. Defaults to
              America/Los_Angeles when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "bucket": bucket,
                        "labels": labels,
                        "region": region,
                        "timezone": timezone,
                    },
                    analytics_get_params.AnalyticsGetParams,
                ),
            ),
            cast_to=AnalyticsResponse,
        )

    def get_instances(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        labels: str | Omit = omit,
        region: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsInstancesResponse:
        """
        Returns per-instance analytics grouped by minute bucket for detailed chart
        views.

        Args:
          from_: Start of the time range (inclusive, RFC3339)

          to: End of the time range (exclusive, RFC3339)

          labels: Label selector to filter instances (e.g., "env=prod,team=backend")

          region: Optional region filter

          timezone: Optional IANA timezone used for minute bucket grouping. Defaults to
              America/Los_Angeles when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "labels": labels,
                        "region": region,
                        "timezone": timezone,
                    },
                    analytics_get_instances_params.AnalyticsGetInstancesParams,
                ),
            ),
            cast_to=AnalyticsInstancesResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/limrun-inc/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/limrun-inc/python-sdk#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        bucket: Literal["hour", "day", "week", "minute"] | Omit = omit,
        labels: str | Omit = omit,
        region: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsResponse:
        """
        Get analytics for the authenticated organization

        Args:
          from_: Start of the time range (inclusive, RFC3339)

          to: End of the time range (exclusive, RFC3339)

          bucket: Time bucket granularity for the analytics series

          labels: Label selector to filter instances (e.g., "env=prod,team=backend")

          region: Optional region filter

          timezone: Optional IANA timezone used for time bucket grouping. Defaults to
              America/Los_Angeles when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "bucket": bucket,
                        "labels": labels,
                        "region": region,
                        "timezone": timezone,
                    },
                    analytics_get_params.AnalyticsGetParams,
                ),
            ),
            cast_to=AnalyticsResponse,
        )

    async def get_instances(
        self,
        *,
        from_: Union[str, datetime],
        to: Union[str, datetime],
        labels: str | Omit = omit,
        region: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsInstancesResponse:
        """
        Returns per-instance analytics grouped by minute bucket for detailed chart
        views.

        Args:
          from_: Start of the time range (inclusive, RFC3339)

          to: End of the time range (exclusive, RFC3339)

          labels: Label selector to filter instances (e.g., "env=prod,team=backend")

          region: Optional region filter

          timezone: Optional IANA timezone used for minute bucket grouping. Defaults to
              America/Los_Angeles when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "labels": labels,
                        "region": region,
                        "timezone": timezone,
                    },
                    analytics_get_instances_params.AnalyticsGetInstancesParams,
                ),
            ),
            cast_to=AnalyticsInstancesResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get = to_raw_response_wrapper(
            analytics.get,
        )
        self.get_instances = to_raw_response_wrapper(
            analytics.get_instances,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get = async_to_raw_response_wrapper(
            analytics.get,
        )
        self.get_instances = async_to_raw_response_wrapper(
            analytics.get_instances,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get = to_streamed_response_wrapper(
            analytics.get,
        )
        self.get_instances = to_streamed_response_wrapper(
            analytics.get_instances,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get = async_to_streamed_response_wrapper(
            analytics.get,
        )
        self.get_instances = async_to_streamed_response_wrapper(
            analytics.get_instances,
        )
