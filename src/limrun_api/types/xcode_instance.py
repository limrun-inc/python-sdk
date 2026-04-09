# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XcodeInstance", "Metadata", "Spec", "Status"]


class Metadata(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    organization_id: str = FieldInfo(alias="organizationId")

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    labels: Optional[Dict[str, str]] = None

    terminated_at: Optional[datetime] = FieldInfo(alias="terminatedAt", default=None)


class Spec(BaseModel):
    inactivity_timeout: str = FieldInfo(alias="inactivityTimeout")

    region: str

    hard_timeout: Optional[str] = FieldInfo(alias="hardTimeout", default=None)


class Status(BaseModel):
    token: str

    state: Literal["unknown", "creating", "assigned", "ready", "terminated"]

    api_url: Optional[str] = FieldInfo(alias="apiUrl", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)


class XcodeInstance(BaseModel):
    metadata: Metadata

    spec: Spec

    status: Status
