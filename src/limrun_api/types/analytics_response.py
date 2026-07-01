# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .analytics_entry import AnalyticsEntry
from .analytics_summary import AnalyticsSummary

__all__ = ["AnalyticsResponse"]


class AnalyticsResponse(BaseModel):
    as_of: datetime = FieldInfo(alias="asOf")

    bucket: Literal["hour", "day", "week", "minute"]

    from_: datetime = FieldInfo(alias="from")

    series: List[AnalyticsEntry]

    summary: AnalyticsSummary
    """
    Summary of analytics across all time buckets, broken down by platform and region
    """

    timezone: str
    """IANA timezone used for time bucket grouping"""

    to: datetime
