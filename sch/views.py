#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2018/12/12 20:01


from flask import g, make_response, send_file, jsonify
from sch import *
from libs.auth import login_require
from copy import deepcopy
from conf.message import M



@sch_bp.route('/get_jobs', methods=['GET'])
@login_require
def get_sch_jobs():
    joblist = scheduler.get_jobs()
    result = deepcopy(M['success'])
    result['data'] = [{'id':job.id,'name':job.name, 'next_run_time':job.next_run_time} for job in joblist]
   
    return jsonify(result)


@sch_bp.route('/remove_jobs', methods=['POST'])
@login_require
def remove_sch_jobs():
    result = deepcopy(M['success'])
    for job in g.args:
        if job.get('id'):
            try:
                scheduler.remove_job(job.get('id'))
            except Exception as e:
                if result.get('error') is None:
                    result['error'] = [str(e)]
                else:
                    result['error'].append(str(e))
        else:
            if result.get('error') is None:
                    result['error'] = ['job id is none!']
            else:
                result['error'].append('job id is none!')

    joblist = scheduler.get_jobs()
    
    result['data'] = [{'id':job.id,'name':job.name, 'next_run_time':job.next_run_time} for job in joblist]
    return jsonify(result)



@sch_bp.route('/resume_jobs', methods=['POST'])
@login_require
def resume_sch_jobs():
    
    result = deepcopy(M['success'])
    for job in g.args:
        if job.get('id'):
            try:
                scheduler.resume_job(job.get('id'))
            except Exception as e:
                if result.get('error') is None:
                    result['error'] = [str(e)]
                else:
                    result['error'].append(str(e))
        else:
            if result.get('error') is None:
                    result['error'] = ['job id is none!']
            else:
                result['error'].append('job id is none!')

    joblist = scheduler.get_jobs()
    
    result['data'] = [{'id':job.id,'name':job.name, 'next_run_time':job.next_run_time} for job in joblist]
    return jsonify(result)


@sch_bp.route('/pause_jobs', methods=['POST'])
@login_require
def pause_sch_jobs():
    result = deepcopy(M['success'])
    for job in g.args:
        if job.get('id'):
            try:
                scheduler.pause_job(job.get('id'))
            except Exception as e:
                if result.get('error') is None:
                    result['error'] = [str(e)]
                else:
                    result['error'].append(str(e))
        else:
            if result.get('error') is None:
                    result['error'] = ['job id is none!']
            else:
                result['error'].append('job id is none!')

    joblist = scheduler.get_jobs()
    
    result['data'] = [{'id':job.id,'name':job.name, 'next_run_time':job.next_run_time} for job in joblist]
    return jsonify(result)


@sch_bp.route('/add_jobs', methods=['POST'])
@login_require
def add_jobs():
    needed_args = ['id', 'func',]
    for k in needed_args:
        if k not in g.args:
            return jsonify(M['needargs'])
    joblist = scheduler.get_jobs()
    for job in joblist:
        if g.args['id'] == job.id:
            return jsonify(M['duplicate'])
    if scheduler_jobdict.get(g.args['func']) is None:
        return jsonify(M['404'])
    try:
        if g.args.get('trigger') == 'interval':
            if isinstance(g.args.get('interval'),dict):
                scheduler.add_job(id=g.args['id'], func=scheduler_jobdict.get(g.args['func']), args=g.args.get('args'), trigger='interval', replace_existing=True, **g.args['interval'])
            return jsonify(M['needargs'])
        elif g.args.get('trigger') == 'cron':
            if isinstance(g.args.get('cron'),dict):
                scheduler.add_job(id=g.args['id'], func=scheduler_jobdict.get(g.args['func']), args=g.args.get('args'), trigger='cron', replace_existing=True, **g.args['cron'])
            return jsonify(M['needargs'])
        elif g.args.get('trigger') is None:
            scheduler.add_job(id=g.args['id'], func=scheduler_jobdict.get(g.args['func']), args=g.args.get('args'), replace_existing=True)
        else:
            return jsonify(M['errargs'])
    except Exception as e:
        return jsonify({'status':0,'msg':str(e)})
    joblist = scheduler.get_jobs()
    result = deepcopy(M['success'])
    result['data'] = [{'id':job.id,'name':job.name, 'next_run_time':job.next_run_time} for job in joblist]
   
    return jsonify(result)