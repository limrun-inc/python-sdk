# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncInstances", "AsyncInstances"]

_T = TypeVar("_T")


@runtime_checkable
class InstancesItem(Protocol):
    id: str


class SyncInstances(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    instances: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        instances = self.instances
        if not instances:
            return []
        return instances

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        instances = self.instances
        if not instances:
            return None

        if is_forwards:
            item = cast(Any, instances[-1])
            if not isinstance(item, InstancesItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.instances[0])
            if not isinstance(item, InstancesItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})


class AsyncInstances(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    instances: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        instances = self.instances
        if not instances:
            return []
        return instances

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        instances = self.instances
        if not instances:
            return None

        if is_forwards:
            item = cast(Any, instances[-1])
            if not isinstance(item, InstancesItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.instances[0])
            if not isinstance(item, InstancesItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})
