#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-02 23:18:00
@LastEditors: Kin P. Lam
@LastEditTime: 2020-01-02 23:31:21
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/21 0:07


import re
import datetime
from conf import config
from models import *
from flask import request


def tof(obj):
    if obj in ['1', True, 'enable', 1, 'True','true','Enable']:
        return True
    else:
        return False


def get_setting(key):
    if config.SETTING == {}:
        setting_query = Setting.query.all()
        for s in setting_query:
            config.SETTING[s.key] = s.value
    return config.SETTING.get(key, None)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(config.ALLOW_EXT)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def int_f(o:object, default:int):
    try:
        return int(o)
    except:
        return default