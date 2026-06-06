from datetime import datetime
from typing import Optional, Literal, List
from pydantic import BaseModel


class TodoGlobalResponse(BaseModel):
    id: int
    title: str
    done: bool
    date: datetime
    category: Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']

    class Config:
        from_attributes = True

class TodoDictResponse(BaseModel):
    data: TodoGlobalResponse
    detail: str

    class Config:
        from_attributes = True

class TodosDictResponse(BaseModel):
    data: List[TodoGlobalResponse]
    detail: str

    class Config:
        from_attributes = True

class TodoPostRequest(BaseModel):
    title: str
    category: Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']

class TodoUpdateRequest(BaseModel):
    title: Optional[str]
    category: Optional[Literal['courses', 'santé', 'études', 'informatique', 'loisir', 'ménage']]
    done: Optional[bool]
