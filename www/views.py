#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-04 00:37:14
@LastEditors  : Kin P. Lam
@LastEditTime : 2020-01-04 00:39:07
'''

from www import www_bp
from flask import render_template

@www_bp.route()
def index():
    return render_template('index.html')