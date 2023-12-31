from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from typing import List, Optional
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from sqlalchemy import func

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
router = APIRouter(prefix = "/posts", tags = ['posts'])


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = models.Post(user_id = current_user.id, **post.model_dump())
    db.add(query)
    db.commit()
    db.refresh(query)
    if  query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post was not created")
    return query
#use %20 in queries (like search) to represent space(like entering two words in query for search)
#@router.get("/", response_model = List[schemas.Post])
@router.get("/")
async def get_all_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #query = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    #the limit parameter is now used to limit the number of posts that can be retrieved
    #the offset parameter allows us to skip a certain number of posts
    query = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    #performing a join sql action below
    #the join method is by default a LEFT INNER JOIN
    result = db.query(models.Post, func.count(models.Vote.post_id).label("votes")
                      ).join(models.Vote, models.Vote.post_id == models.Post.id, 
                             isouter= True).group_by(models.Post.id).filter(
                                 models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #return query
    formatted_result = [{"post": post, "votes": votes} for post, votes in result]
    return formatted_result


#the id is always a string so manually convert in to int if needed
#@router.get("/{id}", response_model = schemas.Post)
@router.get("/{id}")
async def get(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == id).first()
    if query is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")   
    result = db.query(models.Post, func.count(models.Vote.post_id).label("votes")
                      ).join(models.Vote, models.Vote.post_id == models.Post.id, 
                             isouter= True).group_by(models.Post.id).filter(models.Post.id == id).first()
    #return query
    formatted_result = {"post": result[0], "votes": result[1]} 
    return formatted_result

    
    #return query


@router.delete("/{id}")
def delete(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Post).filter(models.Post.id == id)
    
    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    if query.first().user_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=" Not Authorised to perform requested action")
    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@router.put("/{id}", status_code = status.HTTP_200_OK)
def update(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Post).filter(models.Post.id == id)

    if query.first() is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    if query.first().user_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=" Not Authorised to perform requested action")
    query.update(post.model_dump(), synchronize_session = False)
    db.commit()
    return query.first()