#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: K.P. Lam
# @Time: 2019/1/21 0:16

try:
    from connect import *
    from utils import *
except ImportError:
    from .connect import *
    from .utils import*
