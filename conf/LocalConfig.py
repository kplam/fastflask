#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-03-21 04:00:06
@LastEditTime : 2020-01-03 01:34:12
'''


import os
import sys

ENV = 'development'
DEBUG = True
SECRET_KEY = '1'
BASE_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
# BASE_PATH = 'F:\coding\gz\lolita\src'

SQL_USER = 'root'
SQL_PSW = '1'
SQL_SERVER = '127.0.0.1'
SQL_DB = 'sfa'
SQL_PORT = 3306

REDIS_SERVER = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PWD = None

CELERY_REDIS_BROKER_DB = 2
CELERY_REDIS_BACKEND_DB = 3 