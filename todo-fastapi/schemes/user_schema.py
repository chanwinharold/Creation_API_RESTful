from datetime import datetime
from typing import Optional, Literal, List
from pydantic import BaseModel, EmailStr


class UserPostRequest(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    password: str

class UserUpdateRequest(UserPostRequest):
    confirm_password: str

class UserGlobalResponse(BaseModel):
    name: str
    email: Optional[EmailStr]
    created_at: datetime

class UserDictResponse(BaseModel):
    data: UserGlobalResponse | None
    detail: str