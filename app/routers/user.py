from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from typing import List
from ..database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
router = APIRouter()

@router.post("/users", status_code = status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    query = models.User(**user.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user was not created")
    return query

@router.get("/users", response_model = List[schemas.UserOut])
async def get_all_users(db: Session = Depends(get_db)):
    query = db.query(models.User).all()
    return query

@router.get("/users/{id}", response_model = schemas.UserOut)
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found")     
    return query

@router.delete("/users/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)
    
    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found") 
    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@router.put("/users/{id}", status_code = status.HTTP_200_OK)
def update(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    query = db.query(models.User).filter(models.User.id == id)

    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"user with id: {id} was not found") 
    query.update(user.model_dump(), synchronize_session = False)
    db.commit()
    return query.first()