import uvicorn
from fastapi import FastAPI, Depends
from db.Database import Base, engine
from router.card_router import router as card_router
from router.staff_router import router as staff_router
from router.student_router import router as student_router
from router.teacher_router import router as teacher_router

app = FastAPI(title="My project")

app.include_router(card_router)
app.include_router(staff_router)
app.include_router(staff_router)
app.include_router(student_router)
app.include_router(teacher_router)

Base.metadata.create_all(engine)