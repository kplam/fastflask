#!/usr/bin/python3
# -*- coding: utf-8 -*-


test_list = [
    {'url': '/static/<path:filename>', 'data': {}},
    {'url': '/admin/setting', 'data': {}},
    {'url': '/admin/upload_auth', 'data': {}},
    {'url': '/api/login', 'data': {}},
    {'url': '/api/social_login', 'data': {}},
    {'url': '/api/<model>/c', 'data': {}},
    {'url': '/api/<model>/u', 'data': {}},
    {'url': '/api/<model>/d', 'data': {}},
    {'url': '/admin/sch/get_jobs', 'data': {}},
    {'url': '/admin/sch/remove_jobs', 'data': {}},
    {'url': '/admin/sch/resume_jobs', 'data': {}},
    {'url': '/admin/sch/pause_jobs', 'data': {}},
    {'url': '/admin/sch/add_jobs', 'data': {}},
    {'url': '/admin/token', 'data': {}},
    {'url': '/admin/user/c', 'data': {'id': 1, 'account': 'admin', 'name': 'Administartor', 'group': 'admin', 'status': True}},
    {'url': '/admin/user/r', 'data': {'id': 1, 'account': 'admin', 'name': 'Administartor', 'group': 'admin', 'status': True}},
    {'url': '/admin/user/u', 'data': {'id': 1, 'account': 'admin', 'name': 'Administartor', 'group': 'admin', 'status': True}},
    {'url': '/admin/user/d', 'data': {'id': 1, 'account': 'admin', 'name': 'Administartor', 'group': 'admin', 'status': True}},
    {'url': '/admin/usergroup/r', 'data': {}},
    {'url': '/admin/usergroup/c', 'data': {}},
    {'url': '/admin/usergroup/u', 'data': {}},
    {'url': '/admin/usergroup/d', 'data': {}},
    {'url': '/admin/auth/r', 'data': {'id': 1, 'key': 'user_bp.get_auth', 'group': 'admin', 'value': True, 'remark': 'user get auth'}},
    {'url': '/admin/auth/u', 'data': {'id': 1, 'key': 'user_bp.get_auth', 'group': 'admin', 'value': True, 'remark': 'user get auth'}},
    {'url': '/test_cly', 'data': {}},
    {'url': '/', 'data': {}},
    {'url': '/chat', 'data': {}},
    {'url': '/upload', 'data': {}},
]