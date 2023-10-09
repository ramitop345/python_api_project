import datetime
from pydantic import BaseModel
# it is used for validation when requesting datafrom databank
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int 
    created_at: datetime
    #this helps pydantic to recognise the output as dictionary although it is a class
    #this helps limit the number of data that will be returned as response to a query
    class config:
        orm_mode = True