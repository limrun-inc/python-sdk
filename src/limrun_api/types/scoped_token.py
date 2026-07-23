# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScopedToken"]


class ScopedToken(BaseModel):
    token: str
    """The scoped token, to be sent as a Bearer token or the token query parameter."""

    expires_at: datetime = FieldInfo(alias="expiresAt")

    scopes: List[str]
