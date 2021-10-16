from typing import Optional, List
from fastapi import FastAPI, Query, Path

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(..., min_length=3, max_length=50, regex="^fixedquery$")):
#     res = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         res.update({"q":q})
#     return res
# async def read_items(q: Optional[str] = Query(None, alias = "item-good", deprecated=True)):
#     res = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         res.update({"q":q})
#     return res

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q:str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results