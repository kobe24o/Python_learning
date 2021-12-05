# pip install fastapi
# pip install uvicorn[standard]

from typing import Optional  # typing 模块用于类型检查
from fastapi import FastAPI, Header, Cookie, Response
from pydantic import BaseModel

# pydantic库是一种常用的用于数据接口schema定义与检查的库

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root(response: Response):
    response.headers["x-custom-header"] = "myvalue"
    response.set_cookie(key="mycookie", value="myvalue")
    return {'Hello1_nihao': 'world'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)