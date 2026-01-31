from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from itd.models.user import UserPost
from itd.models.file import Attach


class TextObject(BaseModel):
    id: UUID
    content: str
    author: UserPost
    attachments: list[Attach] = []

    created_at: datetime = Field(alias='createdAt')

    model_config = {'populate_by_name': True}

    @field_validator('created_at', mode='plain')
    @classmethod
    def validate_created_at(cls, v: str):
        try:
            return datetime.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError:
            return datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ')