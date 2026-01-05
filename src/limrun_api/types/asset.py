# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

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

    signed_download_url: Optional[str] = FieldInfo(alias="signedDownloadUrl", default=None)

    signed_upload_url: Optional[str] = FieldInfo(alias="signedUploadUrl", default=None)
