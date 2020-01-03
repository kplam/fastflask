#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-04 00:37:03
@LastEditors  : Kin P. Lam
@LastEditTime : 2020-01-04 00:37:37
'''

from flask import Blueprint

www_bp = Blueprint('www_bp', __name__, template_folder='templates', url_prefix='')

import api.views