from fastapi import FastAPI
from fastapi.responses import FileResponse
from os import path

app = FastAPI()

@app.get("/pyfile")
async def get_cat():
    root_directory = path.dirname(path.dirname(__file__))
    file_path = path.join(root_directory, "a.jpg")
    return FileResponse(file_path)

