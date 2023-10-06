from fastapi import Depends, HTTPException, APIRouter, status

from auth.login import get_current_admin
from db.Database import get_db, SessionLocal
from models.teacher_model import Teacher
from schemas.schemas import StaffCreateSchema, StaffReadSchema
from typing import List

router = APIRouter(prefix="/teacher",
                   tags=["teacher"])


@router.get("/all_teachers", response_model=List[StaffReadSchema])
async def all_teachers(db: SessionLocal = Depends(get_db),
                       login: dict = Depends(get_current_admin)
                       ):
    cards = db.query(Teacher).all()
    return cards


@router.get("/teacher/{id}", response_model=StaffReadSchema)
async def teacher(id: int,
               db: SessionLocal = Depends(get_db),
                  login: dict = Depends(get_current_admin)
                  ):
    teacher = db.query(Teacher).filter(Teacher.id == id).first()
    if teacher is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )
    return teacher


@router.post("/create_teacher", response_model=StaffReadSchema)
async def create_teacher(teacher_schema: StaffCreateSchema,
                      db: SessionLocal = Depends(get_db),
                         login: dict = Depends(get_current_admin)
                         ):
    model = Teacher()
    model.name = teacher_schema.name
    model.number = teacher_schema.number

    db.add(model)
    db.commit()
    return model


@router.put("/change_teacher", response_model=StaffReadSchema)
async def change_teacher(id: int,
                      teacher_schema: StaffCreateSchema,
                      db: SessionLocal = Depends(get_db),
                         login: dict = Depends(get_current_admin)
                         ):
    query = db.query(Teacher).filter(Teacher.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher Not found"
        )
    query.name = teacher_schema.name
    query.number = teacher_schema.number

    db.add(query)
    db.commit()
    return query


@router.delete("/delete_teacher")
async def delete_teacher(id: int,
                      db: SessionLocal = Depends(get_db),
                         login: dict = Depends(get_current_admin)
                         ):
    query = db.query(Teacher).filter(Teacher.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff Not found"
        )
    db.delete(query)
    db.commit()
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Teacher Deleted"
    )
