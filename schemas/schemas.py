from typing import Optional

from pydantic import BaseModel
from datetime import datetime, date


class CardCreateSchema(BaseModel):
    name: str
    staff: str


class CardReadSchema(BaseModel):
    id: str
    name: str
    staff: str


    class Config:
        orm_mode = True


class StaffCreateSchema(BaseModel):
    name: str
    number: str


class StaffReadSchema(BaseModel):
    id: int
    name: str
    number: str

    class Config:
        orm_mode = True


class StudentCreateSchema(BaseModel):
    name: str
    number: str
    paid: bool


class StudentReadSchema(BaseModel):
    id: int
    name: str
    number: str
    paid: bool

    class Config:
        orm_mode = True


class AdminSchema(BaseModel):
    name: str
    born: date
    created_at: Optional[datetime]
    phone_number: str
    gmail: str
    password: str
    country: str = "UZB"
    region: str
    is_active: bool = True
    is_staff: bool = True
    is_superuser: bool
    is_verified: bool


class AdminReadSchema(BaseModel):
    id: int
    name: str
    born: date
    created_at: datetime
    phone_number: str
    gmail: str
    country: str = "UZB"
    region: str
    is_active: bool = True
    is_staff: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


# class CheckInOutReadSchema(BaseModel):
#     check: datetime
#     name: str
#
#     class Config:
#         orm_mode = True

