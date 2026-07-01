# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import assets, analytics, ios_instances, xcode_instances, android_instances
    from .resources.assets import AssetsResource, AsyncAssetsResource
    from .resources.analytics import AnalyticsResource, AsyncAnalyticsResource
    from .resources.ios_instances import IosInstancesResource, AsyncIosInstancesResource
    from .resources.xcode_instances import XcodeInstancesResource, AsyncXcodeInstancesResource
    from .resources.android_instances import AndroidInstancesResource, AsyncAndroidInstancesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Limrun", "AsyncLimrun", "Client", "AsyncClient"]


class Limrun(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Limrun client instance.

        This automatically infers the `api_key` argument from the `LIM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LIM_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LIMRUN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.limrun.com"

        custom_headers_env = os.environ.get("LIMRUN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def android_instances(self) -> AndroidInstancesResource:
        from .resources.android_instances import AndroidInstancesResource

        return AndroidInstancesResource(self)

    @cached_property
    def assets(self) -> AssetsResource:
        from .resources.assets import AssetsResource

        return AssetsResource(self)

    @cached_property
    def ios_instances(self) -> IosInstancesResource:
        from .resources.ios_instances import IosInstancesResource

        return IosInstancesResource(self)

    @cached_property
    def xcode_instances(self) -> XcodeInstancesResource:
        from .resources.xcode_instances import XcodeInstancesResource

        return XcodeInstancesResource(self)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def with_raw_response(self) -> LimrunWithRawResponse:
        return LimrunWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimrunWithStreamedResponse:
        return LimrunWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLimrun(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLimrun client instance.

        This automatically infers the `api_key` argument from the `LIM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LIM_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LIMRUN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.limrun.com"

        custom_headers_env = os.environ.get("LIMRUN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def android_instances(self) -> AsyncAndroidInstancesResource:
        from .resources.android_instances import AsyncAndroidInstancesResource

        return AsyncAndroidInstancesResource(self)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        from .resources.assets import AsyncAssetsResource

        return AsyncAssetsResource(self)

    @cached_property
    def ios_instances(self) -> AsyncIosInstancesResource:
        from .resources.ios_instances import AsyncIosInstancesResource

        return AsyncIosInstancesResource(self)

    @cached_property
    def xcode_instances(self) -> AsyncXcodeInstancesResource:
        from .resources.xcode_instances import AsyncXcodeInstancesResource

        return AsyncXcodeInstancesResource(self)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLimrunWithRawResponse:
        return AsyncLimrunWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimrunWithStreamedResponse:
        return AsyncLimrunWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LimrunWithRawResponse:
    _client: Limrun

    def __init__(self, client: Limrun) -> None:
        self._client = client

    @cached_property
    def android_instances(self) -> android_instances.AndroidInstancesResourceWithRawResponse:
        from .resources.android_instances import AndroidInstancesResourceWithRawResponse

        return AndroidInstancesResourceWithRawResponse(self._client.android_instances)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithRawResponse:
        from .resources.assets import AssetsResourceWithRawResponse

        return AssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def ios_instances(self) -> ios_instances.IosInstancesResourceWithRawResponse:
        from .resources.ios_instances import IosInstancesResourceWithRawResponse

        return IosInstancesResourceWithRawResponse(self._client.ios_instances)

    @cached_property
    def xcode_instances(self) -> xcode_instances.XcodeInstancesResourceWithRawResponse:
        from .resources.xcode_instances import XcodeInstancesResourceWithRawResponse

        return XcodeInstancesResourceWithRawResponse(self._client.xcode_instances)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)


class AsyncLimrunWithRawResponse:
    _client: AsyncLimrun

    def __init__(self, client: AsyncLimrun) -> None:
        self._client = client

    @cached_property
    def android_instances(self) -> android_instances.AsyncAndroidInstancesResourceWithRawResponse:
        from .resources.android_instances import AsyncAndroidInstancesResourceWithRawResponse

        return AsyncAndroidInstancesResourceWithRawResponse(self._client.android_instances)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithRawResponse:
        from .resources.assets import AsyncAssetsResourceWithRawResponse

        return AsyncAssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def ios_instances(self) -> ios_instances.AsyncIosInstancesResourceWithRawResponse:
        from .resources.ios_instances import AsyncIosInstancesResourceWithRawResponse

        return AsyncIosInstancesResourceWithRawResponse(self._client.ios_instances)

    @cached_property
    def xcode_instances(self) -> xcode_instances.AsyncXcodeInstancesResourceWithRawResponse:
        from .resources.xcode_instances import AsyncXcodeInstancesResourceWithRawResponse

        return AsyncXcodeInstancesResourceWithRawResponse(self._client.xcode_instances)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)


class LimrunWithStreamedResponse:
    _client: Limrun

    def __init__(self, client: Limrun) -> None:
        self._client = client

    @cached_property
    def android_instances(self) -> android_instances.AndroidInstancesResourceWithStreamingResponse:
        from .resources.android_instances import AndroidInstancesResourceWithStreamingResponse

        return AndroidInstancesResourceWithStreamingResponse(self._client.android_instances)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithStreamingResponse:
        from .resources.assets import AssetsResourceWithStreamingResponse

        return AssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def ios_instances(self) -> ios_instances.IosInstancesResourceWithStreamingResponse:
        from .resources.ios_instances import IosInstancesResourceWithStreamingResponse

        return IosInstancesResourceWithStreamingResponse(self._client.ios_instances)

    @cached_property
    def xcode_instances(self) -> xcode_instances.XcodeInstancesResourceWithStreamingResponse:
        from .resources.xcode_instances import XcodeInstancesResourceWithStreamingResponse

        return XcodeInstancesResourceWithStreamingResponse(self._client.xcode_instances)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)


class AsyncLimrunWithStreamedResponse:
    _client: AsyncLimrun

    def __init__(self, client: AsyncLimrun) -> None:
        self._client = client

    @cached_property
    def android_instances(self) -> android_instances.AsyncAndroidInstancesResourceWithStreamingResponse:
        from .resources.android_instances import AsyncAndroidInstancesResourceWithStreamingResponse

        return AsyncAndroidInstancesResourceWithStreamingResponse(self._client.android_instances)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithStreamingResponse:
        from .resources.assets import AsyncAssetsResourceWithStreamingResponse

        return AsyncAssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def ios_instances(self) -> ios_instances.AsyncIosInstancesResourceWithStreamingResponse:
        from .resources.ios_instances import AsyncIosInstancesResourceWithStreamingResponse

        return AsyncIosInstancesResourceWithStreamingResponse(self._client.ios_instances)

    @cached_property
    def xcode_instances(self) -> xcode_instances.AsyncXcodeInstancesResourceWithStreamingResponse:
        from .resources.xcode_instances import AsyncXcodeInstancesResourceWithStreamingResponse

        return AsyncXcodeInstancesResourceWithStreamingResponse(self._client.xcode_instances)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)


Client = Limrun

AsyncClient = AsyncLimrun
