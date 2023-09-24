from fastapi import Depends, HTTPException, APIRouter, status
from db.Database import get_db, SessionLocal
from models.student_model import Student
from schemas.schemas import StudentCreateSchema, StudentReadSchema
from typing import List

router = APIRouter(prefix="/student",
                   tags=["student"])


@router.get("/all_student", response_model=List[StudentReadSchema])
async def all_students(db: SessionLocal = Depends(get_db)):
    cards = db.query(Student).all()
    return cards


@router.get("/student/{id}", response_model=StudentReadSchema)
async def student(id: int,
               db: SessionLocal = Depends(get_db)):
    staff = db.query(Student).filter(Student.id == id).first()
    if staff is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return staff


@router.post("/create_student", response_model=StudentReadSchema)
async def create_student(student_schema: StudentCreateSchema,
                      db: SessionLocal = Depends(get_db)):
    model = Student()
    model.name = student_schema.name
    model.paid = student_schema.paid
    model.number = student_schema.number

    db.add(model)
    db.commit()
    return model


@router.put("/change_student", response_model=StudentReadSchema)
async def change_student(id: int,
                      student_schema: StudentCreateSchema,
                      db: SessionLocal = Depends(get_db)):
    query = db.query(Student).filter(Student.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not found"
        )
    query.name = student_schema.name
    query.paid = student_schema.paid
    query.number = student_schema.number

    db.add(query)
    db.commit()
    return query


@router.patch("/change-paid")
async def change_paid(id:int, paid: bool, db: SessionLocal = Depends(get_db)):
    query = db.query(Student).filter(Student.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    query.paid = paid
    db.add(query)
    db.commit()
    return "Successfull"

@router.delete("/delete_student")
async def delete_student(id: int,
                      db: SessionLocal = Depends(get_db)):
    query = db.query(Student).filter(Student.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not found"
        )
    db.delete(query)
    db.commit()
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Student Deleted"
    )
