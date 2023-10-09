from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from fastapi.logger import logger
import mysql.connector
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    query = models.Post(**post.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query in None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post was not created")
    return {"data": query}

@app.get("/posts")
async def get_all_posts(db: Session = Depends(get_db)):
    query = db.query(models.Post).all()
    return {"data": query}


#the id is always a string so manually convert in to int if needed
@app.get("/posts/{id}")
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")     
    return {"Post details": query}


@app.delete("/posts/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id)
    
    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}", status_code = status.HTTP_200_OK)
def update(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id)

    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    query.update(post.model_dump(), synchronize_session = False)
    db.commit()
    return {'data': query.first()}