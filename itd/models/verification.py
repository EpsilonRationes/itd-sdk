from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

class Verification(BaseModel):
    id: UUID
    user_id: UUID = Field(alias='userId')
    video_url: str = Field(alias='videoUrl')
    status: str # should be enum, but we dont know all statuses (what status for accepted?)

    reject_reason: str | None = Field(None, alias='rejectionReason')
    reviewer: str | None = Field(None, alias='reviewedBy')
    reviewed_at: datetime | None = Field(None, alias='reviewedAt')

    created_at: datetime = Field(alias='createdAt')
    updated_at: datetime = Field(alias='updatedAt')


class VerificationStatus(BaseModel):
    status: str # should be enum, but we dont know all statuses (what status for accepted?)
    request_id: UUID = Field(alias='requestId')
    submitted_at: datetime = Field(alias='submittedAt')