from datetime import datetime
from typing import Any
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    password: str
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int 
    created_at: Any
    #this helps pydantic to recognise the output as dictionary although it is a class
    #this helps limit the number of data that will be returned as response to a query
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int 
    created_at: Any
    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: Any