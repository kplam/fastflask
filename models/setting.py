#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-03 01:18:31
'''


try:
    from models.database import *
except ImportError:
    from .database import *


class Setting(db.Model, BaseModelMixin):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    key = Column(VARCHAR(64), nullable=False, unique=True)
    type = Column(VARCHAR(64), nullable=False)
    value = Column(VARCHAR(512), nullable=False)
    remark = Column(VARCHAR(512), nullable=False)


