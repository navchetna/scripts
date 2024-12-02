from fastapi import FastAPI, Request
from pathlib import Path
from fastapi.responses import StreamingResponse
from handlers.logger import Logger

custom_logger = Logger(__file__)
ui_app = FastAPI(title="ui app")
@ui_app.api_route("/{path_name:path}", methods=["GET"])
async def serve_ui(req: Request, path_name: str):
    reqURL = req.url.path
    custom_logger.logger.info(f"Requested URL " + reqURL)    

    if (path_name == "/" or path_name == ""):
        path_name = "index.html"
    elif (Path(path_name).suffix == ""):
        path_name = path_name+".html"
    return StreamingResponse(open(f"../frontend/out/{path_name}", "rb"))
