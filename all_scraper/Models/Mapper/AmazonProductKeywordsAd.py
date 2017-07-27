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
import pytz
import datetime
from Models.Mapper.Abstract import Model_Mapper_Abstract
class Model_Mapper_AmazonProductKeywordsAd(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonProductKeywordsAd, self).__init__()

    def save(self, region, keywords, node_id, ad_position, ad_position_type, position, data):
        searchData = {
            "region": region,
            "keywords": keywords,
            "node_id": node_id,
            "ad_position": ad_position,
            "ad_position_type": ad_position_type,
            "position": position,
        }
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        data['last_updated_time'] = last_updated_time
        result = self.insert("amazon_product_keywords_ad", data, searchData)
        return result

    def clearAdData(self, region, keywords, node_id):
        searchData = {"region": region,
                      "keywords": keywords,
                      "node_id": node_id}
        result = self.delete("amazon_product_keywords_ad", searchData)
        return result