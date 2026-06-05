from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from schemes.todo_schema import TodoGlobalResponse, TodoPostRequest, TodoUpdateRequest
from models.todo_model import Base
from database import engine, get_db
from models.todo_model import db_get_todos, db_post_todo, db_get_todo, db_update_todo, db_delete_todo
from models import todo_model

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"data": None, "detail": "Application en cours..."}

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def post_todo(todo_: TodoPostRequest, db: Session = Depends(get_db)):
    todo_posted_: TodoGlobalResponse = db_post_todo(todo_)
    return {"data": todo_posted_, "detail": "Todo posted successfully !"}

@app.get("/todos")
def get_todos():
    todos_: list[TodoGlobalResponse] = db_get_todos()

    if not todos_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todos Not Found")
    return {"data": todos_, "detail": "All todos retrieved successfully !"}


@app.get("/todos/{id_}")
def get_post(id_: int):
    todo_: TodoGlobalResponse = db_get_todo(id_)

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_, "detail": "Todo retrieved successfully !"}

@app.delete("/todos/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id_: int):
    todo_: TodoGlobalResponse = db_delete_todo(id_)

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return

@app.put("/todos/{id_}")
def update_todo(id_: int, todo_: TodoUpdateRequest):
    todo_updated_: TodoGlobalResponse = db_update_todo(id_, todo_)

    if not todo_updated_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_updated_, "detail": "Todo updated successfully !"}