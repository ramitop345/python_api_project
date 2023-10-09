from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
router = APIRouter(prefix = "/posts", tags = ['posts'])


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    query = models.Post(**post.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post was not created")
    return query

@router.get("/", response_model = List[schemas.Post])
async def get_all_posts(db: Session = Depends(get_db)):
    query = db.query(models.Post).all()
    return query


#the id is always a string so manually convert in to int if needed
@router.get("/{id}", response_model = schemas.Post)
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")     
    return query


@router.delete("/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id)
    
    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@router.put("/{id}", status_code = status.HTTP_200_OK)
def update(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id)

    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    query.update(post.model_dump(), synchronize_session = False)
    db.commit()
    return query.first()