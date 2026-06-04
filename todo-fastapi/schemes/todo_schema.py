from datetime import time
from typing import Optional
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    done: bool = False
    date: str | time
    category: Optional[str] = None