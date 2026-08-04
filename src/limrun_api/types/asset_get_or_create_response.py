# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AssetGetOrCreateResponse"]


class AssetGetOrCreateResponse(BaseModel):
    id: str

    kind: Literal["App", "Keychain"]

    name: str

    signed_download_url: str = FieldInfo(alias="signedDownloadUrl")

    signed_upload_url: str = FieldInfo(alias="signedUploadUrl")

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """When set, the time after which the asset is automatically deleted."""

    md5: Optional[str] = None
    """Returned only if there is a corresponding file uploaded already."""

    platform: Optional[Literal["ios", "android", "xcode"]] = None
