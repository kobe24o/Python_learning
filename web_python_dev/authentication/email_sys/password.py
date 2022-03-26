# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 17:33
# @Author : Michael
# @File : password.py
# @desc :

import secrets  # 随机密码生成
from passlib.context import CryptContext  # 密码哈希加密

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')  # bcrypt 单向哈希加密算法


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def generate_token() -> str:
    return secrets.token_urlsafe(32)
