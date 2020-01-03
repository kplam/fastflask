<!--
 * @Author: Kin P. Lam
 * @Date: 2019-11-20 22:54:33
 * @LastEditors: Kin P. Lam
 * @LastEditTime: 2019-12-05 14:57:42
 -->

# API Test

这是一个针对flask api后端的测试.

## 环境配置

    python 3
    pip3 install requests

## 接口配置

config.py sample

    base_url = 'http://127.0.0.1:5000'
    login_url = '/api/login'
    account = 'admin'
    password = '123654'

test.py sample

    test_list=[
        {'url':'/api/vessel/c', 'data':{"id":1,"vessel_name":"test_name"}},
    ]

将以下代码粘贴于flask app.run()前，快速获取test_list

    if app.config.get('ENV') != 'production':
        with app.app_context():
            if not os.path.exists(os.path.join(config.BASE_PATH, 'test')):
                os.mkdir('test')
            with open('./test/test.py','w', encoding='utf8') as f:
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
    
## 执行

    python3 app.py

## 结果

运行完毕后在当前目录生成执行时间命名的csv文件

    datetime，level，url，result
    "2019-11-20 22:49:34,732","ERROR","/api/login","Login Connection Error！"
    "2019-11-20 22:49:34,732","INFO","/api/vessel/c","缺少必要参数!"

## TODO

    1. 模块化接入flask
    2. 增加压测功能