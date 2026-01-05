# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Asset"]


class Asset(BaseModel):
    id: str

    name: str

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Human-readable display name for the asset. If not set, the name should be used."""

    md5: Optional[str] = None
    """Returned only if there is a corresponding file uploaded already."""

    os: Optional[Literal["ios", "android"]] = None
    """The operating system this asset is for.

    If not set, the asset is available for all platforms.
    """

    signed_download_url: Optional[str] = FieldInfo(alias="signedDownloadUrl", default=None)

    signed_upload_url: Optional[str] = FieldInfo(alias="signedUploadUrl", default=None)
