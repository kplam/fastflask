#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-03 01:22:41
'''


from .database import *
from .user import *
from .setting import *
from .sample import *
from conf import config


models_dict = {
    'setting' : Setting,
    'user': User,
    'user_group': UserGroup,
    'auth': Auth,
    'login_record': LoginRecord,
    'mod': Mod
}