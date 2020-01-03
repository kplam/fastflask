#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/21 0:16

try:
    from connect import R
except ImportError:
    from .connect import R
from flask import request
from libs.func import get_setting


def try_login_times():
    """
    登录失败计次
    :return:
    """
    if R.exists('BAN_IP:' + str(request.remote_addr)):
        R.incr('BAN_IP:' + str(request.remote_addr), 1)
        R.expire('BAN_IP:' + str(request.remote_addr), 60 * int(get_setting('ban_ip_time')))
    else:
        R.set('BAN_IP:' + str(request.remote_addr), 1)


def ban_check():
    """
    连续多次错误密码或用户名后禁止登录。
    """
    times = R.get('BAN_IP:' + str(request.remote_addr))
    if times is not None:
        if int(times) >= int(get_setting('ban_ip_times')):
            return True
        else:
            return False
    return False