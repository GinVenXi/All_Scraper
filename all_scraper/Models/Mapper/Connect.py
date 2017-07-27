#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-16'
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

import pymysql
#mysql 连接类
class Model_Mapper_Connect():
    def __init__(self,host,port,user,passwd,db,charset='utf8'):
        self.conn = pymysql.connect(host = host , port = port , user = user , passwd = passwd , db = db , charset = charset)
    def connects(self):
        return self.conn
    #关闭mysql连接
    def close(self):
        self.conn.close()