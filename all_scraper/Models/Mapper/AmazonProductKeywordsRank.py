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
class Model_Mapper_AmazonProductKeywordsRank(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonProductKeywordsRank, self).__init__()

    def save(self, region, keywords, node_id, rank, data):
        searchData = {
            "region": region,
            "keywords": keywords,
            "node_id": node_id,
            "rank": rank,
        }
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        data['last_updated_time'] = last_updated_time
        result = self.insert("amazon_product_keywords_rank", data, searchData)
        return result

    def clearRankData(self, region, keywords, node_id):
        searchData = {"region": region, "keywords": keywords, "node_id": node_id}
        result = self.delete("amazon_product_keywords_rank", searchData)
        return result