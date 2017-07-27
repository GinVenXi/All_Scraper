#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-30'
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

import datetime
from Models.Mapper.Abstract import Model_Mapper_Abstract
class Model_Mapper_AmazonProduct(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonProduct, self).__init__()

    def save(self, region, asin, data):
        searchData = {'region': region,
                      'asin' : asin,
        }
        result = self.findData("all", "amazon_product", searchData)
        if (result):
            # print (result)
            result = self.update("amazon_product", data, searchData)
        else:
            tz = pytz.timezone('Asia/Shanghai')
            last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            data['last_updated_time'] = last_updated_time
            result = self.insert("amazon_product", data, searchData)
        return result

    def saveFromKeywordsProduct(self, region, data):
        searchData = {
            'region': region,
            'asin': data['asin']
        }
        result = self.findData("all", "amazon_product", searchData)
        if (result):
            result = self.update("amazon_product", data, searchData)
        else:
            result = self.insert("amazon_product", data, searchData)
        return result
