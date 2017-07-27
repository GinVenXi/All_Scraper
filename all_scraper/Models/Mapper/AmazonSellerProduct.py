#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-5'
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
class Model_Mapper_AmazonSellerProduct(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonSellerProduct, self).__init__()

    def save(self, region, asin, data):
        searchData = {
            "region": region,
            "asin": asin,
            "seller_id": data['seller_id'],
        }
        result = self.findData("all", "amazon_seller_product", searchData)
        if (result):
            result = self.update("amazon_seller_product", data, searchData)
        else:
            result = self.insert("amazon_seller_product", data, searchData)
        return result