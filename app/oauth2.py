from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app import models
from .database import Session, get_db
from . import schemas
from fastapi.security.oauth2 import OAuth2PasswordBearer
from .config import settings

# token related functions in oauth2.py

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    # the 'exp' key is a jwt standard to set expiry time
    to_encode.update({"exp": expiry})

    encoded_jwt = jwt.encode(
        claims=to_encode, key=settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        decoded_jwt = jwt.decode(
            token=token, key=settings.secret_key, algorithms=[settings.algorithm]
        )
        if decoded_jwt.get("id") == None and decoded_jwt.get("email") == None:
            raise credentials_exception
        token_data = schemas.TokenData(
            id=decoded_jwt.get("id"), email=decoded_jwt.get("email")
        )
    except JWTError as e:
        raise credentials_exception
    return token_data


# to get current user
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(
        token=token, credentials_exception=credentials_exception
    )
    return db.query(models.User).filter(models.User.id == token.id).first()
