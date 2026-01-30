from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

from itd.enums import ReportTargetType, ReportTargetReason

class Report(BaseModel):
    id: UUID
    reason: ReportTargetReason
    description: str | None = None

    target_type: ReportTargetType = Field(alias='targetType')
    target_id: UUID

    created_at: datetime = Field(alias='createdAt')