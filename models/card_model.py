import uuid

from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean


class CardPass(Base):
    __tablename__ = 'card_pass'
    id = Column(String)
    name = Column(String, nullable=False)
    staff = Column(String, default="Student", nullable=False)
    index = Column(Integer, primary_key=True, index=True)
