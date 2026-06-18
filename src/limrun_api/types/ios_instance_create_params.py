# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IosInstanceCreateParams",
    "Metadata",
    "Spec",
    "SpecClue",
    "SpecInitialAsset",
    "SpecSandbox",
    "SpecSandboxXcode",
]


class IosInstanceCreateParams(TypedDict, total=False):
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


class SpecInitialAsset(TypedDict, total=False):
    kind: Required[Literal["App"]]

    source: Required[Literal["URL", "AssetName", "AssetID"]]

    asset_id: Annotated[str, PropertyInfo(alias="assetId")]

    asset_name: Annotated[str, PropertyInfo(alias="assetName")]

    launch_mode: Annotated[
        Literal["ForegroundIfRunning", "RelaunchIfRunning", "FailIfRunning"], PropertyInfo(alias="launchMode")
    ]
    """Launch mode specifies how to launch the app after installation.

    If not given, the app won't be launched.
    """

    url: str


class SpecSandboxXcode(TypedDict, total=False):
    enabled: bool


class SpecSandbox(TypedDict, total=False):
    xcode: SpecSandboxXcode


class Spec(TypedDict, total=False):
    clues: Iterable[SpecClue]

    hard_timeout: Annotated[str, PropertyInfo(alias="hardTimeout")]
    """
    After how many minutes should the instance be terminated. Example values 1m,
    10m, 3h. Default is "0" which means no hard timeout.
    """

    inactivity_timeout: Annotated[str, PropertyInfo(alias="inactivityTimeout")]
    """
    After how many minutes of inactivity should the instance be terminated. Example
    values 1m, 10m, 3h. Default is 3m. Providing "0" uses the organization's default
    inactivity timeout.
    """

    initial_assets: Annotated[Iterable[SpecInitialAsset], PropertyInfo(alias="initialAssets")]

    model: Literal["iphone", "ipad", "watch"]
    """The model for the Apple Simulator. Default is iphone."""

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

    sandbox: SpecSandbox
