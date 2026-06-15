from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from schemes.todo_schema import TodoPostRequest, TodoUpdateRequest, TodoDictResponse, TodosDictResponse
from schemes.user_schema import UserPostRequest,UserDictResponse
from models.todo_model import Base
from models import todo_model as tm
from models import user_model as um
from pwdlib import PasswordHash

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"data": None, "detail": "Application en cours..."}

@app.post("/todos", status_code=status.HTTP_201_CREATED, response_model=TodoDictResponse)
def post_todo(todo_: TodoPostRequest, db_: Session = Depends(get_db)):
    todo_posted_ = tm.Todo(**todo_.model_dump())
    db_.add(todo_posted_)
    db_.commit()
    db_.refresh(todo_posted_)
    return {"data": todo_posted_, "detail": "Todo posted successfully !"}

@app.get("/todos", response_model=TodosDictResponse)
def get_todos(db_: Session = Depends(get_db)):
    todos_ = db_.query(tm.Todo).all()

    if not todos_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todos Not Found")
    return {"data": todos_, "detail": "All todos retrieved successfully !"}


@app.get("/todos/{id_}", response_model=TodoDictResponse)
def get_post(id_: int, db_: Session = Depends(get_db)):
    todo_ = db_.query(tm.Todo).filter(tm.Todo.id == id_).first()

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_, "detail": "Todo retrieved successfully !"}

@app.delete("/todos/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id_: int, db_: Session = Depends(get_db)):
    todo_ = db_.query(tm.Todo).filter(tm.Todo.id == id_)

    if not todo_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_.delete(synchronize_session=False)
    db_.commit()
    return

@app.put("/todos/{id_}", response_model=TodoDictResponse)
def update_todo(id_: int, todo_: TodoUpdateRequest, db_: Session = Depends(get_db)):
    todo_updated_ = db_.query(tm.Todo).filter(tm.Todo.id == id_)

    if not todo_updated_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_updated_.update(todo_.model_dump(), synchronize_session=False)
    db_.commit()
    return {"data": todo_updated_.first(), "detail": "Todo updated successfully !"}

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserDictResponse)
def create_user(user_: UserPostRequest, db_: Session = Depends(get_db)):
    user_created_ = um.User(**user_.model_dump())
    db_.add(user_created_)
    db_.commit()
    db_.refresh(user_created_)
    return {"data": user_created_, "detail": "User created successfully !"}