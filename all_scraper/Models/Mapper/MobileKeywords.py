#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-24'
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
from Models.Mapper.Abstract import Model_Mapper_Abstract
class Model_Mapper_MobileKeywords(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_MobileKeywords, self).__init__()

    def save(self, region, keywords, total):
        searchData = {
            "region": region,
            "name": keywords,
        }
        result = self.findData("all", "mobile_keywords", searchData)
        if (result):
            result = self.update("mobile_keywords", total, searchData)
        else:
            result = self.insert("mobile_keywords", total, searchData)
        return result
