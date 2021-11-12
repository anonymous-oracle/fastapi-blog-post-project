from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import func

from app.oauth2 import get_current_user
from .. import schemas, models
from ..database import Session, get_db

router = APIRouter(prefix="/vote", tags=["Vote"])

# this route is used to handle the vote/like for a post by a user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post {vote.post_id} not found",
        )
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has already voted for post {vote.post_id}",
            )
        new_vote = models.Vote(user_id=current_user.id, post_id=vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has not voted for post {vote.post_id}",
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully down voted"}


@router.get("/{post_id}")
async def get_votes(post_id: int, db: Session = Depends(get_db)):
    join_query = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
    )

    return {
        "votes": join_query.filter(models.Post.id == post_id).first(),
    }
