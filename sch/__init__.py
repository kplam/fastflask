#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-03 02:02:07
'''


from flask import Blueprint
from flask_apscheduler import APScheduler
from flask import current_app
try:
    from .sch_jobs import *
except ImportError:
    from sch.sch_jobs import *

sch_bp = Blueprint('sch_bp', __name__, template_folder='templates', url_prefix='/api/sch')

class ContextScheduler(APScheduler):
    def get_app(self):
        if self.app:
            return self.app
        if current_app:
            return  current_app

scheduler = ContextScheduler()

import sch.views
