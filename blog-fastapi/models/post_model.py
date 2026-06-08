from datetime import datetime
from typing import Literal
from sqlmodel import Field, SQLModel


class Posts(SQLModel, table=True):
    __tablename__ = "bf_posts"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, unique=True, max_length=255)
    content: str = Field(nullable=False, max_length=4096)
    image: str = Field(default='pic_default.png', nullable=False)
    category: Literal['art', 'technology', 'science', 'fashion', 'nutrition', 'music', 'game', 'politic', 'others'] = Field(default='others', nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    modify_at: datetime | None = Field(default=None, nullable=True)
    user_id: int = Field(default=1)
