# _*_ coding: utf-8 _*_
# @Time : 2022/3/8 9:28
# @Author : Michael
# @File : database.py
# @desc :
import sqlalchemy
from databases import Database
DB_URL = 'sqlite:///cp6_sqlalchemy.db'
database = Database(DB_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DB_URL)

def get_database() -> Database:
    return database
