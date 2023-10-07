from fastapi import FastAPI
from fastapi.params import Body
from fastapi.logger import logger


app = FastAPI()

@app.post("/createposts/")
async def create_posts(body: dict = Body(...)):
    print(body)
    return {"new post": f'title: {body["title"]} content: {body["content"]}'}
    


@app.get("/")
async def root():
    return {"message": "Hello World"}