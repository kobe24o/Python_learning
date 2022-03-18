# _*_ coding: utf-8 _*_
# @Time : 2022/3/18 9:30
# @Author : Michael
# @File : models.py
# @desc :

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from tortoise.models import Model
from tortoise import fields

class PostBase(BaseModel):
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)
    class Config:
        orm_mode = True

class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostDB(PostBase):
    id: int

class PostTortoise(Model):
    id = fields.IntField(pk=True, generated=True) # pk=True 表示主键
    publication_date = fields.DatetimeField(null=False)
    title = fields.CharField(max_length=255, null=False)
    content = fields.TextField(null=False)
    class Meta:
        table = 'posts'
