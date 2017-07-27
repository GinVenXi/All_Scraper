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
class Model_Mapper_AmazonSeller(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonSeller, self).__init__()

    def save(self, region, data):
        searchData = {
            "region": region,
            "seller_id": data['seller_id'],
        }
        result = self.findData("all", "amazon_seller", searchData)
        if (result):
            result = self.update("amazon_seller", data, searchData)
        else:
            result = self.insert("amazon_seller", data, searchData)
        return result

    def save_seller(self, region, seller_id, data):
        searchData = {
            "region": region,
            "seller_id": seller_id,
        }
        result = self.findData("all", "amazon_seller", searchData)
        if (result):
            result = self.update("seller", data, searchData)
        else:
            result = self.insert("seller", data, searchData)
        return result

    def save_productsseller(self, region, seller_id):
        searchData = {
            "region": region,
            "seller_id": seller_id,
        }
        result = self.findData("all", "amazon_seller", searchData)
        if (result):
            pass
        else:
            result = self.insert("product_seller", searchData)
        return result

    def save_updaterank(self, region, seller_id):
        searchData = {
            "region": region,
            "seller_id": seller_id,
        }
        self.update("productssellerrank", searchData)