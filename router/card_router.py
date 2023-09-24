import json
from algorithm import Paid_check
from fastapi import Depends, HTTPException, APIRouter, status
from db.Database import get_db, SessionLocal
from models.card_model import Card_pass
from models.student_model import Student
from schemas.schemas import CardCreateSchema, CardReadSchema
from typing import List
from db.Database import Base,engine

router = APIRouter(prefix="/card",
                   tags=["card"])


@router.get("/all_cards", response_model=List[CardReadSchema])
async def all_cards(db: SessionLocal = Depends(get_db)):
    cards = db.query(Card_pass).all()
    return cards


@router.get("/card/{id}", response_model=CardReadSchema)
async def card(id: int,
               db: SessionLocal = Depends(get_db)):
    card = db.query(Card_pass).filter(Card_pass.id == id).first()
    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    

@router.post("/create_card",response_model=CardReadSchema)
async def create_card(card_schema: CardCreateSchema,
                      db: SessionLocal = Depends(get_db)):
    model = Card_pass()
    model.name = card_schema.name
    model.staff = card_schema.who_is_this

    db.add(model)
    db.commit()
    return model


@router.put("/change_card", response_model=CardReadSchema)
async def change_card(id: int,
                      card_schema: CardCreateSchema,
                      db: SessionLocal = Depends(get_db)):
    query = db.query(Card_pass).filter(Card_pass.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card Not found"
        )
    if card_schema.is_teacher is True:
        staff = "teacher"
    else:
        staff = "staff"
    query.name = card_schema.name
    query.staff = staff

    db.add(query)
    db.commit()
    return query


@router.delete("/delete_card", response_model=CardReadSchema)
async def change_card(id: int,
                      db: SessionLocal = Depends(get_db)):
    query = db.query(Card_pass).filter(Card_pass.id == id).first()
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
