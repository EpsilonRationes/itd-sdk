from uuid import UUID
from datetime import datetime

from pydantic import Field

from itd.models._text import _TextObject


class CommentShort(_TextObject):
    likes_count: int = Field(0, alias='likesCount')
    replies_count: int = Field(0, alias='repliesCount')
    is_liked: bool = Field(False, alias='isLiked')

    replies: list['CommentShort'] = []