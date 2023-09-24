from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Card_pass(Base):
    __tablename__ = 'card-pass'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    staff = Column(String, default="Student", nullable=False)
