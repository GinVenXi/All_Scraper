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
class Model_Mapper_AmazonSellerProductOffer(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonSellerProductOffer, self).__init__()

    def save(self, region, asin, data):
        searchData = {
            "region": region,
            "asin": asin,
            "item_id": data["item_id"]
        }
        result = self.findData("all", "amazon_seller_product_offer", searchData)
        if (result):
            # print (result)
            try:
                result = self.update("amazon_seller_product_offer", data, searchData)
            except Exception as err:
                print (err)
        else:
            try:
                result = self.insert("amazon_seller_product_offer", data, searchData)
            except Exception as err:
                print (err)
        return result