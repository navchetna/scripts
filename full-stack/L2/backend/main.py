import fastapi

from fastapi import FastAPI, HTTPException
import uvicorn
import os
from handlers.routes.ui import ui_app
from handlers.routes.backend import api_app
from handlers.database.database import prisma
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to DB
    await prisma.connect()
    yield
    # Disconnect from DB
    await prisma.disconnect()



app = FastAPI(title="Full Stack Server", lifespan=lifespan)
app.mount("/api", api_app)
app.mount("/", ui_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
