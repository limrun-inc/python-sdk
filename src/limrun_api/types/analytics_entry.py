# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .analytics_instance import AnalyticsInstance
from .analytics_region_stats import AnalyticsRegionStats

__all__ = ["AnalyticsEntry"]


class AnalyticsEntry(BaseModel):
    """Analytics data for a single time bucket, broken down by platform and region"""

    android: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for Android"""

    ios: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for iOS"""

    sandbox: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for Sandbox"""

    timestamp: str
    """
    RFC3339 timestamp for the start of the bucket in the requested timezone,
    including the local offset
    """

    instances: Optional[List[AnalyticsInstance]] = None
    """Individual instance details for this time bucket"""
