#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-13 18:37:24
@LastEditTime : 2020-01-03 01:33:21
'''
 

ENV = 'test'
DEBUG = True
SECRET_KEY = '1234'
BASE_PATH = '/data/app'

SQL_USER = 'root'
SQL_PSW = '1'
SQL_SERVER = '192.168.1.2'
SQL_DB = 'sfa'
SQL_PORT = 3306

REDIS_SERVER = '192.168.1.2'
REDIS_PORT = 6379
REDIS_DB = 2
REDIS_PWD = None

CELERY_REDIS_BROKER_DB = 2
CELERY_REDIS_BACKEND_DB = 3