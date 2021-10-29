# routers/items.py
# 此模块中的所有路径操作都有相同的：
#   路径 prefix：/items
#   tags：（仅有一个 items 标签）
#   额外的 responses
#   dependencies：它们都需要我们创建的 X-Token 依赖项

from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header 

router = APIRouter(
    prefix="/items", # 前缀不能以 / 作为结尾
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
    # 这些参数将应用于此路由器中包含的所有路径操作
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/")
async def read_items():
    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
) # 这个路径操作将包含标签的组合：["items"，"custom"]
# 也会有两个响应，一个用于 404，一个用于 403
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}