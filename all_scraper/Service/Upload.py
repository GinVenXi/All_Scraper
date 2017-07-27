#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-22'
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
import time
import urllib
import urllib2
import json

import datetime
from Service.Abstract import Service_Abstract

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

class Service_Upload(Service_Abstract):
    def __init__(self):
        self.accessKey = 'ABCDEFG'

    def doPost(self, d):
        data = urllib.urlencode(d)

        request = urllib2.Request('http://120.27.154.57/upload/amazon', data)

        response = urllib2.urlopen(request)
        file = response.read()
        if response.code != 200:
            return 'error code:' + response.code
        else:
            return file

    def upload(self, data, t='DownloadQueue'):

        # print (data)
        fields = {
            'access_key': self.accessKey,
            'data': json.dumps(data, cls=CJsonEncoder),
            'type': t,
            'time': time.time(),
            # 'debug': 1,
        }
        if (fields):
            print ("Encode success")
        # print (fields)
        result = self.doPost(fields)
        # print (result)
        result = json.loads(result)
        # {"success":true,"data":{"6":true}}
        ###########################需要根据实际上传返回值进行相应操作################################
        # result = {
        #     "success" : True,
        #     "data" : {
        #         "3": True,
        #     }
        # }
        # 返回结果
        #{
        	# success:false/true
        	# data: {
        	# 	1:true
        	# 	2:false
        	# 	3:true
        	# }
        # }
        print (result)
        # print (result["success"])
        if (result["success"] == True):
            return result['data']

        # if (result['message']):
        #     import datetime
        #     now = datetime.datetime.now()
        #     # 当前日期
        #     now_date = now.strftime("%Y-%m-%d %H:%M:%S")
        #     with open("/home/javen/PycharmProjects/AMAZON_SCRAPY/Cronjob/log.log", "a") as f:
        #         f.write(str(now_date) + "---Error from AmazonCloud:---" + result['message'] + "--Upload--")
        # return result