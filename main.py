from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class  Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "Favourite Cars", "content": "I love Subarus", "id": 2}]

@app.get("/")
def root():
    return {"message": "Hello World-Chacha"}

# @app.get("/posts")
# def get_posts():
#     return {"data": "This is your posts"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "successfully created"}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# @app.post("/createposts")
# def create_posts(new_post:Post):
#     print(new_post.rating)
#     return {"data": "new post"}

# @app.post("/posts")
# def create_posts(post:Post):
#     print(post)
#     print(post.dict())
#     return {"data": post}

@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

#title str, content str