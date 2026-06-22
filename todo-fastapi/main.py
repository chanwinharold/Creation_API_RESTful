from fastapi import FastAPI
from database import engine
from models.todo_model import Base
from routers import todo_route as todo, user_route as user, auth_route as auth


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"data": None, "detail": "Application en cours..."}
