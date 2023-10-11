from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from typing import List, Optional
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
router = APIRouter(prefix = "/vote", tags = ['vote'])


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.Vote)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    actual_post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not actual_post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="post was not found in database")
    query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == vote.user_id)
    found_vote  =query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "vote does not exist")
        query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted vote"}