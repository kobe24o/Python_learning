from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Item = Body(
        ...,
        example = {
            "name": "michael",
            "description": "a learner",
            "price": 100.1, 
            "tax": 0.1
        }
    )
):
    res = {"item_id": item_id, "item": item}
    return res