from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from models.blogs import Post
from handlers.logger import Logger
import json
from datetime import datetime


custom_logger = Logger(__file__)

api_app = FastAPI(title="api app")

api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api_app.post("/blogs")
async def save_blog(blog: Post):
    print(blog)
   
    data = []
    # Open and read the JSON file
    with open('handlers/database/data.json', 'r') as file:
        data = json.load(file)
        
        data.append({
            "id": str(len(data) + 1),
            "title": blog.title,
            "content": blog.content,
            "author": blog.author,
            "created_at": str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        })
    # Write to the JSON file
    with open('handlers/database/data.json', 'w') as file:
        json.dump(data, file)
   
    custom_logger.logger.info("Blog saved successfully with id %s", str(data[len(data)-1]["id"]))
    
    return {"message": "Blog saved successfully"}

@api_app.get("/blogs/{id}")
async def get_blog_by_id(req: Request, id: str):
    data = {}
    # Open and read the JSON file
    with open('handlers/database/data.json', 'r') as file:
        data = json.load(file)

    resp = data.get(id)
    custom_logger.logger.info("Blog retrieved successfully with id %s", str(resp.id))
    
    return {"message": "Blog retrieved successfully", "data": resp}

@api_app.get("/blogs")
async def get_blogs(req: Request):
    data = {}
    # Open and read the JSON file
    with open('handlers/database/data.json', 'r') as file:
        data = json.load(file)
    custom_logger.logger.info("Blogs retrieved successfully %s", str(data))
    return {"message": "Blogs retrieved successfully", "data": data}

@api_app.delete("/blogs/{id}")
async def delete_blog_by_id(req: Request, id: str):
    data = {}
    # Open and read the JSON file
    with open('handlers/database/data.json', 'r') as file:
        data = json.load(file)
    data.pop(id)
    # Write to the JSON file
    with open('handlers/database/data.json', 'w') as file:
        json.dump(data, file)

    custom_logger.logger.info("Blog deleted successfully with id: %s", str(id))
    return {"message": "Blog deleted successfully"}


@api_app.patch("/blogs/{id}")
async def update_blog_by_id(req: Request, id: str, blog: Post):
    data = {}
    # Open and read the JSON file
    with open('handlers/database/data.json', 'r') as file:
        data = json.load(file)
    data[id] = {
        "title": blog.title,
        "content": blog.content,
        "author": blog.author
    }
    # Write to the JSON file
    with open('handlers/database/data.json', 'w') as file:
        json.dump(data, file)
    
    custom_logger.logger.info("Blog updated successfully with id %s", str(id))
    return {"message": "Blog updated successfully", "data": data[id]}
