# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AnalyticsInstancesResponse",
    "Series",
    "SeriesInstance",
    "SeriesInstanceBilledBreakdown",
    "SeriesInstanceCostBreakdown",
]


class SeriesInstanceBilledBreakdown(BaseModel):
    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")

    plan_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="planBilledMinutes", default=None)
    """Map of plan ID to billed minutes"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""


class SeriesInstanceCostBreakdown(BaseModel):
    """Cost breakdown by billing source in dollars"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    plan_cost: Optional[Dict[str, float]] = FieldInfo(alias="planCost", default=None)
    """Map of plan ID to cost in dollars"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class SeriesInstance(BaseModel):
    """Analytics details for a single instance within a time bucket"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars for this instance"""

    instance_tid: str = FieldInfo(alias="instanceTid")
    """Instance type ID (e.g., ios_xxx, android_xxx)"""

    platform: str
    """Platform name, such as android, ios, or xcode"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    billed_breakdown: Optional[SeriesInstanceBilledBreakdown] = FieldInfo(alias="billedBreakdown", default=None)

    cost_breakdown: Optional[SeriesInstanceCostBreakdown] = FieldInfo(alias="costBreakdown", default=None)
    """Cost breakdown by billing source in dollars"""

    labels: Optional[Dict[str, str]] = None
    """Instance labels at billing time"""

    region: Optional[str] = None
    """Region where the instance ran"""


class Series(BaseModel):
    instances: List[SeriesInstance]

    timestamp: str
    """
    RFC3339 timestamp for the start of the minute bucket in the requested timezone,
    including the local offset
    """


class AnalyticsInstancesResponse(BaseModel):
    as_of: datetime = FieldInfo(alias="asOf")

    from_: datetime = FieldInfo(alias="from")

    series: List[Series]

    timezone: str
    """IANA timezone used for time bucket grouping"""

    to: datetime
