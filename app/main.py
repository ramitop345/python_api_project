from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from fastapi.logger import logger
from pydantic import BaseModel
import mysql.connector


app = FastAPI()


config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'python_api',
    'port': '3308'
}
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary= True)
except mysql.connector.Error as err:
    print(f"Error: {err}")

posts = "CREATE TABLE IF NOT EXISTS posts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(250) NOT NULL, content VARCHAR(3000) NOT NULL, published DATETIME DEFAULT CURRENT_TIMESTAMP)"
cursor.execute(posts)

connection.commit()

# it is used for validation when requesting datafrom databank
class Post(BaseModel):
    title: str
    content: str
    published: datetime
    rating: Optional[int] = None


def get_posts():
    get_query = "SELECT * FROM  posts"
    cursor.execute(get_query)
    return cursor.fetchall()

def get_post_by_id(id: int):
    get_query = f"SELECT * FROM  posts WHERE id = {id}"
    cursor.execute(get_query)
    return cursor.fetchall()

def create_new_post(post:Post):
    post_query = "INSERT INTO posts (title, content, published) VALUES (%s,%s,%s)"
    values = (post.title, post.content, post.published)
    cursor.execute(post_query, values)
    return cursor.rowcount > 0

def delete_post(id: int):
    delete_query = "DELETE FROM posts WHERE id = %s"
    values = (id,)
    cursor.execute(delete_query, values)
    return cursor.rowcount > 0

def update_post(id: int, post: Post):
    update_query = "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s"
    new_date = datetime.now()
    values = (post.title, post.content, new_date, id)
    cursor.execute(update_query, values)
    return cursor.rowcount > 0





@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def create_posts(post: Post):
    created = create_new_post(post)
    if not created:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post was not created")
    return {"data": "added new post"}

@app.get("/posts")
async def get_all_posts():
    return {"data": get_posts()}


#the id is always a string so manually convert in to int if needed
@app.get("/posts/{id}")
async def get(id: int):
    post = get_post_by_id(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")     
    return {"Post details": post}


@app.delete("/posts/{id}")
def delete(id:int):
    deleted = delete_post(id)
    if not deleted:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
    return Response(status_code = status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}", status_code = status.HTTP_200_OK)
def update(id: int, post: Post):
    updated = update_post(id, post)
    if  not updated:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
  
    return {'data': updated}
