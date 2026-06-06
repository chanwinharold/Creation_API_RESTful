from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from schemes.todo_schema import TodoPostRequest, TodoUpdateRequest
from models.todo_model import Base
from database import engine, get_db
# from models.todo_model import db_get_todos, db_post_todo, db_get_todo, db_update_todo, db_delete_todo
from models import todo_model as model


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"data": None, "detail": "Application en cours..."}

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def post_todo(todo_: TodoPostRequest, db_: Session = Depends(get_db)):
    # todo_posted_: TodoGlobalResponse = db_post_todo(todo_)
    todo_posted_ = model.Todo(**todo_.model_dump())
    db_.add(todo_posted_)
    db_.commit()
    db_.refresh(todo_posted_)
    return {"data": todo_posted_, "detail": "Todo posted successfully !"}

@app.get("/todos")
def get_todos(db_: Session = Depends(get_db)):
    # todos_: list[TodoGlobalResponse] = db_get_todos()
    todos_ = db_.query(model.Todo).all()

    if not todos_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todos Not Found")
    return {"data": todos_, "detail": "All todos retrieved successfully !"}


@app.get("/todos/{id_}")
def get_post(id_: int, db_: Session = Depends(get_db)):
    # todo_: TodoGlobalResponse = db_get_todo(id_)
    todo_ = db_.query(model.Todo).filter(model.Todo.id == id_).first()

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_, "detail": "Todo retrieved successfully !"}

@app.delete("/todos/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id_: int, db_: Session = Depends(get_db)):
    # todo_: TodoGlobalResponse = db_delete_todo(id_)
    todo_ = db_.query(model.Todo).filter(model.Todo.id == id_)

    if not todo_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_.delete(synchronize_session=False)
    db_.commit()
    return

@app.put("/todos/{id_}")
def update_todo(id_: int, todo_: TodoUpdateRequest, db_: Session = Depends(get_db)):
    # todo_updated_: TodoGlobalResponse = db_update_todo(id_, todo_)
    todo_updated_ = db_.query(model.Todo).filter(model.Todo.id == id_)

    if not todo_updated_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_updated_.update(todo_.model_dump(), synchronize_session=False)
    db_.commit()
    return {"data": todo_updated_.first(), "detail": "Todo updated successfully !"}