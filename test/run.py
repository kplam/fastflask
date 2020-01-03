#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2019-11-19 13:35:18
@LastEditors  : Kin P. Lam
@LastEditTime : 2019-12-20 16:47:33
'''

import requests as r
from src.test import test_list
from config import *
import logging
import datetime
import os


filepath = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.csv'
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(filepath, encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('"%(asctime)s","%(levelname)s",%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")


class ApiFunctinTest:
    def __init__(self,account,password,base_url,login_url,test_list):
        self.account = account
        self.password = password
        # self.access_token = None
        self.base_url = base_url
        self.login_url = login_url
        self.test_list = test_list
        self.headers = {'Content-Type':'application/json'}
        self.s = self._init_session()
        self.result = []

    def _init_session(self):
        try:
            print('正在尝试登录...')            
            j = r.post(self.base_url+self.login_url,json={'account':self.account,'password':self.password},headers=self.headers)
        except:
            print('网络错误, 任意键退出！')
            os.system('pause')
            logger.error('"%s","%s"'%(login_url,'Login Connection Error!'))
            exit()
        if j.status_code!=200:
            print('登录失败, 任意键退出！')
            os.system('pause')
            logger.error('"%s","%s"'%(login_url,'Login Status Code Error!'))
            exit()
        if j.json().get('status') == 1:
            print('成功获取AccessToken,正在更新请求头...')
            self.headers.update({'access_token':j.json()['data'].get('access_token')})
            logger.info('"%s","%s"'%(login_url,j.json()['msg']))
        else:
            print('错误：%s, 任意键退出！'% j.json().get('msg'))
            os.system('pause')
            logger.error('"%s","%s"'%(login_url,j.json().get('msg')))
            exit()
        s = r.session()
        s.headers.update(self.headers)
        return s

    def single_test(self,url,data):
        try:
            j = self.s.post(self.base_url+url,json=data)
        except:
            print('网络连接错误！')
            logger.error('"%s","%s"'%(url,'Connection Error!'))
        if j.status_code != 200:
            print('status code error: '+str(j.status_code))
            logger.error('"%s","%s"'%(url,'status code error: '+str(j.status_code)))
        else:
            try:
                if j.json().get('status') == 1:
                    logger.info('"%s","%s"'%(url,j.json().get('data')))
                else:
                    print(j.json().get('msg'))
                    logger.info('"%s","%s"'%(url,j.json().get('msg')))
            except Exception as e:
                print(e)
                logger.warning('"%s","%s"'%(url,e))


    def multi_test(self,test_list=None):
        if test_list == None:
            test_list = self.test_list
        print('当前测试请求总数：%i'%len(test_list))    
        for i, t in enumerate(test_list):
            print('%i / %i url:%s'%(i+1, len(test_list), t['url']))
            self.single_test(**t)
        print('测试完成，任意键退出...')
        os.system('pause')

class ServerStressTest:
    def __init__(self):
        pass

if __name__ == '__main__':
    aft = ApiFunctinTest(account=account,password=password,base_url=base_url,login_url=login_url,test_list=test_list)
    # apitest.single_test(url='/api/income/c',data={'amount':"200","date":"2019-01-01 20:20:20","items":"5654","messrs":"1216","received":False,"remarks":"asd","vessel_id":14})
    aft.multi_test()
