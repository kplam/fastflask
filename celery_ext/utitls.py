#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@LastEditors: Kin P. Lam
@Date: 2019-04-12 23:40:50
@LastEditTime: 2019-04-13 19:50:39
'''


from .base import cly
import time


@cly.task
def notification():
	result = {"mail": None, "sms": None, "wx": None}
	try:
		send_mail()
		result['mail'] = True

	except Exception as e:
		result['mail'] = str(e)

	try:
		send_wx()
		result['wx'] = True

	except Exception as e:
		result['wx'] = str(e)

	try:
		send_sms()
		result['sms'] = True

	except Exception as e:
		result['sms'] = str(e)
		
	return result
	
			

def send_mail():
	pass

def send_sms():
	pass

def send_wx():
	pass 