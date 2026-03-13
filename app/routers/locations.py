from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.location import LocationRepository
from app.schemas.blog import LocationCreate, LocationOut, LocationUpdate

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("", response_model=list[LocationOut])
def list_locations(db: Session = Depends(get_db)):
    return LocationRepository(db).list()


@router.post("", response_model=LocationOut, status_code=status.HTTP_201_CREATED)
def create_location(payload: LocationCreate, db: Session = Depends(get_db)):
    return LocationRepository(db).create(payload.model_dump())


@router.get("/{location_id}", response_model=LocationOut)
def get_location(location_id: int, db: Session = Depends(get_db)):
    return LocationRepository(db).get(location_id)


@router.put("/{location_id}", response_model=LocationOut)
def update_location(location_id: int, payload: LocationUpdate, db: Session = Depends(get_db)):
    data = payload.model_dump(exclude_unset=True)
    return LocationRepository(db).update(location_id, data)


@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    LocationRepository(db).delete(location_id)
