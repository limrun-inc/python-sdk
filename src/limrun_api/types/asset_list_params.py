# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Return items up until this ID.

    If not given, it will return up until the 50th item.
    """

    include_download_url: Annotated[bool, PropertyInfo(alias="includeDownloadUrl")]
    """Toggles whether a download URL should be included in the response"""

    include_upload_url: Annotated[bool, PropertyInfo(alias="includeUploadUrl")]
    """Toggles whether an upload URL should be included in the response"""

    limit: int
    """Maximum number of items to be returned. The default is 50."""

    name_filter: Annotated[str, PropertyInfo(alias="nameFilter")]
    """Query by file name"""

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Return items starting after this ID.

    If not given, it will start from the most recent one.
    """
