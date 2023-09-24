from pydantic import BaseModel


class CardCreateSchema(BaseModel):
    name: str
    who_is_this: str


class CardReadSchema(BaseModel):
    id: int
    name: str
    staff: str


class StaffCreateSchema(BaseModel):
    name: str
    number: str


class StaffReadSchema(BaseModel):
    id: int
    name: str
    number: str


class StudentCreateSchema(BaseModel):
    name: str
    number: str
    paid: bool


class StudentReadSchema(BaseModel):
    id: int
    name: str
    number: str
    paid: bool
