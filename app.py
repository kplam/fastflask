#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-03-21 03:57:24
@LastEditTime : 2020-01-03 02:55:59
'''

import gevent
from gevent import monkey; monkey.patch_all()
import os
import sys
import atexit
import platform
from conf import config
from exts import create_app
from models import *
from flask import request, g

app = create_app(config)

if os.path.exists(os.path.join(config.BASE_PATH, 'sch')):

    from sch.sch_jobs import *

    def scheduler_init(app):
        if config.ENV == 'production':        
            config.JOBS.append(
                    # append apscheduler Jobs here
                    { 
                        'id': 'pop_auto',
                        'func': hello_world,
                        'args': None,
                        'trigger': 'interval',
                        'replace_existing':True,
                        'max_instances': 4,
                        'seconds': 1*60
                    }
                )

        sysstr = platform.system()
        if sysstr == "Linux" :
            import fcntl
            f = open("scheduler.lock", "wb")
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                scheduler.init_app(app)
                scheduler.start()
            except:
                pass
            def unlock():
                fcntl.flock(f, fcntl.LOCK_UN)
                f.close()
            atexit.register(unlock)
        else:
            try:
                if R.get('scheduler.lock') != '1':
                    
                    scheduler.init_app(app)
                    scheduler.start()
                    R.set('scheduler.lock','1')
            except:
                pass
            def unlock():
                R.set('scheduler.lock','0')
            atexit.register(unlock)
  
    scheduler_init(app)


@app.after_request
def save_operation_record(response):
    """
    save create, update ,delete record to database table 'operation_record'

    To save operation record please use [create, update, delete, edit] in request function's name
    """
    try:
        if 'create' in request.endpoint or 'update' in request.endpoint or 'delete' in request.endpoint or 'edit' in request.endpoint:
            rj = response.get_json()
            if rj:
                if rj.get('status') == 1:
                    new_record = OperationRecord(user_id=g.user['id'], endpoint=request.endpoint, url=request.path, args=json.dumps(g.args))
                    db.session.add(new_record)
                    db.session.commit()
    finally:
        return response
        

if __name__ == '__main__':

    # if os.path.exists(os.path.join(config.BASE_PATH,'setup.pyc')) or os.path.exists(os.path.join(config.BASE_PATH,'setup.py')):
    #     from setup import system_init

    #     with app.app_context():
    #         try:
    #             db.create_all()
    #             # db.engine.execute("ALTER TABLE `usergroup` CHANGE `id` `id` INT (11) NOT NULL AUTO_INCREMENT;")

    #             if not Setting.query.all():
    #                 system_init()
    #             if os.path.exists(os.path.join(config.BASE_PATH,'setup.pyc')):
    #                 os.unlink('setup.pyc')
    #             # if os.path.exists(os.path.join(config.BASE_PATH,'setup.py')):
    #             #     os.unlink('setup.py')
    #         except Exception as e:
    #             print('System init failed! Reason: %s' % str(e))
                
    with app.app_context():
        if config.ENV == 'test':
            if not os.path.exists(os.path.join(config.BASE_PATH, 'test')):
                os.mkdir(os.path.join(config.BASE_PATH, 'test'))
            with open(os.path.join(config.BASE_PATH[:-3], 'test/test.py'),'w', encoding='utf8') as f:
                f.writelines('#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n\n')
                f.writelines('test_list = [\n')
                for url in app.url_map.__dict__['_rules']:
                    # map_dict[url.__dict__['rule']] = url.__dict__['methods']
                    u = url.__dict__['rule']
                    d = {'url':u,'data':{}}
                    if len(u.split('/'))>3:
                        m = models_dict.get(u.split('/')[2])
                    else:
                        m = None
                    if m is not None:
                        dm = m.query.first()
                        if dm:
                            d['data'] = dm.to_dict()
                    f.writelines('    %s,\n' % d)
                f.writelines(']')

    app.run(port=5000, host='0.0.0.0', threaded=True)
