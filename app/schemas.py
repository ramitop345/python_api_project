from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, EmailStr, conint

class UserBase(BaseModel):
    email: EmailStr
    password: str
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: Any

class User(UserBase):
    id: int 
    created_at: Any
    class Config:
        from_attributes = True

class Post(PostBase):
    id: int 
    created_at: Any
    user_id: int
    # we created a relationship in models and the code below retrieves all information from the user that generated this post
    #it is a faster way to than implementing a foreign key to get some data from other table
    owner: UserOut
    #this helps pydantic to recognise the output as dictionary although it is a class
    #this helps limit the number of data that will be returned as response to a query
    class Config:
        from_attributes = True

"""
    schema for sql queries with joins
"""
class PostOut(PostBase):
    Post: Post
    votes: int
    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)