# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 17:12
# @Author : Michael
# @File : models.py
# @desc :

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timedelta
from web_python_dev.authentication.email_sys.password import generate_token
from tortoise import fields, timezone
from tortoise.models import Model


def get_expire_time(duration_seconds: int = 86400) -> datetime:
    return timezone.now() + timedelta(seconds=duration_seconds)


class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class UserDB(User):
    hashed_password: str


class AccessToken(BaseModel):
    user_id: int
    access_token: str = Field(default_factory=generate_token)
    expire_time: datetime = Field(default_factory=get_expire_time)

    class Config:
        orm_mode = True


class UserTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    email = fields.CharField(max_length=255, unique=True, index=True, null=False)
    hashed_password = fields.CharField(max_length=255, null=False)

    class Meta:
        table = 'users_table'


class AccessTokenTortoise(Model):
    access_token = fields.CharField(pk=True, max_length=255)
    user = fields.ForeignKeyField('models.UserTortise', null=False)
    expire_time = fields.DatetimeField(null=False)

    class Meta:
        table = 'access_tokens_table'
