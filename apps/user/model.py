# ORM  类 ---> 表
# 类对象 ---> 一条数据
from datetime import datetime

from ext import db


# creat table user(id int primarykey auto_increment, username varchar(20) not null, ...)
class User(db.Model):
    # db.Column(类型，约束)，映射表中的列
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11))
    isdelete = db.Column(db.Boolean, default=False)  # 是否删除
    rdatetime = db.Column(db.DateTime, default=datetime.now)  # 添加时间

    def __str__(self):
        return self.username


class UserInfo(db.Model):
    # db.Column(类型，约束)，映射表中的列
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(15), nullable=False)
    sex = db.Column(db.Boolean, default=False)  # False表示男

    def __str__(self):
        return self.realname
