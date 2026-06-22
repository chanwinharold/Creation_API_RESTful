from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemes.user_schema import UserPostRequest, UserDictResponse
from models import user_model as um
from utils import hash_password


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserDictResponse)
def create_user(user_: UserPostRequest, db_: Session = Depends(get_db)):
    user_.password = hash_password(user_.password)
    user_created_ = um.User(**user_.model_dump())
    db_.add(user_created_)
    db_.commit()
    db_.refresh(user_created_)
    return {"data": user_created_, "detail": "User created successfully !"}


@router.get("/{id_}", response_model=UserDictResponse)
def get_user(id_: int, db_: Session = Depends(get_db)):
    user_ = db_.query(um.User).filter(um.User.id == id_).first()

    if not user_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User :{id_} doesn't exist")
    return {"data": user_, "detail": "User informations retrieved successfully !"}