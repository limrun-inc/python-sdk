# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CostBreakdown"]


class CostBreakdown(BaseModel):
    """Cost breakdown by billing source in dollars"""

    credits_cost: float = FieldInfo(alias="creditsCost")
    """Cost from credits (always 0)"""

    on_demand_cost: float = FieldInfo(alias="onDemandCost")
    """Cost from on-demand billing in dollars"""

    plan_cost: Optional[Dict[str, float]] = FieldInfo(alias="planCost", default=None)
    """Map of plan ID to cost in dollars"""

    subscription_cost: Optional[Dict[str, float]] = FieldInfo(alias="subscriptionCost", default=None)
    """Map of subscription ID to cost in dollars"""
