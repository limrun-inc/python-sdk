# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .asset import Asset
from .._models import BaseModel

__all__ = ["AssetListResponse"]


class AssetListResponse(BaseModel):
    items: Optional[List[Asset]] = None
