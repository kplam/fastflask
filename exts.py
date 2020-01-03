#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-03-21 03:57:24
@LastEditTime : 2020-01-02 23:24:03
'''


import os
import importlib
from flask import Flask
from models.database import db
from flask_cors import CORS
try:
    from werkzeug.middleware.proxy_fix import ProxyFix
except ImportError:
    from werkzeug.contrib.fixers import ProxyFix



def create_app(conf):
    # set app config
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(conf)
    # ApiDoc(app)
    # auto register blueprint
    services = []
    pathlist = os.listdir(conf.BASE_PATH)

    for path in pathlist:
        if os.path.isdir(os.path.join(conf.BASE_PATH , path)):
            subpath_list = os.listdir(os.path.join(conf.BASE_PATH , path))
            if 'views.pyc' in subpath_list or 'views.py' in subpath_list:
                services.append({'package': path, 'blueprint': path + '_bp'})
                print('BLUEPRINT: [%s] loading completed !'%(path))

    for service in services:
        module = importlib.import_module('.views', package=service['package'])
        app.register_blueprint(getattr(module, service['blueprint']))

    # init sqlalchemy
    db.init_app(app)

    # init flask-redis
    if os.path.exists(os.path.join(conf.BASE_PATH , 'redis_ext')):
        
        from redis_ext import R

        R.init_app(app)
        print('REDIS: Init done!')
    else:
        print('REDIS: Init failed!')

    if os.path.exists(os.path.join(conf.BASE_PATH,'celery_ext')):
        from celery_ext import cly

        cly.init_app(app)
        cly.conf.update(app.config)
        print('CELERY: Init done!')
    else:
        print('CELERY: Init failed!')

    # if os.path.exists(os.path.join(conf.BASE_PATH, 'sch')):
    #     from sch import scheduler
    #     config.JOBS.append({
    #                         'id': 'createschuler_job',
    #                         'func': hello_world,
    #                         'args': None,
    #                         'trigger': 'interval',
    #                         'seconds': 5})
    #     scheduler.init_app(app)


    # fix nginx proxy
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Cross domain request allowed  
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app

