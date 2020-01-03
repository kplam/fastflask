#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: Kin P. Lam
@Date: 2020-01-02 23:18:00
@LastEditors  : Kin P. Lam
@LastEditTime : 2020-01-04 00:35:36
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/21 0:06


import smtplib
from email.mime.text import MIMEText
from email.header import Header


try:
    from .auth import *
    # from .database import *
    # from .models import *
    from .func import *
except ImportError:
    from libs.auth import *
    # from libs.database import *

    from libs.func import *


def simple_mail(host, user, pass_, receivers, subject, message):

    sender = user
    # receivers = ['10000@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(message, 'html', 'utf-8')
    # message['From'] = Header("[Shipxy error]", 'utf-8')
    # message['To'] =  Header("[amazon spyer error]", 'utf-8')

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(host, 465)
        smtpObj.login(user, pass_)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件,%s"%e)