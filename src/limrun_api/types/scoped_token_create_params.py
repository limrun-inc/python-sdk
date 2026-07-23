# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ScopedTokenCreateParams"]


class ScopedTokenCreateParams(TypedDict, total=False):
    scopes: Required[SequenceNotStr[str]]
    """
    Scopes in the form <resource>:<id|_>:<action>, e.g. "device:_:install",
    "asset:asset_01h455vb4pex5vsknk084sn02q:read" or "applerelay:\\**:connect".
    Resource IDs are the customer-visible IDs returned by the API.
    """

    ttl_seconds: Annotated[int, PropertyInfo(alias="ttlSeconds")]
    """How long the token stays valid.

    Defaults to 3600 (1 hour), maximum is 14400 (4 hours).
    """
