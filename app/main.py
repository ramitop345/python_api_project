from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas
from typing import List
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts", status_code = status.HTTP_201_CREATED, response_model = schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    query = models.Post(**post.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post was not created")
    return query

@app.get("/posts", response_model = List[schemas.Post])
async def get_all_posts(db: Session = Depends(get_db)):
    query = db.query(models.Post).all()
    return query


#the id is always a string so manually convert in to int if needed
@app.get("/posts/{id}", response_model = schemas.Post)
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")     
    return query


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
    return query.first()


@app.post("/users", status_code = status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    query = models.User(**user.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user was not created")
    return query

@app.get("/users", response_model = List[schemas.UserOut])
async def get_all_users(db: Session = Depends(get_db)):
    query = db.query(models.User).all()
    return query

@app.get("/users/{id}", response_model = schemas.UserOut)
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found")     
    return query

@app.delete("/users/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)
    
    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found") 
    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@app.put("/users/{id}", status_code = status.HTTP_200_OK)
def update(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)

    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found") 
    query.update(user.model_dump(), synchronize_session = False)
    db.commit()
    return query.first()

