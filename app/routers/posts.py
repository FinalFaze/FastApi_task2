from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.post import PostRepository
from app.schemas.blog import PostCreate, PostOut, PostUpdate

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return PostRepository(db).list()


@router.post("", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(payload: PostCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    if data.get("pub_date") is None:
        data.pop("pub_date")
    return PostRepository(db).create(data)


@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return PostRepository(db).get(post_id)


@router.put("/{post_id}", response_model=PostOut)
def update_post(post_id: int, payload: PostUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    if "pub_date" in data and data["pub_date"] is None:
        data.pop("pub_date")
    return PostRepository(db).update(post_id, data)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    PostRepository(db).delete(post_id)
