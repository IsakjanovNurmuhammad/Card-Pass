from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from datetime import datetime
import pytz

class CheckIn(Base):
    __tablename__ = 'check_in'
    id = Column(Integer, primary_key=True, index=True)
    checkin_at = Column(DateTime, default=datetime.utcnow())
    name = Column(String, nullable=False)


class CheckOut(Base):
    __tablename__ = 'check_out'
    id = Column(Integer, primary_key=True, index=True)
    checkout_at = Column(DateTime, default=func.now())
    name = Column(String, nullable=False)
