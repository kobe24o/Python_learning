# main.py 你的应用程序中将所有内容联结在一起的主文件
# 你的大部分逻辑现在都存在于其自己的特定模块中
# 因此主文件的内容将非常简单
from fastapi import Depends, FastAPI
from dependencies import get_query_token, get_token_header
from internal import admin
from routers import items, users
# from .routers.items import router # 以下两行名称重叠，注意避免
# from .routers.users import router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
# users.router 包含了 app/routers/users.py 文件中的 APIRouter
# items.router 包含了 app/routers/items.py 文件中的 APIRouter
app.include_router(
    admin.router,
    prefix="/admin", # 添加路径前缀，而不必修改admin.router
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
    # 但这只会影响我们应用中的 APIRouter，
    # 而不会影响使用admin.router的任何其他代码
)
#  app.include_router()，可以将每个 APIRouter 添加到主 FastAPI 应用程序中

# 多次使用不同的 prefix 包含同一个路由器
app.include_router(
    admin.router,
    prefix="/admin_test", # 添加路径前缀，而不必修改admin.router
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot, diff "}},
    # 但这只会影响我们应用中的 APIRouter，
    # 而不会影响使用admin.router的任何其他代码
)

# 也可以在另一个 APIRouter 中包含一个 APIRouter
# router.include_router(other_router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}