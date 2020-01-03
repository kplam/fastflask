#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-02 23:18:00
@LastEditors  : Kin P. Lam
@LastEditTime : 2020-01-02 23:36:45
'''


from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, template_folder='templates', url_prefix='/api')

import api.views
