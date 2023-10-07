from fastapi import FastAPI
from fastapi.params import Body
from fastapi.logger import logger
from pydantic import BaseModel

app = FastAPI()

# it is used for validation when requesting datafrom databank
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.post("/createposts/")
async def create_posts(new_post: Post):
    print(new_post.title)
    return {"data": new_post}
    


@app.get("/")
async def root():
    return {"message": "Hello World"}