# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .analytics_region_stats import AnalyticsRegionStats

__all__ = ["AnalyticsSummary"]


class AnalyticsSummary(BaseModel):
    """
    Summary of analytics across all time buckets, broken down by platform and region
    """

    android: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for Android"""

    ios: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for iOS"""

    sandbox: Dict[str, AnalyticsRegionStats]
    """Map of region to analytics stats for Sandbox"""
