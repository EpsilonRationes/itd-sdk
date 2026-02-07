from pydantic import Field

from itd.models._text import TextObject
from itd.models.user import UserPost
from itd.models.file import Attach


class Comment(TextObject):
    author: UserPost

    likes_count: int = Field(0, alias='likesCount')
    replies_count: int = Field(0, alias='repliesCount')
    is_liked: bool = Field(False, alias='isLiked')

    attachments: list[Attach] = []
    replies: list['Comment'] = []
    reply_to: UserPost | None = None # author of replied comment, if this comment is reply