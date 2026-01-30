from uuid import UUID

from pydantic import BaseModel, Field

class File(BaseModel):
    id: UUID
    url: str
    filename: str
    mime_type: str = Field('image/png', alias='mimeType')
    size: int