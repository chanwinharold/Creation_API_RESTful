from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime
from typing import Literal
from database import Base


class Posts(Base):
    __tablename__ = 'bf_posts'

    id: int = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title: str = Column(String, nullable=False, unique=True)
    content: str = Column(String, nullable=False)
    image: str = Column(String, server_default='pic_default.png', nullable=False)
    category: Literal[
        'art', 'technology', 'science',
        'fashion', 'nutrition', 'music',
        'game', 'politic', 'others'
    ] = Column(String, server_default='others', nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    modified_at: datetime | None = Column(TIMESTAMP(timezone=True), nullable=True)
    user_id: int = Column(Integer, nullable=False)
