# _*_ coding: utf-8 _*_
# @Time : 2022/3/23 14:37
# @Author : Michael
# @File : app.py.py
# @desc :

from typing import List, Tuple
from bson import ObjectId, errors  # BSON (Binary JSON) encoding and decoding
from fastapi import Depends, FastAPI, HTTPException, Query, status
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from web_python_dev.mongo_motor.models import PostDB, PostCreate, PostPartialUpdate, CommentCreate

app = FastAPI()
motor_client = AsyncIOMotorClient(
    "mongodb://localhost:27017"
)
database = motor_client["cp6_mongodb"]  # 单个数据库实例


def get_database() -> AsyncIOMotorDatabase:
    return database


async def pagination(skip: int = Query(0, ge=0),
                     limit: int = Query(10, ge=0)) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except (errors.InvalidId, TypeError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_post_or_404(
        id: ObjectId = Depends(get_object_id),
        database: AsyncIOMotorDatabase = Depends(get_database)
) -> PostDB:
    raw_post = await database['posts'].find_one({"_id": id})
    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return PostDB(**raw_post)


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(
        post: PostCreate, database: AsyncIOMotorDatabase = Depends(get_database)
) -> PostDB:
    post_db = PostDB(**post.dict())
    await database["posts"].insert_one(post_db.dict(by_alias=True))

    post_db = await get_post_or_404(post_db.id, database)

    return post_db

@app.post("/posts/{id}/comments", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_comment(comment:CommentCreate,
                         post:PostDB=Depends(get_post_or_404),
                         database:AsyncIOMotorDatabase=Depends(get_database))->PostDB:
    await database['posts'].update_one(
        {'_id': post.id}, {'$push': {'comments': comment.dict()}}
    )
    post_db = await get_post_or_404(post.id, database)
    return post_db


@app.get("/posts")
async def list_posts(
        pagination: Tuple[int, int] = Depends(pagination),
        database: AsyncIOMotorDatabase = Depends(get_database)
) -> List[PostDB]:
    skip, limit = pagination
    query = database['posts'].find({}, skip=skip, limit=limit)
    # find 第一个参数 是过滤用的，我们要获取所有的，所以留空
    result = [PostDB(**raw_post) async for raw_post in query]
    # async 列表推导
    return result


@app.get("/posts/{id}", response_model=PostDB)
async def get_post(post: PostDB = Depends(get_post_or_404)) -> PostDB:
    return post


@app.patch("/posts/{id}", response_model=PostDB)
async def update_post(
        post_update: PostPartialUpdate,
        post: PostDB = Depends(get_post_or_404),
        database: AsyncIOMotorDatabase = Depends(get_database),
) -> PostDB:
    await database["posts"].update_one(
        {"_id": post.id}, {"$set": post_update.dict(exclude_unset=True)}
    )

    post_db = await get_post_or_404(post.id, database)

    return post_db


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
        post: PostDB = Depends(get_post_or_404),
        database: AsyncIOMotorDatabase = Depends(get_database),
):
    await database["posts"].delete_one({"_id": post.id})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True, debug=True)
