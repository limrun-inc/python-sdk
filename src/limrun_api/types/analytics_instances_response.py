# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .analytics_instance_entry import AnalyticsInstanceEntry

__all__ = ["AnalyticsInstancesResponse"]


class AnalyticsInstancesResponse(BaseModel):
    as_of: datetime = FieldInfo(alias="asOf")

    from_: datetime = FieldInfo(alias="from")

    series: List[AnalyticsInstanceEntry]

    timezone: str
    """IANA timezone used for time bucket grouping"""

    to: datetime
