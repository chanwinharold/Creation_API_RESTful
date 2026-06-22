import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
import os, dotenv

dotenv.load_dotenv(".env")
SECRET_KEY=os.getenv('AUTH_SECRET_KEY')
ALGORITHM=os.getenv('AUTH_ALGORITHM')
EXPIRES_IN=os.getenv('AUTH_EXPIRES_IN') or 30


def generate_token(payload_: dict) -> str:
    c_payload_ = payload_.copy()
    expires_in_ = datetime.now() + timedelta(minutes=float(EXPIRES_IN))
    c_payload_["expires_in"] = expires_in_.__str__()
    encoded_ = jwt.encode(payload=c_payload_, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_