#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-13 00:52:20
@LastEditTime : 2020-01-03 03:26:52
'''

"""
change import for diff env 
"""
try:
    from .LocalConfig import *
    # from .ProductionConfig import *
    # from .TestServerConfig import *
except ImportError:
    from conf.LocalConfig import *
    # from conf.ProductionConfig import *
    # from conf.TestServerConfig import *


# base flask config
THREADED = True
JSON_AS_ASCII = False
JSONIFY_PRETTYPRINT_REGULAR = False
MAX_CONTENT_LENGTH = 40 * 1024 * 1024
ALLOW_EXT = ['jpg', 'jpeg', 'png', 'bmp', 'gif']
ADMIN_PREFIX  = '/admin'

# SQL Server
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_RECYCLE = 1600
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(SQL_USER, SQL_PSW, SQL_SERVER, SQL_PORT, SQL_DB)
SQLALCHEMY_DATABASE_URI = DB_URI

# redis config
REDIS_URL= 'redis://{}:{}/{}'.format(REDIS_SERVER,REDIS_PORT,REDIS_DB) if REDIS_PWD is None else 'redis://:{}@{}:{}/{}'.format(REDIS_PWD,REDIS_SERVER,REDIS_PORT,REDIS_DB)

# 内存常驻变量
SYSTEM_AUTH = {}
SETTING = {}

# apscheduler
SCHEDULER_API_ENABLE = True
JOBS = []

# celery config
CELERY_BROKER_URL = 'redis://{}:{}/{}'.format(REDIS_SERVER,REDIS_PORT,CELERY_REDIS_BROKER_DB) if REDIS_PWD is None else 'redis://:{}@{}:{}/{}'.format(REDIS_PWD,REDIS_SERVER,REDIS_PORT,CELERY_REDIS_BROKER_DB)
CELERY_RESULT_BACKEND = 'redis://{}:{}/{}'.format(REDIS_SERVER,REDIS_PORT,CELERY_REDIS_BACKEND_DB) if REDIS_PWD is None else 'redis://:{}@{}:{}/{}'.format(REDIS_PWD,REDIS_SERVER,REDIS_PORT,CELERY_REDIS_BACKEND_DB)
CELERY_TIMEZONE = 'Asia/Shanghai'

