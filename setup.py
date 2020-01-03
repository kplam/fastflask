#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2019-12-08 01:49:19
@LastEditors  : Kin P. Lam
@LastEditTime : 2019-12-20 16:16:50
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/11/6 0006 下午 15:11


from flask import Flask
from conf import config
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
import getpass
import os
import importlib
from exts import create_app
import setup_config
import sqlalchemy

app = create_app(config)

e = sqlalchemy.create_engine('mysql+pymysql://{}:{}@{}:{}'.format(config.SQL_USER, config.SQL_PSW, config.SQL_SERVER, config.SQL_PORT))
e.execute("DROP DATABASE IF EXISTS `%s`"%config.SQL_DB)
e.execute("CREATE DATABASE `%s`;"%config.SQL_DB) #create db

db.init_app(app)


def system_init(acc='admin', pwd='123654'):
    # db.engine.execute("ALTER TABLE `user_group` CHANGE `id` `id` INT (11) NOT NULL AUTO_INCREMENT;")


    for k, v in setup_config.__dict__.items():
        if not k.startswith('__'):
            mod = models_dict.get(k,None)
            if mod is not None:
                if isinstance(v,dict):
                    db.session.add(mod(**v))
                    db.session.commit()
                elif isinstance(v, list):
                    for i in v:
                        db.session.add(mod(**i))
                    db.session.commit()


    for k in set([url.endpoint for url in app.url_map.__dict__['_rules']]):
        if k != 'static':
            db.session.add(Auth(group='admin', key=k, value=True, remark=k.replace('_bp.', ' ').replace('_', ' ')))

    db.session.commit()
    # for auth in auth_list:
    #     db.session.add(Auth(**auth))
    # db.session.commit()


    db.session.add(User(id=1, account=acc, name='Administartor', group='admin',
                        password=generate_password_hash(acc + pwd, method='pbkdf2:sha256', salt_length=32),
                        status=True))
    db.session.commit()


if __name__ == '__main__':
    print('Preparing Initialization\n\r' + '=' * 32)
    account = input('Please enter the administrator account:\n\r')
    password = getpass.getpass("Please input your password:")
    confirm = getpass.getpass("Please input your password again:")
    # tel = input('Please enter the administrator telphone number:\n\r')

    while password != confirm or password == '' or len(password) < 6:
        if password == '':
            print('The code can not be empty!')
        elif len(password) < 6:
            print('The code you entered must be a minimum of 6 characters long!')
        elif password != confirm:
            print('The code you entered twice must be the same.')
        password = getpass.getpass("Please input your password:")
        confirm = getpass.getpass("Please input your password again:")

    print('=' * 32 + '\n\rDatabase Initializing...\n\r' + '=' * 32)

    with app.app_context():
        # try:
            print(
                'Initializing tables...\n\rif tables are already existed, please run the following commands to upgrade your datebase!\n\r   1. $> python3 manager.py db init\n\r   2. $> python3 manager.py db migrate\n\r   3. $> python3 manager.py db upgrade')
            db.create_all()
            # print(r.fetchall())
            print('Checking records...')
            if User.query.filter(User.id == 1).first():
                raise Exception(
                    'Administrator account is already existed!\n\rPlease check your database and config file!')
            if Setting.query.all():
                raise Exception('System setting is already existed!\n\rPlease check your database and config file!')

            print('Writing data...')
            system_init(acc=account, pwd=password)
            print(
                '=' * 32 + '\n\rSystem init done!\n\r' + '=' * 32 + '\n\rAdmin Account: %s\n\rPassword: %s\n\rPlease login and change your password immediately!' % (
                account, '*' * len(password)))

        # except Exception as e:
        #     print('*' * 32 + '\n\rSystem init failed!\n\r' + '*' * 32 + '\n\r' + str(e))
