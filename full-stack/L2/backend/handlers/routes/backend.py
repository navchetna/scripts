from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from handlers.database.database import prisma
from models.blogs import Post
from handlers.logger import Logger


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
   
    resp = await prisma.post.create(
        data={
            "title": blog.title,
            "content": blog.content,
            "author": blog.author,
        }
    )  
    custom_logger.logger.info("Blog saved successfully with id: %s", resp.id)
    
    return {"message": "Blog saved successfully"}

@api_app.get("/blogs/{id}")
async def get_blog_by_id(req: Request, id: int):

    resp = await prisma.post.find_first(where={"id": id})
    custom_logger.logger.info("Blog retrieved successfully with id: %s", resp.id)
    
    return {"message": "Blog retrieved successfully", "data": resp}

@api_app.get("/blogs")
async def get_blogs(req: Request):
    resp = await prisma.post.find_many()
    return {"message": "Blogs retrieved successfully", "data": resp}

@api_app.delete("/blogs/{id}")
async def delete_blog_by_id(req: Request, id: int):
    resp = await prisma.post.delete(where={"id": id})
    custom_logger.logger.info("Blog deleted successfully with id: %s", id)


    return {"message": "Blog deleted successfully"}


@api_app.put("/blogs/{id}")
async def update_blog_by_id(req: Request, id: int, blog: Post):
    resp = await prisma.post.update(
        where={"id": id},
        data={
            "title": blog.title,
            "content": blog.content,
            "author": blog.author,
        },
    )
    custom_logger.logger.info("Blog updated successfully with id: %s", id)

    return {"message": "Blog updated successfully", "data": resp}
