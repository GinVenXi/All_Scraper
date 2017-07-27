#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import pytz
import time
import datetime
from Models.Abstract import Model_Abstract
class Model_Time(Model_Abstract):
    def __init__(self):
        pass

    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

    def getCurrentDatetime(self):
        tz = pytz.timezone('Asia/Shanghai')
        # tz = pytz.timezone('America/New_York')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return last_updated_time