# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncAndroidInstance", "AsyncAndroidInstance"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


@runtime_checkable
class AndroidInstanceItem(Protocol):
    id: Optional[str]


class SyncAndroidInstance(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, AndroidInstanceItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, AndroidInstanceItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"data": data}),
            },
        )


class AsyncAndroidInstance(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("endingBefore", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, AndroidInstanceItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"startingAfter": item.id})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, AndroidInstanceItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"endingBefore": item.id})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"data": data}),
            },
        )
