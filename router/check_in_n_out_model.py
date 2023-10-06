from fastapi import Depends, HTTPException, APIRouter, status

from auth.login import get_current_admin
from db.Database import get_db, SessionLocal
from models.check_model import CheckIn, CheckOut
from typing import List
# from schemas.schemas import CheckInOutReadSchema



router = APIRouter(prefix="/check",
                   tags=["check"])


@router.get("/all_chekins")
async def all_checkins(db: SessionLocal = Depends(get_db),
                       login: dict = Depends(get_current_admin)):
    checkins = db.query(CheckIn).all()
    return checkins


@router.get("/checkin_by_name/{name}")
async def checkin_by_name(name: str,
                          db: SessionLocal = Depends(get_db),
                          login: dict = Depends(get_current_admin)):
    checkins = db.query(CheckIn).filter(CheckIn.name == name).all()
    if checkins is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No checkins")
    return checkins


@router.get("/all_chekouts")
async def all_checkouts(db: SessionLocal = Depends(get_db),
                        login: dict = Depends(get_current_admin)):
    checkouts = db.query(CheckOut).all()
    return checkouts


@router.get("/checkout_by_name/{name}")
async def checkout_by_name(name: str,
                          db: SessionLocal = Depends(get_db),
                           login: dict = Depends(get_current_admin)):
    checkouts = db.query(CheckIn).filter(CheckIn.name == name).all()
    if checkouts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No checkouts")
    return checkouts
