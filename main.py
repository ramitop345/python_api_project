from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from fastapi.logger import logger
from pydantic import BaseModel

app = FastAPI()

# it is used for validation when requesting datafrom databank
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = []


def find_post_by_id(id):
    result = [p for p in my_posts if p["id"] == id]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts/")
async def create_posts(post: Post):
    print(post.model_dump())
    return {"data": post}

@app.get("/posts/")
async def get_posts():
    return {"data": my_posts}

#the id is always a string so manually convert in to int if needed
@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post_by_id(id)
    return {"Post details": post}
    
