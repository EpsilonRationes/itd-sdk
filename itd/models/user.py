from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

class UserNotification(BaseModel):
    id: UUID
    username: str
    display_name: str = Field(alias='displayName')
    avatar: str

    model_config = {'populate_by_name': True}


class UserPost(UserNotification):
    verified: bool = False


class UserSearch(UserPost):
    followers_count: int = Field(0, alias='followersCount')


class User(UserSearch):
    banner: str | None = None
    bio: str | None = None
    pinned_post_id: UUID | None

    private: bool | None = Field(None, alias='isPrivate') # none for not me
    wall_closed: bool = Field(False, alias='wallClosed')

    following_count: int = Field(0, alias='followingCount')
    posts_count: int = Field(0, alias='postsCount')

    is_following: bool | None = Field(None, alias='isFollowing') # none for me
    is_followed: bool | None = Field(None, alias='isFollowedBy') # none for me

    created_at: datetime = Field(alias='createdAt')
