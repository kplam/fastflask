#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/23 22:14



from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from models.database import db
from models import *
from app import app

"""
python3 manager.py db init
python3 manager.pu db migrate
python3 manager.py db upgrade
"""

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()