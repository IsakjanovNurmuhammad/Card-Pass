import json
from datetime import datetime

from fastapi import Depends, HTTPException, APIRouter, status
from db.Database import get_db, SessionLocal
from models.card_model import CardPass
from schemas.schemas import CardCreateSchema, CardReadSchema
from typing import List
from models.card_model import CardPass
from models.student_model import Student
from models.check_model import CheckIn, CheckOut
from sqlalchemy import func


def Paid_check(name, db, model):
    query = db.query(model).filter(model.name == name).first()
    paid = query.paid
    if paid == True:
        return True
    else:
        return False


def checkin_approve(name,
                    db):
    last_checkin = db.query(CheckIn).order_by(CheckIn.id.desc()).first()
    last_checkout = db.query(CheckOut).order_by(CheckOut.id.desc()).first()
    if last_checkout is None or last_checkin is None:
        return True
    else:
        checkin = last_checkin.CheckedIn
        checkout = last_checkout.CheckedOut
        if checkin is None and checkout is None:
            return True
        elif checkout is None:
            return False
        elif checkout > checkin:
            return True
        elif checkout < checkin:
            return False
        else:
            return False


def checkout_approve(name,
                    db):
    last_checkin = db.query(CheckIn).order_by(CheckIn.id.desc()).first()
    last_checkout = db.query(CheckOut).order_by(CheckOut.id.desc()).first()
    if last_checkout is None or last_checkin is None:
        return True
    else:
        checkin = last_checkin.CheckedIn
        checkout = last_checkout.CheckedOut
        if checkin is None and checkout is None:
            return False
        elif checkout > checkin:
            return False
        elif checkout < checkin:
            return True
        else:
            return True


def check(id: str,
          db):
    card = db.query(CardPass).filter(CardPass.id == id).first()
    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    role = card.staff
    if role == "teacher":
        approve = checkin_approve(card.name, db)
        if approve:
            model = CheckIn()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )

    elif role == "staff":
        approve = checkin_approve(card.name, db)
        if approve:
            model = CheckIn()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )
    name = card.name
    checkit = Paid_check(name, db, Student)
    if checkit == False:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="You should make payment"
        )
    else:
        approve = checkin_approve(card.name, db)
        checkout = checkout_approve(card.name, db)
        name = card.name
        if approve and checkout is False:
            model = CheckIn()
            model.checkin_at = datetime.utcnow()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )


def checkout(id: str,
          db):
    card = db.query(CardPass).filter(CardPass.id == id).first()
    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    role = card.staff
    if role == "teacher":
        approve = checkout_approve(card.name, db)
        if approve:
            model = CheckIn()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )

    elif role == "staff":
        approve = checkout_approve(card.name, db)
        if approve:
            model = CheckIn()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )
    else:
        approve = checkin_approve(card.name, db)
        checkout = checkout_approve(card.name, db)
        name = card.name
        if approve and checkout is False:
            model = CheckIn()
            model.checkin_at = datetime.utcnow()
            model.name = card.name
            db.add(model)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="Pass approved"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Something went wrong"
            )