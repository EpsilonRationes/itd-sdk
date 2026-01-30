from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

from itd.enums import NotificationType, NotificationTargetType
from itd.models.user import UserNotification

class Notification(BaseModel):
    id: UUID
    type: NotificationType

    target_type: NotificationTargetType | None = Field(None, alias='targetType') # none - follows, other - NotificationTragetType.POST
    target_id: int | None = Field(None, alias='targetId') # none - follows

    preview: str | None = None # follow - none, comment/reply - content, repost - original post content, like - post content, wall_post - wall post content

    read: bool = False
    read_at: datetime | None = Field(None, alias='readAt')
    created_at: datetime = Field(alias='createdAt')

    actor: UserNotification