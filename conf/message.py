#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2018/12/12 19:14

"""
 1： 成功
-1： 未登录
 500： 未知错误
 404:  无相关数据
 8:  请求体格式出错
 7： 帐号密码等等，请求参数不正确
 6： SQL错误
 5： 权限错误
 4： 重复数据
 99： 存在相关数据
 0： 其他错误
"""

M = {
    'welcome': {'status': 1, 'msg': 'Welcome!'},
    'success': {'status': 1, 'msg': 'Succeed!'},
    'tokenexp': {'status': -1, 'msg': 'Token Expired！'},
    'tokenerr': {'status': -1, 'msg': 'Error Token!'},
    'login_require': {'status': -1, 'msg': 'Login first!'},
    'unknown': {'status': 500, 'msg': 'Unkonwn Error!'},
    'badargs': {'status': 8, 'msg': 'Bad args format!'},
    'badrequest': {'status': 8, 'msg': 'Bad request format!'},
    'errargs': {'status': 7, 'msg': 'Parameter error!'},
    'errext': {'status': 7, 'msg': 'Unsupported file types!'},
    'needargs': {'status': 7, 'msg': 'Required parameter missing!'},
    'duplicate': {'status': 4, 'msg': 'Duplicate key fields!'},
    'needtoken': {'status': -1, 'msg': 'Token Needed!'},
    '404': {'status': 404, 'msg': '404 Not Found!'},
    'loginerr': {'status': 7, 'msg': 'Incorrect username or password!'},
    'sqlerror': {'status': 6, 'msg': 'SQL query execute error!'},
    'nopermit': {'status': 5, 'msg': 'Permission denied!'},
    'failed': {'status': 0, 'msg': 'Request failed!'},
    'diffpsw': {'status': 7, 'msg': 'The two passwords you entered did not match!'},
    'existuser': {'status': 4, 'msg': 'User already exists!'},
    'delban': {'status': 5, 'msg': 'Delete forbidden!'},
    'delban02': {'status': 5, 'msg': 'Relevant data exist, not allowed to be deleted!'},
    'configerror': {'status': 9, 'msg': 'config error!'},
}
