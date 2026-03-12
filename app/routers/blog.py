from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.blog import (
    CategoryCreate, CategoryOut, CategoryUpdate,
    LocationCreate, LocationOut, LocationUpdate,
    PostCreate, PostOut, PostUpdate,
    CommentCreate, CommentOut, CommentUpdate,
)
from app.repositories.category import CategoryRepository
from app.repositories.location import LocationRepository
from app.repositories.post import PostRepository
from app.repositories.comment import CommentRepository
from app.repositories.user import UserRepository
from app.schemas.blog import UserCreate, UserOut, UserUpdate

router = APIRouter()
from datetime import datetime


@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list()


@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    data["date_joined"] = datetime.utcnow()
    data["last_login"] = None
    return UserRepository(db).create(data)


@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserRepository(db).get(user_id)


@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return UserRepository(db).update(user_id, data)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserRepository(db).delete(user_id)

@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return CategoryRepository(db).list()


@router.post("/categories", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryRepository(db).create(payload.model_dump())


@router.get("/categories/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryRepository(db).get(category_id)


@router.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, payload: CategoryUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return CategoryRepository(db).update(category_id, data)


@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    CategoryRepository(db).delete(category_id)


@router.get("/locations", response_model=list[LocationOut])
def list_locations(db: Session = Depends(get_db)):
    return LocationRepository(db).list()


@router.post("/locations", response_model=LocationOut, status_code=status.HTTP_201_CREATED)
def create_location(payload: LocationCreate, db: Session = Depends(get_db)):
    return LocationRepository(db).create(payload.model_dump())


@router.get("/locations/{location_id}", response_model=LocationOut)
def get_location(location_id: int, db: Session = Depends(get_db)):
    return LocationRepository(db).get(location_id)


@router.put("/locations/{location_id}", response_model=LocationOut)
def update_location(location_id: int, payload: LocationUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return LocationRepository(db).update(location_id, data)


@router.delete("/locations/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    LocationRepository(db).delete(location_id)


@router.get("/posts", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return PostRepository(db).list()


@router.post("/posts", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(payload: PostCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    if data.get("pub_date") is None:
        data.pop("pub_date")
    return PostRepository(db).create(data)


@router.get("/posts/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return PostRepository(db).get(post_id)


@router.put("/posts/{post_id}", response_model=PostOut)
def update_post(post_id: int, payload: PostUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return PostRepository(db).update(post_id, data)


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    PostRepository(db).delete(post_id)


@router.get("/comments", response_model=list[CommentOut])
def list_comments(db: Session = Depends(get_db)):
    return CommentRepository(db).list()


@router.post("/comments", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(payload: CommentCreate, db: Session = Depends(get_db)):
    return CommentRepository(db).create(payload.model_dump())


@router.get("/comments/{comment_id}", response_model=CommentOut)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    return CommentRepository(db).get(comment_id)


@router.put("/comments/{comment_id}", response_model=CommentOut)
def update_comment(comment_id: int, payload: CommentUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return CommentRepository(db).update(comment_id, data)


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    CommentRepository(db).delete(comment_id)
