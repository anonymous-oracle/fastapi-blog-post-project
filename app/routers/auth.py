from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import oauth2
from .. import schemas, models
from ..database import Session, get_db
from ..hashing import check_pwd

router = APIRouter(tags=["Authentication"])

# authentication related routes in auth.py


@router.post("/login", response_model=schemas.Token)
# OAuth2PasswordRequestForm is required to receive the credentials in a form data
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )
    if not user or not check_pwd(user_credentials.password, user.password, user.salt):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )

    # create a token
    token_payload = {"email": user_credentials.username, "id": user.id}
    access_token = oauth2.create_access_token(data=token_payload)

    # return the token as well as the type of token
    return {"access_token": access_token, "token_type": "bearer"}
