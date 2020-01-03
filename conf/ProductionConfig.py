#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-03 01:41:08
'''


import os

ENV = 'production'
DEBUG = False
SECRET_KEY = os.urandom(32)
BASE_PATH = '/data/app'

SQL_USER = 'root'
SQL_PSW = '1'
SQL_SERVER = '127.0.0.1'
SQL_DB = 'sfa'
SQL_PORT = 3306

REDIS_SERVER = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PWD = None

CELERY_REDIS_BROKER_DB = 2
CELERY_REDIS_BACKEND_DB = 3