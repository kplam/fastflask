#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors  : Kin P. Lam
@Date: 2019-04-17 00:17:05
@LastEditTime : 2020-01-04 00:15:11
'''


from flask import g, make_response, send_file, jsonify, request
from api import api_bp
from libs.auth import login_require 
from conf.message import M
from copy import deepcopy
from sqlalchemy import or_
from sqlalchemy.orm.collections import InstrumentedList
from models import *





@api_bp.route('/login', methods=['POST'])
def login():
    if 'account' in g.args and 'password' in g.args:
        # TODO
        pass
    else:
        return jsonify(M['needargs'])


"""
the base CRUD functions below

<model> is the keyword for models setting in models.__init__

models_dict = {
    'setting' : Setting,
    'user': User,
    'user_group': UserGroup,
    'auth': Auth,
    'login_record': LoginRecord,
    'mod': Mod
}


"""

@api_bp.route('/<model>', methods=['POST'])
@login_require
def model_read(model):
    if model not in models_dict:
        return jsonify(M['404'])
    mod = models_dict[model]
    filter_list = []
    for k, v in g.args.items():
        logist = k.spilt('_')
        if len(logist) == 1: 
            filter_list.append(mod.__table__.c[k] == v)
        elif len(logist) > 1:
            if logist[-1] in ['gt', 'ge', 'lt', 'eq', 'le', 'ne', 'lk']:
                cal = logist[-1]
                field ='_'.join(logist[:-1])
                if cal == 'gt':
                    filter_list.append(mod.__table__.c[field] > v)
                elif cal == 'ge':
                    filter_list.append(mod.__table__.c[field] >= v)
                elif cal == 'lt':
                    filter_list.append(mod.__table__.c[field] < v)
                elif cal == 'eq':
                    filter_list.append(mod.__table__.c[field] == v)
                elif cal == 'le':
                    filter_list.append(mod.__table__.c[field] <= v)
                elif cal == 'ne':
                    filter_list.append(mod.__table__.c[field] != v)
                elif cal == 'lk':
                    filter_list.append(mod.__table__.c[field].like('%'+str(v)+'%'))
        
    query = mod.query.filter(*filter_list).all()
    result = deepcopy(M['success'])
    result['data'] = [row.to_dict() for row in query]
    return jsonify(result)


@api_bp.route('/api/<model>/c', methods=['POST'])
@login_require
def mod_create(model):
    if model not in models_dict:
        return jsonify(M['404'])
    mod = models_dict[model]
    if 'id' in g.args:
        del g.args['id']
    b, result, keys, args = check_model_args(mod, g.args)
    if b:
        new = mod(**args)
        if 'lasteditor' in keys:
            new.lasteditor = g.user['id']
        if 'lastupdate' in keys:
            new.lastupdate = datetime.datetime.now()
        db.session.add(new)
        db.session.commit()
        d = new.to_dict()
        result['data'] = [d]
        return jsonify(result)
    else:
        return jsonify(result)



@api_bp.route('/api/<model>/u', methods=['POST'])
@login_require
def mod_update(model):
    if 'id' not in g.args:
        return jsonify(M['needargs'])
    if model not in models_dict:
        return jsonify(M['404'])
    mod = models_dict[model]
    update = mod.query.filter(mod.id == g.args['id']).first()
    if not update:
        return jsonify(M['404'])

    del g.args['id']
    b, result, keys, args = check_model_args(update, g.args)
    if b:
        for k, v in args.items():
            update.__setattr__(k, v)
        if 'lasteditor' in keys:
            update.lasteditor = g.user['id']
        if 'lastupdate' in keys:
            update.lastupdate = datetime.datetime.now()
        db.session.add(update)
        db.session.commit()
        d = update.to_dict()
        result['data'] = [d]
        return jsonify(result)
    else:
        return jsonify(result)


@api_bp.route('/api/<model>/d', methods=['POST'])
@login_require
def mod_delete(model):
    if 'id' not in g.args:
        return jsonify(M['needargs'])
    if model not in models_dict:
        return jsonify(M['404'])
    mod = models_dict[model]
    check = mod.query.filter(mod.id == g.args['id']).first()
    if not check:
        return jsonify(M['404'])

    col = [c.name for c in check.__table__.c]
    for k in dir(check):
        if k not in col and k[:1]!='_':
            r = check.__getattribute__(k)
            if isinstance(r,InstrumentedList):
                for r0 in r:
                    db.session.delete(r0)
                db.session.commit()
    db.session.delete(check)
    db.session.commit()
    return jsonify(M['success'])