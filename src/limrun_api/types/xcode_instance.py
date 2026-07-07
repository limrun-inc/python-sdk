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

    termination_reason: Optional[str] = FieldInfo(alias="terminationReason", default=None)
    """Machine-readable reason the instance was terminated.

    Always present once state is "terminated", never present before that. New values
    may be added over time, so treat any unrecognized value as "Unknown". Known
    values:

    - "UserRequested": terminated by a delete request to the API.
    - "InactivityTimeout": the timeout given in spec.inactivityTimeout elapsed.
    - "HardTimeout": the timeout given in spec.hardTimeout elapsed.
    - "Unknown": terminated for a cause the platform did not attribute, including
      instances that failed to get ready during creation. See errorMessage for
      details when available.
    """


class XcodeInstance(BaseModel):
    metadata: Metadata

    spec: Spec

    status: Status
