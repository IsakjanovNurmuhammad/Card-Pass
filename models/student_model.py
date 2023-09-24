from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)
    paid = Column(Boolean, default=False, nullable=False)



