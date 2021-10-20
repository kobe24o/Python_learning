from typing import Optional, List
from fastapi import Cookie, FastAPI, Header

app = FastAPI()
@app.get("/items/")
async def read_items(X_token: Optional[List[str]] = Header(None)):
    return {"x_token value:": X_token}
    