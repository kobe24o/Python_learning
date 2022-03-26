# _*_ coding: utf-8 _*_
# @Time : 2022/3/23 14:37
# @Author : Michael
# @File : models.py
# @desc :

from datetime import datetime
from typing import Optional, List
from bson import ObjectId  # A MongoDB ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoBaseModel(BaseModel):
    # PyObjectId 类的作用是 使得 ObjectId 成为 Pydantic 兼容的类型
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    # alias 是一个 pydantic选项，在调用 dict 方法时，会转换为 _id 名，这是MongoDB需要的

    class Config:
        json_encoders = {ObjectId: str}
        # json序列化时，采用的映射方法，ObjectId自己实现了__str__，可以被映射为 str


class PostBase(MongoBaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class CommentBase(BaseModel):
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str


class CommentCreate(CommentBase):
    pass


class CommentDB(CommentBase):
    pass

class PostDB(PostBase):
    comments: List[CommentDB] = Field(default_factory=list)