from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def valid_excep_handler(req, exec):
    return PlainTextResponse(str(exec), status_code=400)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="3 is not a good number")
    return {"item_id" : item_id}

# from starlette.exceptions import HTTPException as StarletteHTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(req, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)