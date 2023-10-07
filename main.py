from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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

def find_index_post(id):
    for i, p in enumerate(my_posts):
        return i if p['id'] == id else None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts/", status_code = status.HTTP_201_CREATED)
async def create_posts(post: Post):
    print(post.model_dump())
    return {"data": post}

@app.get("/posts/")
async def get_posts():
    return {"data": my_posts}


#our latest path will be confused with if if not implemented above the get request with id
@app.get("/posts/latest")
async def get_latest_post():
    post = my_posts[:-1]
    return {"latest_post": post}

#the id is always a string so manually convert in to int if needed
@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post_by_id(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")     
    return {"Post details": post}


@app.delete("/posts/{id}")
def delete_post(id:int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)



