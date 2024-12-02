import fastapi

from fastapi import FastAPI, HTTPException
import uvicorn
import os
from handlers.routes.ui import ui_app
from handlers.routes.backend import api_app

app = FastAPI(title="Full Stack Server")
app.mount("/api", api_app)
app.mount("/", ui_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
