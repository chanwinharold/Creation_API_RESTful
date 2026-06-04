from database import db
from schemes.todo_schema import TodoGlobalResponse, TodoPostRequest, TodoUpdateRequest


def db_get_todos() -> list[TodoGlobalResponse]:
    db.open()
    db.curs_.execute("""SELECT * FROM tf_todos""")
    res = db.curs_.fetchall()
    db.close()
    return res

def db_get_todo(id_: int) -> TodoGlobalResponse:
    db.open()
    db.curs_.execute("""
        SELECT * FROM tf_todos
        WHERE id = %s
    """, (id_, ))
    res = db.curs_.fetchone()
    db.close()
    return res

def db_post_todo(todo: TodoPostRequest) -> TodoGlobalResponse:
    db.open()
    db.curs_.execute("""
        INSERT INTO tf_todos (title, category) 
        VALUES (%s, %s)
        RETURNING *
    """, (todo.title, todo.category))
    db.conn_.commit()
    res = db.curs_.fetchone()
    db.close()
    return res

def db_update_todo(id_: int, todo_: TodoUpdateRequest) -> TodoGlobalResponse:
    db.open()
    db.curs_.execute("""
        UPDATE tf_todos
        SET title = %s, 
            category = %s,
            done = %s
        WHERE id = %s
        RETURNING *
    """, (todo_.title, todo_.category, todo_.done, id_))
    db.conn_.commit()
    res = db.curs_.fetchone()
    db.close()
    return res

def db_delete_todo(id_: int) -> TodoGlobalResponse:
    db.open()
    db.curs_.execute("""
        DELETE FROM tf_todos
            WHERE id = %s
        RETURNING *
    """, (id_, ))
    db.conn_.commit()
    res = db.curs_.fetchone()
    db.close()
    return res
