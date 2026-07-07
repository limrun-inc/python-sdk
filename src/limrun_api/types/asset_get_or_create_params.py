# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssetGetOrCreateParams"]


class AssetGetOrCreateParams(TypedDict, total=False):
    name: Required[str]

    kind: Literal["App", "Keychain"]

    platform: Literal["ios", "android", "xcode"]

    ttl: str
    """Optional time-to-live as a Go duration string (e.g.

    "24h"). When set, the asset is deleted this long after now; minimum is 1m. Omit
    for no expiry. On re-upload of an existing asset, a value updates the expiry
    while omitting it leaves the current expiry unchanged.
    """
