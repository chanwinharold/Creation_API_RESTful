from fastapi import FastAPI, status, HTTPException
from schemes.todo_schema import Todo
from random import randint
from models.todo_model import findTodoById, findIndex

app = FastAPI()


all_todos = [
    {
        "id": 1,
        "title": "Faire les courses",
        "done": False,
        "date": "2026-06-05",
        "category": "courses"
    },
    {
        "id": 2,
        "title": "Appeler le dentiste",
        "done": True,
        "date": "2026-06-04",
        "category": "santé"
    },
    {
        "id": 3,
        "title": "Réviser le cours de FastAPI",
        "done": False,
        "date": "2026-06-06",
        "category": "études"
    },
    {
        "id": 4,
        "title": "Nettoyer le clavier",
        "done": False,
        "date": "2026-06-10",
        "category": "informatique"
    },
    {
        "id": 5,
        "title": "Sport (30 min)",
        "done": True,
        "date": "2026-06-03",
        "category": "loisir"
    }
]

@app.get("/")
def root():
    return {"data": None, "detail": "Application en cours..."}


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def post_todo(todo_: Todo):
    del todo_.id
    todo_.id = randint(1, 999999999)
    all_todos.append(todo_.model_dump())

    print(all_todos)
    return {"data": todo_, "detail": "Todo posted successfully !"}

@app.get("/todos")
def get_todos():
    return {"data": all_todos, "detail": "All todos retrieved successfully !"}


@app.get("/todos/{id_}")
def get_post(id_: int):
    todo_ = findTodoById(id_, all_todos)

    if not todo_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return {"data": todo_, "detail": "Todo retrieved successfully !"}

@app.delete("/todos/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id_: int):
    index = findIndex(id_, all_todos)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    all_todos.pop(index)
    return

@app.put("/todos/{id_}")
def update_todo(id_: int, todo_: Todo):
    index = findIndex(id_, all_todos)
    del todo_.id

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    all_todos[index] = todo_.model_dump()
    all_todos[index]['id'] = id_
    return {"data": all_todos[index], "detail": "Todo updated successfully !"}