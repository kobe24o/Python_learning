# _*_ coding: utf-8 _*_
# @Time : 2022/3/18 9:57
# @Author : Michael
# @File : app.py
# @desc :

from tortoise.contrib.fastapi import register_tortoise
from typing import Optional, List, Tuple
from fastapi import FastAPI, Depends, Query, status, HTTPException
from web_python_dev.sql_tortoise_orm.models import PostDB, PostCreate, PostPartialUpdate, PostTortoise, CommentDB, \
    CommentBase, CommentTortoise, PostPublic
from tortoise.exceptions import DoesNotExist

app = FastAPI()

TORTOISE_ORM = {
    "connections": {"default": "sqlite://cp6_tortoise.db"},
    "apps": {
        "models": {
            "models": ["aerich.models", "web_python_dev.sql_tortoise_orm.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
    # 限制查询页面的显示条数
    capped_limit = min(limit, 100)
    return (skip, capped_limit)


async def get_post_or_404(id: int) -> PostTortoise:
    try:
        return await PostTortoise.get(id=id).prefetch_related("comments")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/posts")
async def list_posts(pagination: Tuple[int, int] = Depends(pagination)) -> List[PostDB]:
    skip, limit = pagination
    posts = await PostTortoise.all().offset(skip).limit(limit)
    results = [PostDB.from_orm(post) for post in posts]
    return results


@app.get("/posts/{id}", response_model=PostPublic)
async def get_post(post: PostTortoise = Depends(get_post_or_404)) -> PostPublic:
    return PostPublic.from_orm(post)


@app.post("/posts", response_model=PostPublic, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate) -> PostPublic:
    post_tortoise = await PostTortoise.create(**post.dict())
    await post_tortoise.fetch_related("comments")
    return PostPublic.from_orm(post_tortoise)
    # 因为 pydantic 中 开启了 orm_mode = True
    # 将 PostTortoise 转换成 Pydantic 模型


@app.patch("/posts/{id}", response_model=PostPublic)
async def update_post(post_update: PostPartialUpdate,
                      post: PostTortoise = Depends(get_post_or_404)) -> PostPublic:
    post.update_from_dict(post_update.dict(exclude_unset=True))
    await post.save()
    return PostPublic.from_orm(post)


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: PostTortoise = Depends(get_post_or_404)) -> None:
    await post.delete()


@app.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentBase) -> CommentDB:
    try:
        await PostTortoise.get(id=comment.post_id)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Post {comment.post_id} does not exist.")
    comment_tortoise = await CommentTortoise.create(**comment.dict())
    return CommentDB.from_orm(comment_tortoise)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app:app", host="127.0.0.1", port=8001, reload=True, debug=True, lifespan='on')
