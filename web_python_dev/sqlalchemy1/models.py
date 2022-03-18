# models.py

import sqlalchemy
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

metadata = sqlalchemy.MetaData()  # 创建元数据对象

posts = sqlalchemy.Table(  # 创建表对象
    'posts',  # 表名
    metadata,  # 元数据对象
    # 列对象（列名，类型，其他选项）
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('publication_date', sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column('title', sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column('text', sqlalchemy.Text(), nullable=False),
)


class PostBase(BaseModel):
    title: str
    text: str
    publication_date: datetime = Field(dafault_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostDB(PostBase):
    id: int


comments = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column(
        "post_id", sqlalchemy.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    ),
    sqlalchemy.Column("publication_date", sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.Text(), nullable=False),
)


class CommentBase(BaseModel):
    post_id: int
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str


class CommentCreate(CommentBase):
    pass


class CommentDB(CommentBase):
    id: int

class PostPublic(PostDB):
    comments: Optional[List[CommentDB]] = None