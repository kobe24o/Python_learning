# routers/users.py
# 将与用户相关的路径操作与其他代码分开，以使其井井有条
from fastapi import APIRouter
router = APIRouter()
# 你可以将 APIRouter 视为一个「迷你 FastAPI」类
# 在此示例中，该变量被命名为 router，但你可以根据你的想法自由命名

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}