from fastapi import FastAPI, Depends, status, HTTPException
from database import get_db, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.post_schema import PostCreateRequest, PostUpdateRequest, PostDictResponse
from models import post_model as model


app = FastAPI()
model.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {'data': None, 'detail': "Application en cours..."}

@app.get("/posts", response_model=PostDictResponse)
def get_posts(db_: Session = Depends(get_db)):
    posts_ = db_.query(model.Posts).all()

    if posts_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="An error occurred : no posts found")
    if len(posts_) == 0:
        return {"data": posts_, "detail": "No post created yet"}
    return {"data": posts_, "detail": "Posts retrieved successfully"}


@app.get("/posts/{id_}", response_model=PostDictResponse)
def get_post(id_: int, db_: Session = Depends(get_db)):
    post_ = db_.query(model.Posts).filter(model.Posts.id == id_).first()

    if not post_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id_} not found")
    return {"data": post_, "detail": f"Post id:{id_} retrieved successfully"}

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostDictResponse)
def create_post(post_: PostCreateRequest, db_: Session = Depends(get_db)):
    post_ = model.Posts(**post_.model_dump())
    db_.add(post_)

    try: db_.commit()
    except IntegrityError as err:
        db_.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err.orig.diag.message_detail)
    db_.refresh(post_)
    return {"data": post_, "detail": "Post created successfully"}

@app.put("/posts/{id_}", response_model=PostDictResponse)
def update_post(id_: int, post_: PostUpdateRequest, db_: Session = Depends(get_db)):
    post_updated = db_.query(model.Posts).filter(model.Posts.id == id_)

    if not post_updated.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"An error occurred : Post id:{id_} not found")
    post_updated.update(post_.model_dump(), synchronize_session=False)
    db_.commit()
    return {"data": post_updated.first(), "detail": "Post updated successfully"}

@app.delete("/posts/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id_: int, db_: Session = Depends(get_db)):
    post_ = db_.query(model.Posts).filter(model.Posts.id == id_)

    if not post_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"An error occurred : Post id:{id_} not found")
    post_.delete(synchronize_session=False)
    db_.commit()
    return
