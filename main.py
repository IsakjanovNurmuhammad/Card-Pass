import uvicorn
from fastapi import FastAPI, Depends
from db.Database import Base, engine
from router.card_router import router as card_router
from router.staff_router import router as staff_router
from router.student_router import router as student_router
from router.teacher_router import router as teacher_router
from router.check_in_n_out_model import router as checkin_out
from auth.admin_auth import router as auth_router
from router.admin_router import router as admin_router

app = FastAPI(title="My project")
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(card_router)
app.include_router(staff_router)
app.include_router(staff_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(checkin_out)
Base.metadata.create_all(engine)
import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)