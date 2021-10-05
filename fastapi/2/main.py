from fastapi import FastAPI

my_app = FastAPI()  # my_app 实例, 名字对应于 终端里的


@my_app.get("/")
async def root():
    return {"message": "Hello World"}


@my_app.get("/items/{item_id}")
async def read_item(item_id: int):  # 要跟上面的 {} 内保持一致
    return {"itemid": item_id}


@my_app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@my_app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


from enum import Enum

app = FastAPI()


class ModelName(str, Enum):  # 继承string， 枚举， 必须是字符串且是指定的枚举值
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

from typing import Optional


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        item_id: str, user_id: int, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# @app.get("/items")
# async def read_item1(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:skip + limit]
