# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    include_app_store: Annotated[bool, PropertyInfo(alias="includeAppStore")]
    """
    If true, also includes assets from Limrun App Store where you have access to.
    App Store assets will be returned with a "appstore/" prefix in their names.
    """

    include_download_url: Annotated[bool, PropertyInfo(alias="includeDownloadUrl")]
    """Toggles whether a download URL should be included in the response"""

    include_upload_url: Annotated[bool, PropertyInfo(alias="includeUploadUrl")]
    """Toggles whether an upload URL should be included in the response"""

    limit: int
    """Maximum number of items to be returned. The default is 50."""

    name_filter: Annotated[str, PropertyInfo(alias="nameFilter")]
    """
    Case-sensitive exact match on the asset name. Cannot be combined with
    namePrefixFilter. When combined with includeAppStore=true, a leading "appstore/"
    is stripped before querying App Store assets (whose stored names never carry the
    prefix).
    """

    name_prefix_filter: Annotated[str, PropertyInfo(alias="namePrefixFilter")]
    """
    Case-sensitive prefix match on the asset name. LIKE wildcards ("%", "\\__") in the
    value are treated as literal characters, not wildcards. Empty string is rejected
    with 400; omit the parameter if no filtering is desired. Cannot be combined with
    nameFilter. When combined with includeAppStore=true, a leading "appstore/" is
    stripped before querying App Store assets (whose stored names never carry the
    prefix); a partial prefix like "appstor" will not match any App Store assets.
    """
