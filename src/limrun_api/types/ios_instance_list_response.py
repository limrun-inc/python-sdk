# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ios_instance import IosInstance

__all__ = ["IosInstanceListResponse"]


class IosInstanceListResponse(BaseModel):
    items: Optional[List[IosInstance]] = None
