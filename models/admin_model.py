from datetime import datetime

from sqlalchemy import Integer, String, Boolean, Column, DateTime, func
from db.Database import Base

class AdminModel(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="root")
    born = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    phone_number = Column(String, nullable=False)
    gmail = Column(String, nullable=False, default="root@root.com")
    password = Column(String, nullable=False, default="root")
    country = Column(String, default="UZB")
    region = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)