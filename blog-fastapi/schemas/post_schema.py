from datetime import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    image: str
    category: Literal[
        'art', 'technology', 'science',
        'fashion', 'nutrition', 'music',
        'game', 'politic', 'others'
    ]

class PostCreateRequest(PostBase):
    user_id: int

class PostUpdateRequest(PostBase):
    modified_at: Optional[datetime] = datetime.now()

class PostResponse(PostBase):
    id: int
    modified_at: Optional[datetime]

class PostDictResponse(BaseModel):
    data: PostResponse | List[PostResponse] | None
    detail: Optional[str] = None