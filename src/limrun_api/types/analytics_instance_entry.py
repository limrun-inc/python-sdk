# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .analytics_instance import AnalyticsInstance

__all__ = ["AnalyticsInstanceEntry"]


class AnalyticsInstanceEntry(BaseModel):
    instances: List[AnalyticsInstance]

    timestamp: str
    """
    RFC3339 timestamp for the start of the minute bucket in the requested timezone,
    including the local offset
    """
