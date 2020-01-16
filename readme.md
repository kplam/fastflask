<!--
 * @Author: Kin P. Lam
 * @Date: 2020-01-02 23:18:27
 * @LastEditors  : Kin P. Lam
 * @LastEditTime : 2020-01-17 00:39:29
 -->

# Simple flask crud api

## 简单介绍

1. 无需逐一编写各个数据表的CRUD接口，只需在models里声明好业务逻辑数据表即可

2. 集成用户分组、权限控制，使用JWT作为用户验证, 统一通过request请求头access-token判定

3. 集成redis、celery、apscheduler，用于处理异步、定时任务

4. blueprint自动注册，在定义blueprint时使用 **文件夹名_bp** 即可

5. 配备**setup.py**和**setup_config.py**用于初始化数据库

6. 自动化接口测试

7. manager.py快速更新数据库结构

## 环境

    python 3.7
    mysql 8
    redis 5

## 配置

1. 在 __.models/sample.py__ 声明数据表, 并将数据表添加至 __.models.\_\_init\_\_.py.models_dict__
2. 在 __.conf.ProductionConfig.py__ 配置好数据库等设置, 然后在 __.conf.config.py__ 将导入localconfig改成导入productionconfig

## 运行

    pip3 install -r requirements.txt
    python3 setup.py
    gunicorn --chdir /app -k gevent -t 90 -b 0.0.0.0:5000 app:app

## API

1. create 新建数据

    #### ** model 为表名， field 为字段名， value为字段值（支持JSON）

        url: http://domain.name/api/<model>/c
        login require : True
        method: post
        minetype: application/json
        data: {"field1": "value1","field2": "value2",...}
        return: {
             "data": [{
                 "id":1,
                 "field1": "value1",
                 "field2": "value2",
                 ...
             }],
             "msg": "succeed!",
             "status": 1
        }

2. read 读取数据

    #### ** model为表名， field为字段名，字段名后可以用下划线'_' + lt等比较字符，例如{"field_gt"： 1}表示字段field>1。字符用法如下： lt: <,  le: <=, gt: >, ge： >=, eq: =, ne: !=, lk: like

        url: http://domain.name/api/<model>
        login require : True
        method: post
        minetype: application/json
        data: {"field1": "value1","field2_ge": "value2",...}
        return: {
             "data": [{
                 "id":1,
                 "field1": "value1",
                 "field2": "value2",
                 ...
             }],
             "msg": "succeed!",
             "status": 1
        }

3. update 更新数据

    #### ** model 为表名， field 为字段名， value为字段值（支持JSON），id为必要字段，其他字段为可选

        url: http://domain.name/api/<model>/u
        login require : True
        method: post
        minetype: application/json
        data: {"id":1, "field1": "value1","field2": "value2",...}
        return: {
             "data": [{
                 "id":1,
                 "field1": "value1",
                 "field2": "value2",
                 ...
             }],
             "msg": "succeed!",
             "status": 1
         }

4. delete 删除数据

    #### ** model 为表名，id为必要字段

        url: http://domain.name/api/<model>/d
        login require : True
        method: post
        minetype: application/json
        data: {"id":1}
        return: {
             "msg": "succeed!",
             "status": 1
        }

## TODO
1. 修正系统用户分组权限的问题
2. 增加压力测力模块
