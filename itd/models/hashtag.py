from uuid import UUID

from pydantic import BaseModel, Field

class Hashtag(BaseModel):
    id: UUID
    name: str
    posts_count: int = Field(0, alias='postsCount')