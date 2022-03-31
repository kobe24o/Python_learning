# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 19:50
# @Author : Michael
# @File : authentication.py
# @desc :

from typing import Optional
from tortoise.exceptions import DoesNotExist
from web_python_dev.authentication.email_sys.models import AccessToken, AccessTokenTortoise, UserDB, UserTortoise
from web_python_dev.authentication.email_sys.password import verify_password

async def authenticate(email: str, password: str) -> Optional[UserDB]:
    try:
        user = await UserTortoise.get(email=email)
    except DoesNotExist:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return UserDB.from_orm(user)

async def create_access_token(user: UserDB) -> AccessToken:
    access_token = AccessToken(user_col_id=user.id)
    access_token_tortoise = await AccessTokenTortoise.create(**access_token.dict())
    return AccessToken.from_orm(access_token_tortoise)