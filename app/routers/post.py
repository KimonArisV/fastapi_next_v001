from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import  engine, get_db

router = APIRouter(prefix='/posts',
                   tags = ["posts"])



@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] =""):
    #posts = db.query(models.Post).all()
    posts = db.query(models.Post).filter(models.Post.owner_id==current_user.id, models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.post("/",status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts(post: schemas.PostCreate, 
                 db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    
    new_post = models.Post(**post.model_dump(),owner_id = current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.Post) #the id is a path parameter
def get_posts( id: int, db: Session = Depends(get_db) ,current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    #print(post)
    if not post:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id : {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "NOT authorized to perform requested action ") 
    
    return  post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id : {id} does not exists")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "NOT authorized to perform requested action ") 
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post) #here is the schema that will bring to the user
def update_post(id: int, updated_post:schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)): 
    #here is the shema we will retrieve and use 
    post_query = db.query(models.Post).filter(models.Post.id==id)

    post = post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id : {id} does not exists")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "NOT authorized to perform requested action ") 
    post_query.update(updated_post.model_dump() ,synchronize_session=False)
    db.commit()
    return post_query.first()







#below si the same using psycopg2
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}


#below is using psycopg2
# def create_posts(post: Post):
#     cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """ ,
#                    (post.title, post.content, post.published) )
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}

# def get_posts(id: int, response: Response):
#     cursor.execute("""SELECT * FROM posts WHERE id= %s""",(str(id),))
#     post=cursor.fetchone()
#     conn.commit()
#     if not post:
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id : {id} not found")
#     return {"post_detail": post}

# def delete_post(id : int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post ==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail = f"post with id : {id} does not exists")
   
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# def update_post(id: int, post:Post):
#     cursor.execute("""UPDATE posts 
#                    SET title = %s, content=%s, published = %s 
#                    WHERE id=%s
#                    RETURNING *""",
#                     (post.title,post.content,post.published,str(id)))
#     post_dict = cursor.fetchone()
#     conn.commit()
#     if post_dict==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail = f"post with id : {id} does not exists")
    
#     return {"data": post_dict}



