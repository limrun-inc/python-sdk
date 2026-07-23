# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import scoped_token_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.scoped_token import ScopedToken

__all__ = ["ScopedTokensResource", "AsyncScopedTokensResource"]


class ScopedTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScopedTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/limrun-inc/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScopedTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScopedTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/limrun-inc/python-sdk#with_streaming_response
        """
        return ScopedTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        scopes: SequenceNotStr[str],
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScopedToken:
        """
        Mint a short-lived scoped token whose scopes limit what the holder can do, e.g.
        install a specific asset on a device through the registry. The token is verified
        offline by services holding the token signing public key and cannot be revoked,
        so keep TTLs short. It is bound to the authenticated caller's organization.

        Args:
          scopes: Scopes in the form <resource>:<id|_>:<action>, e.g. "device:_:install",
              "asset:asset_01h455vb4pex5vsknk084sn02q:read" or "applerelay:\\**:connect".
              Resource IDs are the customer-visible IDs returned by the API.

          ttl_seconds: How long the token stays valid. Defaults to 3600 (1 hour), maximum is 14400 (4
              hours).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/scoped_tokens",
            body=maybe_transform(
                {
                    "scopes": scopes,
                    "ttl_seconds": ttl_seconds,
                },
                scoped_token_create_params.ScopedTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScopedToken,
        )


class AsyncScopedTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScopedTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/limrun-inc/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScopedTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScopedTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/limrun-inc/python-sdk#with_streaming_response
        """
        return AsyncScopedTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        scopes: SequenceNotStr[str],
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScopedToken:
        """
        Mint a short-lived scoped token whose scopes limit what the holder can do, e.g.
        install a specific asset on a device through the registry. The token is verified
        offline by services holding the token signing public key and cannot be revoked,
        so keep TTLs short. It is bound to the authenticated caller's organization.

        Args:
          scopes: Scopes in the form <resource>:<id|_>:<action>, e.g. "device:_:install",
              "asset:asset_01h455vb4pex5vsknk084sn02q:read" or "applerelay:\\**:connect".
              Resource IDs are the customer-visible IDs returned by the API.

          ttl_seconds: How long the token stays valid. Defaults to 3600 (1 hour), maximum is 14400 (4
              hours).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/scoped_tokens",
            body=await async_maybe_transform(
                {
                    "scopes": scopes,
                    "ttl_seconds": ttl_seconds,
                },
                scoped_token_create_params.ScopedTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScopedToken,
        )


class ScopedTokensResourceWithRawResponse:
    def __init__(self, scoped_tokens: ScopedTokensResource) -> None:
        self._scoped_tokens = scoped_tokens

        self.create = to_raw_response_wrapper(
            scoped_tokens.create,
        )


class AsyncScopedTokensResourceWithRawResponse:
    def __init__(self, scoped_tokens: AsyncScopedTokensResource) -> None:
        self._scoped_tokens = scoped_tokens

        self.create = async_to_raw_response_wrapper(
            scoped_tokens.create,
        )


class ScopedTokensResourceWithStreamingResponse:
    def __init__(self, scoped_tokens: ScopedTokensResource) -> None:
        self._scoped_tokens = scoped_tokens

        self.create = to_streamed_response_wrapper(
            scoped_tokens.create,
        )


class AsyncScopedTokensResourceWithStreamingResponse:
    def __init__(self, scoped_tokens: AsyncScopedTokensResource) -> None:
        self._scoped_tokens = scoped_tokens

        self.create = async_to_streamed_response_wrapper(
            scoped_tokens.create,
        )
