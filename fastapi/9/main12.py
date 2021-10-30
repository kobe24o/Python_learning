from fastapi import FastAPI
tags_metadata = [
    {
        "name": "users", # 必须的，跟相应的 tags 参数有相同的名
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/", # url 必须的
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata, openapi_url="/api/v100/michael.json",docs_url="/mydocs", redoc_url=None)

@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]

@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
