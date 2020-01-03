#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-03 02:26:20
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/21 0:16


try:
    from models.database import *
except ImportError:
    from .database import *


class UserGroup(db.Model, BaseModelMixin):
    __tablename__ = 'user_group'
    name = Column(VARCHAR(64), nullable=False, primary_key=True,unique=True)
    remark = Column(VARCHAR(512), nullable=False, default='')
    authority = Column(Integer, nullable=False, default=1)
    status = Column(Boolean, nullable=False, default=True)


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    account = Column(VARCHAR(64), index=True, nullable=False, unique=True)
    name = Column(VARCHAR(64), nullable=False)
    password = Column(VARCHAR(512), nullable=False)
    group = Column(VARCHAR(64), ForeignKey('user_group.name', ondelete='CASCADE', onupdate='CASCADE'),
                   nullable=False, index=True)
    status = Column(Boolean, nullable=False, default=True)
    # wechat = Column(VARCHAR(256))
    user_group = db.relationship('UserGroup', backref=db.backref('user'))


class Auth(db.Model, BaseModelMixin):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    key = Column(VARCHAR(64), index=True, nullable=False)
    group = Column(VARCHAR(64), ForeignKey('user_group.name', ondelete='CASCADE', onupdate='CASCADE'),
                   nullable=False, index=True)
    value = Column(Boolean, nullable=False, default=False)
    remark = Column(VARCHAR(128), nullable=False)

    usergroup = db.relationship('UserGroup', backref=db.backref('auth'))


class LoginRecord(db.Model, BaseModelMixin):
    __tablename__ = 'login_record'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    login_mode = Column(VARCHAR(128), nullable=False)
    useagent = Column(VARCHAR(1024), nullable=False)
    ip = Column(VARCHAR(128), nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = db.relationship('User', backref=db.backref('login_record'))


class OperationRecord(db.Model, BaseModelMixin):
    __tablename__ = 'operation_record'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    endpoint = Column(VARCHAR(512), nullable=False)
    url = Column(VARCHAR(512), nullable=False)
    args = Column(JSON, nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = db.relationship('User', backref=db.backref('operation_record'))