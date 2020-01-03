#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors: Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime: 2019-12-08 01:56:34
'''


import jwt
import json
from functools import wraps
from flask import jsonify, g, request
from conf.message import M
from sqlalchemy.exc import SQLAlchemyError
from conf import config
from models import *
from redis_ext import try_login_times
try:
    from .func import *
except ImportError:
    from libs.func import *


def login_require(function):
    """
    JWT 登录校验（装饰器）
    :param function: 原请求函数
    :return: 校验成功返咽原函数，失败返回access_token错误信息，连续四次解密失败将禁止当前ip请求10分钟。
    """
    @wraps(function)
    def login(*args, **kwargs):
        if str(request.endpoint)[:3] == 'www':
            if not request.headers.get('access_token') and session.get('group') is None:
                return redirect(url_for('www_bp.login'))
            if request.headers.get('access_token'):
                access_token = request.headers.get('access_token')
                try:
                    payload = jwt.decode(access_token, config.SECRET_KEY, algorithm='HS256')
                    g.user = payload['payload']
                    if g.user['ip'] != request.remote_addr:
                        return redirect(url_for('www_bp.login'))
                    if not auth_check(key=str(request.endpoint)):
                        return redirect(url_for('www_bp.nopermit'))
                    return function(*args, **kwargs)
                except jwt.ExpiredSignatureError:
                    return redirect(url_for('www_bp.login'))
                except jwt.InvalidSignatureError:
                    return redirect(url_for('www_bp.login'))
                except:
                    return redirect(url_for('www_bp.ise500'))
            elif session.get('group'):
                try:
                    g.user = session
                    if g.user['ip'] != request.remote_addr:
                            return redirect(url_for('www_bp.login'))
                    if not auth_check(key=str(request.endpoint)):
                        return  redirect(url_for('www_bp.nopermit'))
                    return function(*args, **kwargs)
                except:
                    return redirect(url_for('www_bp.ise500'))
            else:
                return redirect(url_for('www_bp.login'))
        else:
            if request.mimetype != 'application/json' and '.upload' not in str(request.endpoint):
                return jsonify(M['badrequest'])

            if '.upload' not in str(request.endpoint):
                try:
                    g.args = json.loads(request.get_data())
                except json.JSONDecodeError:
                    return jsonify(M['badargs'])
            else:
                g.args = request.args.to_dict()
            if 'login' in str(request.endpoint):
                return jsonify(M['badrequest'])
            else:
                if not request.headers.get('access_token'):

                    return jsonify(M['needtoken'])
                access_token = request.headers.get('access_token')
                try:
                    payload = jwt.decode(access_token, config.SECRET_KEY, algorithm='HS256')
                    g.user = payload['payload']
                    if g.user['ip'] != request.remote_addr:
                        return jsonify(M['tokenerr'])
                    if not auth_check(key=str(request.endpoint)):
                        return jsonify(M['nopermit'])
                    return function(*args, **kwargs)
                except jwt.ExpiredSignatureError:
                    # try_login_times()
                    return jsonify(M['tokenexp'])
                except jwt.InvalidSignatureError:
                    # try_login_times()
                    return jsonify(M['tokenerr'])
                except SQLAlchemyError:
                    return jsonify(M['sqlerror'])
                except Exception:
                    return jsonify(M['unknown'])
    return login


def auth_check(key=None, mode='check'):
    """
    读入权限信息至内存，根据用户登录所在组别（login_require > g.user）和key字段参数确定用户是否有权限进行对应操作
    :param key: 数据库auth.key字段值
    :param mode: check / set
    :return: True or False
    """
    if config.SYSTEM_AUTH == {} or mode == 'set':
        config.SYSTEM_AUTH = {}
        user_auth = Auth.query.all()
        for ua in user_auth:
            if ua.group not in config.SYSTEM_AUTH:
                config.SYSTEM_AUTH[ua.group] = {}
            config.SYSTEM_AUTH[ua.group][ua.key] = ua.value
    if mode == 'check':
        try:
            if key is None:
                key = request.endpoint
            if config.SYSTEM_AUTH[g.user['group']].get(key, None):
                return True
            else:
                return False
        except:
            return False
    else:
        return False


# def try_login_times():
#     """
#     登录失败计次
#     :return:
#     """
#     if R is not None:
#         if R.exists('BAN_IP:' + str(request.remote_addr)):
#             R.incr('BAN_IP:' + str(request.remote_addr), 1)
#             R.expire('BAN_IP:' + str(request.remote_addr), 60 * int(get_setting('ban_ip_time')))
#         else:
#             R.set('BAN_IP:' + str(request.remote_addr), 1)
#     else:
#         if config.BAN_IP.get(str(request.remote_addr)):
#             config.BAN_IP[str(request.remote_addr)]['times'] += 1
#             config.BAN_IP[str(request.remote_addr)]['expire'] = datetime.dateime.now() + datetime.timedelta(minutes=int(get_setting('ban_ip_time')))
#         else:
#             config.BAN_IP[str(request.remote_addr)]={'times':1,'expire':datetime.dateime.now() + datetime.timedelta(minutes=int(get_setting('ban_ip_time')))}
            
# def ban_check():
#     """
#     连续多次错误密码或用户名后禁止登录。
#     """
#     if R is not None:
#         times = R.get('BAN_IP:' + str(request.remote_addr))
#         if times is not None:
#             if int(times) >= int(get_setting('ban_ip_times')):
#                 return True
#             else:
#                 return False
#         return False
#     else:
#         ip = config.BAN_IP.get(str(request.remote_addr))
#         if ip is None:
#             return False
#         else:
#             if ip['times'] >= int(get_setting('ban_ip_times')):
#                 if ip['expire'] < datetime.datetime.now():
#                     return True
#                 else:
#                     return False
#             else:
#                 return False