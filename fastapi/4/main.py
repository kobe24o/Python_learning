from fastapi import FastAPI, Path, Body
from typing import Optional, List
from pydantic import BaseModel, Field
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="price must be greater than 0")
    description: Optional[str] = Field(None, title="description of item", max_length=30)
    tax: Optional[float] = None
    tags: List[str] = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    res = {"item_id" : item_id, "item" : item}
    return res
