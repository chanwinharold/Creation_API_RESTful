from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import user_model as um
from utils import verify_password
import oauth2

router = APIRouter(prefix="/auth", tags=["Authentification"])


@router.post("/login")
def login(user_: OAuth2PasswordRequestForm = Depends(), db_: Session = Depends(get_db)):

    user_fetched_ = db_.query(um.User).filter(um.User.name == user_.username).first()
    if not user_fetched_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials !")

    is_valid = verify_password(user_.password, str(user_fetched_.password))
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    generated_token_ = oauth2.generate_token(payload_={"user_id": user_fetched_.id, "name": user_fetched_.name})
    return {
        "data": {
            "token": generated_token_,
            "token_type": "cookie"
        },
        "detail": "User logged in successfully !"
    }
