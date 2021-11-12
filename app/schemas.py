from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BasePost(BaseModel):
    class Config:
        orm_mode = True


class Post(BasePost):
    title: str
    content: str
    published: bool = True


class BaseUser(BaseModel):
    class Config:
        orm_mode = True


class User(BaseUser):
    email: str
    password: str


class UserResponse(BaseUser):
    id: int
    email: str
    created_at: datetime


class UserLogin(BaseUser):
    email: str
    password: str


class PostResponse(BasePost):
    title: str
    content: str
    user_id: int
    created_at: datetime
    user: UserResponse


# access token schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None


# Vote schema
class Vote(BaseModel):
    post_id: int
    # if dir is 1 then it is a vote/like; if it is 0 it is a down-vote/unlike
    dir: int