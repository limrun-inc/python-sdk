# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XcodeInstanceCreateParams", "Metadata", "Spec", "SpecClue"]


class XcodeInstanceCreateParams(TypedDict, total=False):
    reuse_if_exists: Annotated[bool, PropertyInfo(alias="reuseIfExists")]
    """
    If there is another instance with given labels and region, return that one
    instead of creating a new instance.
    """

    wait: bool
    """Return after the instance is ready to connect."""

    metadata: Metadata

    spec: Spec


class Metadata(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    labels: Dict[str, str]


class SpecClue(TypedDict, total=False):
    kind: Required[Literal["ClientIP"]]

    client_ip: Annotated[str, PropertyInfo(alias="clientIp")]


class Spec(TypedDict, total=False):
    clues: Iterable[SpecClue]

    hard_timeout: Annotated[str, PropertyInfo(alias="hardTimeout")]
    """
    After how many minutes should the instance be terminated. Example values 1m,
    10m, 3h. Default is "0" which means no hard timeout.
    """

    inactivity_timeout: Annotated[str, PropertyInfo(alias="inactivityTimeout")]
    """
    After how many minutes of inactivity should the instance be terminated. The
    timer starts once the instance becomes ready. Example values 1m, 10m, 3h.
    Default is 5m. Providing "0" uses the organization's default inactivity timeout.
    """

    jurisdiction: Literal["us", "eu", "as"]
    """Restricts scheduling to regions in the given jurisdiction.

    Unlike region, this is a hard constraint: the request never overflows to a
    region outside the jurisdiction and fails when no region in the jurisdiction has
    capacity. A region belongs to a jurisdiction when its name starts with the
    jurisdiction prefix, e.g. "eu-north1" is in "eu". A region preference pointing
    outside the jurisdiction is ignored.
    """

    region: str
    """Where the instance will be created.

    If not given, the region is decided based on scheduling clues (client IP) and
    availability.

    A region is a preference, not a hard pin: the request always overflows to every
    other available region, ordered by proximity, when the preferred ones are full.

    Accepted values:

    - A specific region name (e.g. "us-west1"). It is tried first, then the
      remaining regions in order of proximity to it. Scheduling clues (client IP)
      are ignored when a region is given.
    - A region group name (e.g. "us", "eu"). Its member regions are tried first in
      their listed order, then the remaining regions by proximity to the first
      member.
    - A pipe-separated, ordered list of regions (e.g. "us-east1|us-west1"). Those
      are tried first in the given order, then the remaining regions by proximity to
      the first.
    """
