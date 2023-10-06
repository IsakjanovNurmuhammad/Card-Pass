from fastapi import Depends, HTTPException, APIRouter, status

from auth.login import get_current_admin
from db.Database import get_db, SessionLocal
from models.staff_model import Staff
from schemas.schemas import StaffCreateSchema, StaffReadSchema
from typing import List

router = APIRouter(prefix="/staff",
                   tags=["staff"])


@router.get("/all_staff", response_model=List[StaffReadSchema])
async def all_staff(db: SessionLocal = Depends(get_db),
                    login: dict = Depends(get_current_admin)
                    ):
    staff = db.query(Staff).all()
    return staff


@router.get("/staff/{id}", response_model=StaffReadSchema)
async def staff(id: int,
               db: SessionLocal = Depends(get_db),
                login: dict = Depends(get_current_admin)
                ):
    staff = db.query(Staff).filter(Staff.id == id).first()
    if staff is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found"
        )
    return staff


@router.post("/create_staff", response_model=StaffReadSchema)
async def create_staff(staff_schema: StaffCreateSchema,
                      db: SessionLocal = Depends(get_db),
                       login: dict = Depends(get_current_admin)
                       ):
    model = Staff()
    model.name = staff_schema.name
    model.number = staff_schema.number

    db.add(model)
    db.commit()
    return model


@router.put("/change_staff", response_model=StaffReadSchema)
async def change_staff(id: int,
                      staff_schema: StaffCreateSchema,
                      db: SessionLocal = Depends(get_db),
                       login: dict = Depends(get_current_admin)
                       ):
    query = db.query(Staff).filter(Staff.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff Not found"
        )
    query.name = staff_schema.name
    query.number = staff_schema.number

    db.add(query)
    db.commit()
    return query


@router.delete("/delete_staff")
async def delete_staff(id: int,
                      db: SessionLocal = Depends(get_db),
                       login: dict = Depends(get_current_admin)
                       ):
    query = db.query(Staff).filter(Staff.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff Not found"
        )
    db.delete(query)
    db.commit()
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Staff Deleted"
    )
