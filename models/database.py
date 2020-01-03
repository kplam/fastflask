#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors: Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime: 2019-12-07 03:30:16
'''


from flask_sqlalchemy import SQLAlchemy
import datetime
from decimal import Decimal as dec
from sqlalchemy import Column, VARCHAR, Integer, Boolean, ForeignKey, DateTime, JSON, Text, Date, Float, Enum, PickleType, DECIMAL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# import redis
import json
from conf import config
from conf.message import M
from libs.base import pattern
# from sqlalchemy.ext import mutable
import re
from copy import deepcopy


db = SQLAlchemy()


# class JsonEncodedDict(db.TypeDecorator):
#     """Enables JSON storage by encoding and decoding on the fly."""
#     impl = db.Text

#     def process_bind_param(self, value, dialect):
#         if value is not None:
#             value = json.dumps(value)
#         return value

#     def process_result_value(self, value, dialect):
#         if value is not None:
#             value = json.loads(value)
#         return value

# mutable.MutableDict.associate_with(JsonEncodedDict)


class BaseModelMixin(object):
    __table_args__ = {"useexisting": True}

    def to_dict(self):
        result = {}
        for c in self.__table__.columns:
            if 'password' not in str(c.name):
                value = getattr(self, c.name, None)
                if isinstance(value, datetime.datetime):
                    value = str(value)
                if isinstance(value, datetime.date):
                    value = str(value)
                if isinstance(value, dec):
                    value = float(value)
                if c.name == 'wechat':
                    if value is None:
                        value = False
                    else:
                        value = True
                # print(c.type.__visit_name__)
                if c.type.__visit_name__ == 'JSON':
                    if value is None:
                        value = None
                    else:
                        try:
                            value = json.loads(value)
                        except:
                            value = value
                result[str(c.name)] = value            
        return result

    def __str__(self):
        return str(self.to_dict())


def check_model_args(Model,args):
    keys = []
    neededkeys=[]
    for c in Model.__table__.columns:
        keys.append(c.name)
        # print(c.name,c.nullable,c.default,c.autoincrement)

        if c.nullable is False and c.default is None and c.name not in ['id', 'lasteditor', 'lastupdate']:
            neededkeys.append(c.name)
    # print(keys, neededkeys)
    for k in neededkeys:
        if k not in args:
            return False, M['needargs'], keys, args
    d = deepcopy(args)
    for k, v in args.items():
        if k not in keys:
            del d[k]
        else:
            if Model.__table__.c[k].type.__visit_name__ == 'JSON':
                if v is not None:
                    try:
                        d[k] = json.dumps(v)
                    except:
                        return False, M['badargs'], keys, d
            else:
                column_type = Model.__table__.c[k].type.python_type
                if column_type == datetime.date:
                    if not re.match(pattern['date'],str(v)) and v is not None:
                        return False, M['badargs'], keys, d
                if column_type == datetime.datetime:
                    if not re.match(pattern['datetime'],str(v)) and v is not None:
                        return False, M['badargs'], keys, d
                if column_type in [float, int, dec]:
                    if not re.match(pattern['number'],str(v)) and v is not None:
                        return False, M['badargs'], keys, d
                if column_type == bool:
                    if v in ['1', True, 'enable', 1, 'True','true','Enable']:
                        d[k] = True
                    else:
                        d[k] = False

    return True, deepcopy(M['success']), keys, d