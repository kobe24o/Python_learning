from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class MichaelException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(MichaelException)
async def michael_exception_handler(request: Request, exec: MichaelException):
    return JSONResponse(
        status_code=408,
        content = {"msg": "哦，{}出错了".format(exec.name)})
@app.get("/test/{name}")
async def test(name: str):
    if name == "yoyo":
        raise MichaelException(name)
    return {"test_name" : name}

