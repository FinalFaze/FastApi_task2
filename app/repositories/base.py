from typing import Generic, Type, TypeVar

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def list(self) -> list[T]:
        return self.db.query(self.model).order_by(self.model.id).all()

    def get(self, obj_id: int) -> T:
        obj = self.db.get(self.model, obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")
        return obj

    def create(self, data: dict) -> T:
        obj = self.model(**data)
        self.db.add(obj)
        try:
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=str(e.orig))
        self.db.refresh(obj)
        return obj

    def update(self, obj_id: int, data: dict) -> T:
        obj = self.get(obj_id)
        for k, v in data.items():
            setattr(obj, k, v)
        try:
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=str(e.orig))
        self.db.refresh(obj)
        return obj

    def delete(self, obj_id: int) -> None:
        obj = self.get(obj_id)
        self.db.delete(obj)
        try:
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=str(e.orig))
