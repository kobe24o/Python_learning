from typing import Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", 
            response_model=Item, 
            tags=["items, ming"], 
            status_code=201,
            summary="创建item",
            response_description="响应的描述"
            )
async def create_item(item: Item):
    '''
    多行注释 --> description，支持 MD 格式
    ## 1. 标题
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    '''
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["michael"], deprecated=True)
async def read_users():
    return [{"username": "johndoe"}]