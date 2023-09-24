from db.Database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)