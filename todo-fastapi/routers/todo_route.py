from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemes.todo_schema import TodoPostRequest, TodoUpdateRequest, TodoDictResponse, TodosDictResponse
from models import todo_model as tm


router = APIRouter(prefix="/todos", tags=["Posts"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TodoDictResponse)
def post_todo(todo_: TodoPostRequest, db_: Session = Depends(get_db)):
    todo_posted_ = tm.Todo(**todo_.model_dump())
    db_.add(todo_posted_)
    db_.commit()
    db_.refresh(todo_posted_)
    return {"data": todo_posted_, "detail": "Todo posted successfully !"}

@router.get("/", response_model=TodosDictResponse)
def get_todos(db_: Session = Depends(get_db)):
    todos_ = db_.query(tm.Todo).all()

    if not todos_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todos Not Found")
    return {"data": todos_, "detail": "All todos retrieved successfully !"}


@router.get("/{id_}", response_model=TodoDictResponse)
def get_post(id_: int, db_: Session = Depends(get_db)):
    todo_ = db_.query(tm.Todo).filter(tm.Todo.id == id_).first()

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_, "detail": "Todo retrieved successfully !"}

@router.delete("/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id_: int, db_: Session = Depends(get_db)):
    todo_ = db_.query(tm.Todo).filter(tm.Todo.id == id_)

    if not todo_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_.delete(synchronize_session=False)
    db_.commit()
    return

@router.put("/{id_}", response_model=TodoDictResponse)
def update_todo(id_: int, todo_: TodoUpdateRequest, db_: Session = Depends(get_db)):
    todo_updated_ = db_.query(tm.Todo).filter(tm.Todo.id == id_)

    if not todo_updated_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")

    todo_updated_.update(todo_.model_dump(), synchronize_session=False)
    db_.commit()
    return {"data": todo_updated_.first(), "detail": "Todo updated successfully !"}
