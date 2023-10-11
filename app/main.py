from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user,auth,vote
from .config import settings

#this command is now executed in alembic and no more needed here
#it was used to generate all the tables that are created in the models file
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
