

def findTodoById(id_: int, liste_: list[dict]) -> dict | None:
    for todo in liste_:
        if todo['id'] == id_:
            return todo
    return None

def findIndex(id_: int, liste_: list[dict]) -> int | None:
    for index, todo in enumerate(liste_):
        if todo['id'] == id_:
            return index
    return None