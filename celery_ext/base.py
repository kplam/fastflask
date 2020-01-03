#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors: Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime: 2019-05-14 00:13:46
'''


from flask_celery import Celery
from conf import config

cly = Celery()