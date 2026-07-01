# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AnalyticsRegionStats"]


class AnalyticsRegionStats(BaseModel):
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
