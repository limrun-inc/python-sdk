# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .cost_breakdown import CostBreakdown
from .billed_breakdown import BilledBreakdown

__all__ = ["AnalyticsInstance"]


class AnalyticsInstance(BaseModel):
    """Analytics details for a single instance within a time bucket"""

    billed_minutes: int = FieldInfo(alias="billedMinutes")
    """Billed minutes with platform multiplier applied"""

    cost: float
    """Total cost in dollars for this instance"""

    instance_tid: str = FieldInfo(alias="instanceTid")
    """Instance type ID (e.g., ios_xxx, android_xxx)"""

    platform: str
    """Platform name, such as android, ios, or sandbox"""

    runtime_minutes: int = FieldInfo(alias="runtimeMinutes")
    """Actual runtime minutes before platform multiplier"""

    billed_breakdown: Optional[BilledBreakdown] = FieldInfo(alias="billedBreakdown", default=None)

    cost_breakdown: Optional[CostBreakdown] = FieldInfo(alias="costBreakdown", default=None)
    """Cost breakdown by billing source in dollars"""

    labels: Optional[Dict[str, str]] = None
    """Instance labels at billing time"""

    region: Optional[str] = None
    """Region where the instance ran"""
