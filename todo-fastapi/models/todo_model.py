from database import conn, curs
from schemes.todo_schema import TodoGlobalResponse, TodoPostRequest, TodoUpdateRequest

# TODO -> GÉRER LE OPEN ET CLOSE DE LA CONNEXION CONN
def db_get_todos() -> list[TodoGlobalResponse]:
    curs.execute("""SELECT * FROM tf_todos""")
    return curs.fetchall()

def db_get_todo(id_: int) -> TodoGlobalResponse:
    curs.execute("""
        SELECT * FROM tf_todos
        WHERE id = %s
    """, (id_, ))
    return curs.fetchone()

def db_post_todo(todo: TodoPostRequest) -> TodoGlobalResponse:
    curs.execute("""
        INSERT INTO tf_todos (title, category) 
        VALUES (%s, %s)
        RETURNING *
    """, (todo.title, todo.category))
    conn.commit()
    return curs.fetchone()

def db_update_todo(id_: int, todo_: TodoUpdateRequest) -> TodoGlobalResponse:
    curs.execute("""
        UPDATE tf_todos
        SET title = %s, 
            category = %s,
            done = %s
        WHERE id = %s
        RETURNING *
    """, (id_, todo_.title, todo_.category, todo_.done))
    conn.commit()
    return curs.fetchone()

def db_delete_todo(id_: int) -> TodoGlobalResponse:
    curs.execute("""
        DELETE FROM tf_todos
            WHERE id = %s
        RETURNING *
    """, (id_, ))
    conn.commit()
    return curs.fetchone()