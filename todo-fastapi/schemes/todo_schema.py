from datetime import time
from typing import Optional, Literal
from pydantic import BaseModel


class TodoGlobalResponse(BaseModel):
    id: int
    title: str
    done: bool
    date: time
    category: Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']

class TodoPostRequest(BaseModel):
    title: str
    category: Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']

class TodoUpdateRequest(BaseModel):
    title: Optional[str]
    category: Optional[Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']]
    done: Optional[bool]
