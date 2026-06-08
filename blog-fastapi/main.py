from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {'data': None, 'detail': "Application en cours..."}

@app.get("/posts")
def get_posts():
    return {"data": None, "detail": "Posts retrieved successfully"}


@app.get("/posts/{id_}")
def get_post(id_: int):
    pass

@app.post("/posts")
def create_post(post_):
    pass

@app.put("/posts/{id_}")
def update_post(id_: int, post_):
    pass

@app.delete("/posts/{id_}")
def delete_post(id_: int):
    pass
