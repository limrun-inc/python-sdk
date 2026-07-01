# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AnalyticsResponse",
    "Series",
    "SeriesAndroid",
    "SeriesIos",
    "SeriesXcode",
    "SeriesInstance",
    "SeriesInstanceBilledBreakdown",
    "SeriesInstanceCostBreakdown",
    "Summary",
    "SummaryAndroid",
    "SummaryIos",
    "SummaryXcode",
]


class SeriesAndroid(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class SeriesIos(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class SeriesXcode(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


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

    platform: Literal["android", "ios", "xcode"]
    """Platform name."""

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
    """Analytics data for a single time bucket, broken down by platform and region"""

    android: Dict[str, SeriesAndroid]
    """Map of region to analytics stats for Android"""

    ios: Dict[str, SeriesIos]
    """Map of region to analytics stats for iOS"""

    timestamp: str
    """
    RFC3339 timestamp for the start of the bucket in the requested timezone,
    including the local offset
    """

    xcode: Dict[str, SeriesXcode]
    """Map of region to analytics stats for Xcode"""

    instances: Optional[List[SeriesInstance]] = None
    """Individual instance details for this time bucket"""


class SummaryAndroid(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class SummaryIos(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class SummaryXcode(BaseModel):
    """Complete analytics for a specific region including billing breakdown"""

    avg_duration_minutes: float = FieldInfo(alias="avgDurationMinutes")
    """Average instance duration in minutes"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars"""

    count: int
    """Number of unique instances"""

    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")
    """Minutes billed to credits"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")
    """Minutes billed on-demand"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""


class Summary(BaseModel):
    """
    Summary of analytics across all time buckets, broken down by platform and region
    """

    android: Dict[str, SummaryAndroid]
    """Map of region to analytics stats for Android"""

    ios: Dict[str, SummaryIos]
    """Map of region to analytics stats for iOS"""

    xcode: Dict[str, SummaryXcode]
    """Map of region to analytics stats for Xcode"""


class AnalyticsResponse(BaseModel):
    as_of: datetime = FieldInfo(alias="asOf")

    bucket: Literal["hour", "day", "week", "minute"]

    from_: datetime = FieldInfo(alias="from")

    series: List[Series]

    summary: Summary
    """
    Summary of analytics across all time buckets, broken down by platform and region
    """

    timezone: str
    """IANA timezone used for time bucket grouping"""

    to: datetime
