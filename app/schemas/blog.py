from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ORMOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    description: str
    slug: str = Field(min_length=1, max_length=50)
    is_published: bool = True


class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=256)
    description: Optional[str] = None
    slug: Optional[str] = Field(default=None, min_length=1, max_length=50)
    is_published: Optional[bool] = None


class CategoryOut(ORMOut):
    id: int
    is_published: bool
    created_at: datetime
    title: str
    description: str
    slug: str


class LocationCreate(BaseModel):
    name: str = Field(min_length=1, max_length=256)
    is_published: bool = True


class LocationUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=256)
    is_published: Optional[bool] = None


class LocationOut(ORMOut):
    id: int
    is_published: bool
    created_at: datetime
    name: str


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    text: str
    pub_date: Optional[datetime] = None
    is_published: bool = True
    author_id: int = Field(ge=1)
    category_id: Optional[int] = Field(default=None, ge=1)
    location_id: Optional[int] = Field(default=None, ge=1)
    image: Optional[str] = Field(default=None, max_length=100)


class PostUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=256)
    text: Optional[str] = None
    pub_date: Optional[datetime] = None
    is_published: Optional[bool] = None
    author_id: Optional[int] = Field(default=None, ge=1)
    category_id: Optional[int] = Field(default=None, ge=1)
    location_id: Optional[int] = Field(default=None, ge=1)
    image: Optional[str] = Field(default=None, max_length=100)


class PostOut(ORMOut):
    id: int
    is_published: bool
    created_at: datetime
    title: str
    text: str
    pub_date: datetime
    author_id: int
    category_id: Optional[int]
    location_id: Optional[int]
    image: Optional[str]


class CommentCreate(BaseModel):
    text: str
    author_id: int = Field(ge=1)
    post_id: int = Field(ge=1)


class CommentUpdate(BaseModel):
    text: Optional[str] = None
    author_id: Optional[int] = Field(default=None, ge=1)
    post_id: Optional[int] = Field(default=None, ge=1)


class CommentOut(ORMOut):
    id: int
    text: str
    created_at: datetime
    author_id: int
    post_id: int

class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=150)
    password: str = Field(min_length=1, max_length=128)
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    is_staff: bool = False
    is_active: bool = True
    is_superuser: bool = False


class UserUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=1, max_length=150)
    password: Optional[str] = Field(default=None, min_length=1, max_length=128)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserOut(ORMOut):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    is_superuser: bool
    last_login: Optional[datetime]
    date_joined: datetime
