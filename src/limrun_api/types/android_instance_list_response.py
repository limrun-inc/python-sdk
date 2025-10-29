# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .android_instance import AndroidInstance

__all__ = ["AndroidInstanceListResponse"]


class AndroidInstanceListResponse(BaseModel):
    items: Optional[List[AndroidInstance]] = None
