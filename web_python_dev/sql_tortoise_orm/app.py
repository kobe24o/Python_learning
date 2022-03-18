# _*_ coding: utf-8 _*_
# @Time : 2022/3/18 9:57
# @Author : Michael
# @File : app.py
# @desc :

TORTOISE_ORM = {
    "connections": {"default": "'sqlite:///cp6_tortoise.db'"},
    "apps": {
        "models": {
            "models": ["chapter6.tortoise.models"],
            "default_connection": "default",
        },
    },
}