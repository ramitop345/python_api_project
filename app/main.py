from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#this command is now executed in alembic and no more needed here
#it was used to generate all the tables that are created in the models file
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = []

#when a request is sent to an app it goes through the middleware 
#before the app performs any operation
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers= ["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
