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
    user_col_id: int
    access_token: str = Field(default_factory=generate_token)
    expiration_date: datetime = Field(default_factory=get_expire_time)

    class Config:
        orm_mode = True


class UserTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    email = fields.CharField(index=True, unique=True, null=False, max_length=255)
    hashed_password = fields.CharField(null=False, max_length=255)

    class Meta:
        table = "users"


class AccessTokenTortoise(Model):
    access_token = fields.CharField(pk=True, max_length=255)
    user_col = fields.ForeignKeyField("models.UserTortoise", null=False)
    expiration_date = fields.DatetimeField(null=False)

    class Meta:
        table = "access_tokens"
