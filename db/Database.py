from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:5781995@localhost:5432/card-pass"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine.connect()
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

