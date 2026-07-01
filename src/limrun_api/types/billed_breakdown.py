# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BilledBreakdown"]


class BilledBreakdown(BaseModel):
    credits_billed_minutes: int = FieldInfo(alias="creditsBilledMinutes")

    on_demand_billed_minutes: int = FieldInfo(alias="onDemandBilledMinutes")

    plan_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="planBilledMinutes", default=None)
    """Map of plan ID to billed minutes"""

    subscription_billed_minutes: Optional[Dict[str, int]] = FieldInfo(alias="subscriptionBilledMinutes", default=None)
    """Map of subscription ID to billed minutes"""
