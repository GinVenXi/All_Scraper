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
from Models.Abstract import Model_Abstract

class Model_Amazon_Product(Model_Abstract):
    def __init__(self):
        pass
    keys = ['id', 'region', 'asin', 'variation_parentage', 'parent_asin', 'status', 'status', 'title', 'description', 'detail_page_url', 'category', 'browse_node', 'sales_rank', 'rating', 'review_count', 'price', 'list_price', 'fulfillment', 'seller_id', 'seller_name', 'first_available_date', 'bestseller_node_id', 'is_fba', 'variation_count', 'offer_count', 'last_updated_time']

