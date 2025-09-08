from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `limrun_v1.resources` module.

    This is used so that we can lazily import `limrun_v1.resources` only when
    needed *and* so that users can just import `limrun_v1` and reference `limrun_v1.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("limrun_v1.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
