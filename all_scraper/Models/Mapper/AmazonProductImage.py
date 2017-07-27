#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-1'
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
class Model_Mapper_AmazonProductImage(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonProductImage, self).__init__()

    # 产品图片sql语句
    def save(self, region, asin, url, position):
        searchData = {'region': region, 'asin': asin, 'url': url}
        result = self.findData("all", "amazon_product_image", searchData)
        if (result):
            # print (result)
            result = self.update("amazon_product_images", position, searchData)
        else:
            result = self.insert("amazon_product_images", position, searchData)
        return result

    # 关键词图片sql语句
    def save_img(self, region, asin, data):
        searchData = {'region': region, 'asin': asin}
        result = self.findData("all", "amazon_product_image", searchData)
        if (result):
            # print (result)
            pass
        else:
            result = self.insert("amazon_product_image", data, searchData)
        return result