from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from schemes.user_schema import TokenData
from datetime import datetime, timedelta, UTC
import os, dotenv, jwt

dotenv.load_dotenv(".env")
SECRET_KEY=os.getenv('AUTH_SECRET_KEY')
ALGORITHM=os.getenv('AUTH_ALGORITHM')
EXPIRES_IN=os.getenv('AUTH_EXPIRES_IN') or 30

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def generate_token(payload_: dict) -> str:
    c_payload_ = payload_.copy()
    expires_in_ = datetime.now(UTC) + timedelta(minutes=float(EXPIRES_IN))
    c_payload_["expires_in"] = expires_in_.__str__()
    encoded_ = jwt.encode(payload=c_payload_, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_

def verify_token(token_: str, credentials_exception_):
    try:
        decoded_ = jwt.decode(token_, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_: int = int(decoded_.get("user_id"))
        user_name_: str = decoded_.get("user_name")

        if not user_id_ or not user_name_:
            raise credentials_exception_
        token_data_ = TokenData(user_id=user_id_, user_name=user_name_)
    except InvalidTokenError:
        raise credentials_exception_

    return token_data_

def get_current_user(token_: str = Depends(oauth2_schema)):
    credential_exception_ = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return verify_token(token_, credential_exception_)