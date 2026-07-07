# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Asset"]


class Asset(BaseModel):
    id: str

    kind: Literal["App", "Keychain"]

    name: str

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Human-readable display name for the asset. If not set, the name should be used."""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """When set, the time after which the asset is automatically deleted."""

    md5: Optional[str] = None
    """Returned only if there is a corresponding file uploaded already."""

    os: Optional[Literal["ios", "android", "xcode"]] = None
    """Deprecated: alias of platform, always mirrors it. Use platform instead."""

    platform: Optional[Literal["ios", "android", "xcode"]] = None
    """The platform this asset is for.

    If not set, the asset is available for all platforms.
    """

    signed_download_url: Optional[str] = FieldInfo(alias="signedDownloadUrl", default=None)

    signed_upload_url: Optional[str] = FieldInfo(alias="signedUploadUrl", default=None)
