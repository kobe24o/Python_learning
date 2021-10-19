from fastapi import FastAPI, Path, Body
from typing import Optional, List, Set, Dict
from pydantic import BaseModel, Field, HttpUrl
app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="price must be greater than 0")
    description: Optional[str] = Field(None, title="description of item", max_length=30)
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[List[Image]] = None
    

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    res = {"item_id" : item_id, "item" : item}
    return res
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights