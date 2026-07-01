# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AnalyticsGetInstancesParams"]


class AnalyticsGetInstancesParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Start of the time range (inclusive, RFC3339)"""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the time range (exclusive, RFC3339)"""

    labels: str
    """Label selector to filter instances (e.g., "env=prod,team=backend")"""

    region: str
    """Optional region filter"""

    timezone: str
    """Optional IANA timezone used for minute bucket grouping.

    Defaults to America/Los_Angeles when omitted.
    """
