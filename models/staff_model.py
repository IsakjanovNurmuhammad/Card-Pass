from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)