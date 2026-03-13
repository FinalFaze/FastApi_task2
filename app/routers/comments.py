from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.comment import CommentRepository
from app.schemas.blog import CommentCreate, CommentOut, CommentUpdate

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("", response_model=list[CommentOut])
def list_comments(db: Session = Depends(get_db)):
    return CommentRepository(db).list()


@router.post("", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(payload: CommentCreate, db: Session = Depends(get_db)):
    return CommentRepository(db).create(payload.model_dump())


@router.get("/{comment_id}", response_model=CommentOut)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    return CommentRepository(db).get(comment_id)


@router.put("/{comment_id}", response_model=CommentOut)
def update_comment(comment_id: int, payload: CommentUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return CommentRepository(db).update(comment_id, data)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    CommentRepository(db).delete(comment_id)
