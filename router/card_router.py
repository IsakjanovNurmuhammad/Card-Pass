import datetime
import json
import uuid

from algorithm import check
from fastapi import Depends, HTTPException, APIRouter, status
from algorithm import checkout
from auth.login import get_current_admin
from db.Database import get_db, SessionLocal
from models.card_model import CardPass
from models.student_model import Student
from models.check_model import CheckIn, CheckOut
from schemas.schemas import CardCreateSchema, CardReadSchema
from typing import List
from sqlalchemy import func
from db.Database import Base, engine

router = APIRouter(prefix="/card",
                   tags=["card"])


@router.get("/all_cards", response_model=List[CardReadSchema])
async def all_cards(db: SessionLocal = Depends(get_db),
                    login: dict = Depends(get_current_admin)):
    cards = db.query(CardPass).all()
    return cards


@router.get("/checkin/{uuid}", response_model=CardReadSchema)
async def checkin(uuid: str,
                  db: SessionLocal = Depends(get_db),
                  login: dict = Depends(get_current_admin)):
    check(uuid, db)


@router.get("/checkout/{out}", response_model=CardReadSchema)
async def checkout(id: str,
                   db: SessionLocal = Depends(get_db),
                   login: dict = Depends(get_current_admin)):
    checkout(id, db)

@router.post("/create_card", response_model=CardReadSchema)
async def create_card(card_schema: CardCreateSchema,
                      db: SessionLocal = Depends(get_db),
                      login: dict = Depends(get_current_admin)):
    model = CardPass()
    model.id = uuid.uuid4()
    model.name = card_schema.name
    model.staff = card_schema.staff

    db.add(model)
    db.commit()
    return model


@router.put("/change_card", response_model=CardReadSchema)
async def change_card(id: int,
                      card_schema: CardCreateSchema,
                      db: SessionLocal = Depends(get_db),
                      login: dict = Depends(get_current_admin)):
    query = db.query(CardPass).filter(CardPass.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card Not found"
        )
    query.name = card_schema.name
    query.staff = card_schema.staff
    db.add(query)
    db.commit()
    return query


@router.delete("/delete_card", response_model=CardReadSchema)
async def change_card(id: int,
                      db: SessionLocal = Depends(get_db),
                      login: dict = Depends(get_current_admin)):
    query = db.query(CardPass).filter(CardPass.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card Not found"
        )
    db.delete(query)
    db.commit()
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Card Deleted"
    )