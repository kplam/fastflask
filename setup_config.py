#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/11/6 0006 下午 18:37

"""
Setup config
系统运行需要的最基本数据
格式：
数据表名 = [{字段名1：字段值1,字段名2：字段值2,},...]
数据表名 = {字段名1：字段值1,字段名2：字段值2,}
"""


user_group = [
    {'name': 'admin', 'remark': '超级管理员', 'authority': 999, 'status': True},

]

setting = [
    # base setting
    {'key': 'site_name', 'type': 'base', 'value': 'KPL MALL', 'remark': '网站名称'},
    {'key': 'seo_title', 'type': 'base', 'value': 'SEO默认标题', 'remark': 'SEO默认标题'},
    {'key': 'seo_meta_keyword', 'type': 'base', 'value': 'SEO默认关键字', 'remark': 'SEO默认关键字'},
    {'key': 'seo_meta_description', 'type': 'base', 'value': 'SEO默认页面描述', 'remark': 'SEO默认页面描述'},
    {'key': 'icp', 'type': 'base', 'value': '', 'remark': 'ICP备案号'},
    {'key': 'copyright', 'type': 'base', 'value': '', 'remark': '版权信息'},

    # baidu tongji api
    {'key': 'baidu_tongji_api', 'type': 'baidu', 'value': '这里填写百度统计的id', 'remark': '百度统计设置'},

    # email setting
    {'key': 'email_address', 'type': 'email', 'value': '*@*.com', 'remark': '系统通知邮箱帐号'},
    {'key': 'email_address_pwd', 'type': 'email', 'value': '*******', 'remark': '系统通知邮箱密码'},
    {'key': 'email_smtp_host', 'type': 'email', 'value': 'smtp.exmail.qq.com', 'remark': '系统通知邮箱服务器'},
    {'key': 'email_smtp_port', 'type': 'email', 'value': '465', 'remark': '系统通知邮箱端口号'},
    {'key': 'email_smtp_ssl', 'type': 'email', 'value': 'SSL', 'remark': '系统通知邮箱加密方式'},

    # qcloud sms settng
    {'key': 'sms_verification', 'type': 'sms', 'value': 'enable', 'remark': '腾讯短信通知开关'},
    {'key': 'sms_appid', 'type': 'sms', 'value': '1356654', 'remark': '腾讯短信通知appid'},
    {'key': 'sms_appkey', 'type': 'sms', 'value': 'asd4545asdsw4', 'remark': '腾讯短信通知appkey'},
    {'key': 'sms_template_code', 'type': 'sms', 'value': '143564', 'remark': '腾讯短信检证码模板'},
    {'key': 'sms_template_pay', 'type': 'sms', 'value': '143564', 'remark': '腾讯短信付款通知模板'},
    {'key': 'sms_template_reward', 'type': 'sms', 'value': '143564', 'remark': '腾讯短信积分通知模板'},

    # wechat mp
    {'key': 'wx_mp', 'type': 'wx_mp', 'value': 'enable', 'remark': '微信公众号'},
    {'key': 'wx_mp_id', 'type': 'wx_mp', 'value': '13265413', 'remark': '微信公众号app_id'},
    {'key': 'wx_mp_key', 'type': 'wx_mp', 'value': '13265413', 'remark': '微信公众号app_key'},
    {'key': 'wx_mp_template_pay', 'type': 'wx_mp', 'value': '143564', 'remark': '微信公众号付款通知模板'},
    {'key': 'wx_mp_template_reward', 'type': 'wx_mp', 'value': '143564', 'remark': '微信公众号积分通知模板'},

    # wechat merchants
    {'key': 'wx_mch', 'type': 'wxpay', 'value': 'enable', 'remark': '微信支付接口'},
    {'key': 'wx_mch_id', 'type': 'wxpay', 'value': '13265413', 'remark': '微信商户app_id'},
    {'key': 'wx_mch_key', 'type': 'wxpay', 'value': '13265413', 'remark': '微信商户app_key'},

    # alipay merchants
    {'key': 'ali_mch', 'type': 'alipay', 'value': 'enable', 'remark': '支付宝接口'},
    {'key': 'ali_mch_id', 'type': 'alipay', 'value': '13265413', 'remark': '支付宝商户app_id'},
    {'key': 'ali_mch_key', 'type': 'alipay', 'value': '13265413', 'remark': '支付宝商户app_key'},

    # paypal merchants
    {'key': 'paypal_mch', 'type': 'paypal', 'value': 'disable', 'remark': 'paypal接口'},
    {'key': 'paypal_mch_id', 'type': 'paypal', 'value': '13265413', 'remark': 'paypal商户id'},
    {'key': 'paypal_mch_key', 'type': 'paypal', 'value': '13265413', 'remark': 'paypal商户key'},

    # Customer Service System
    {'key': 'customer_service_system', 'type': 'customer', 'value': 'enable', 'remark': '客服系统'},
    {'key': 'css_message_save', 'type': 'customer', 'value': '180', 'remark': '客服消息保存天数'},
    {'key': 'css_weapp', 'type': 'customer', 'value': 'enable', 'remark': '客服微信小程序'},
    {'key': 'css_weapp_id', 'type': 'customer', 'value': '454as54', 'remark': '客服微信小程序app_id'},
    {'key': 'css_weapp_key', 'type': 'customer', 'value': '454as54', 'remark': '客服微信小程序app_key'},

    # qcloud cos
    {'key': 'qcloud_cos', 'type': 'cos', 'value': 'enable', 'remark': 'cos存储'},
    {'key': 'qcloud_cos_id', 'type': 'cos', 'value': 'enable', 'remark': 'cos存储app_id'},
    {'key': 'qcloud_cos_key', 'type': 'cos', 'value': 'enable', 'remark': 'cos存储app_key'},
    {'key': 'qcloud_cos_bucket', 'type': 'cos', 'value': 'enable', 'remark': 'cos存储桶'},
    {'key': 'qcloud_cos_region', 'type': 'cos', 'value': 'enable', 'remark': 'cos存储区域'},

    # weapp
    {'key': 'weapp', 'type': 'weapp', 'value': 'enable', 'remark': '微信小程序'},
    {'key': 'weapp_id', 'type': 'weapp', 'value': '454as54', 'remark': '微信小程序app_id'},
    {'key': 'weapp_key', 'type': 'weapp', 'value': '454as54', 'remark': '微信小程序app_key'},

    # function switch
    {'key': 'system_setting', 'type': 'function', 'value': 'enable', 'remark': '系统设置'},
    {'key': 'user_login_record', 'type': 'function', 'value': 'enable', 'remark': '用户登录'},
    {'key': 'client_login_record', 'type': 'function', 'value': 'enable', 'remark': '客户登录记录'},
    {'key': 'reviews_system', 'type': 'function', 'value': 'enable', 'remark': '客户评论系统'},
    {'key': 'reward_system', 'type': 'function', 'value': 'enable', 'remark': '客户积分系统'},
    {'key': 'shipping_setting', 'type': 'function', 'value': 'enable', 'remark': '物流设置'},
    {'key': 'user_group', 'type': 'function', 'value': 'enable', 'remark': '员工分组'},
    {'key': 'client_group', 'type': 'function', 'value': 'disable', 'remark': '客户分组'},
    {'key': 'coupons', 'type': 'function', 'value': 'enable', 'remark': '优惠券系统'},
    {'key': 'financial', 'type': 'function', 'value': 'disable', 'remark': '财务系统'},
    {'key': 'wills', 'type': 'function', 'value': 'enable', 'remark': '收藏夹'},

]

language = [
    {'lang': 'gb'},
    {'lang': 'big5'},
    {'lang': 'en'},
    {'lang': 'jp'}
]

cms_category = [
    {'id': 1, 'level': 0, 'display': False, 'enable':True, 'name': 'system', 'parent_id': 0, 'sort':0}
]

cms_category_lang = [

]