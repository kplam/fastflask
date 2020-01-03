#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-03 01:19:50
@LastEditors  : Kin P. Lam
@LastEditTime : 2020-01-03 01:31:22
'''


try:
    from models.database import *
except ImportError:
    from .database import *


class Mod(db.Model,BaseModelMixin):
    """
    A sample models
    """

    __tablename__ = 'mod'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(VARCHAR(64), nullable=False)
    number = Column(Float, nullable=False)
    value = Column(VARCHAR(512))
    remark = Column(Text,nullable=False,default='')
    lasteditor = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),
                   nullable=False, index=True)
    lastupdate = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = db.relationship('User', backref=db.backref('mod'))