from uuid import UUID

from pydantic import BaseModel, Field

class Pagination(BaseModel):
    page: int | None = 1
    limit: int = 20
    total: int | None = None
    has_more: bool = Field(True, alias='hasMore')
    next_cursor: UUID | None = Field(None, alias='nextCursor')