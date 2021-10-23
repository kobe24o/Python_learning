from typing import List, Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id] # 提取存储的数据
    stored_item_model = Item(**stored_item_data) # 原来的数据生成新的model
    update_data = item.dict(exclude_unset=True) # 原来的model除去未设置的字段
    updated_item = stored_item_model.copy(update=update_data)# 创建新的model副本，更新数据(只更新设置的字段)
    items[item_id] = jsonable_encoder(updated_item) # 模型副本转换为可存入数据的形式，存入数据库
    return updated_item