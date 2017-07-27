#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '库存解析函数'
__author__ = 'javen'
__mtime__ = '17-2-22'
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
from Models.processor import Model_Processor
from lxml import etree
import sys

class Model_Processor_Product_Offer(Model_Processor):
    def __init__(self):
        pass

    def processInventory(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com/offerlist"
            sys.exit()
        tree = etree.HTML(html)
        quantities = []
        offering_id = []
        item_id = []
        queue = []
        # 库存数 //*[@id="sc-active-cart"] //*[@id='sc-saved-cart']
        try:
            try:
                # 库存
                quantities1 = tree.xpath("//*[@id='sc-active-cart']/form[@id='activeCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-quantity")
                quantities2 = tree.xpath("//*[@id='sc-saved-cart']/form[@id='savedCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-quantity")
            except Exception as err:
                print (err)
            try:
                # offering_id
                offering_id1 = tree.xpath("//*[@id='sc-active-cart']/form[@id='activeCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-encoded-offering")
                offering_id2 = tree.xpath("//*[@id='sc-saved-cart']/form[@id='savedCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-encoded-offering")
            except Exception as err:
                print (err)
            try:
                # item_id
                item_id1 = tree.xpath("//*[@id='sc-active-cart']/form[@id='activeCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-itemid")
                item_id2 = tree.xpath("//*[@id='sc-saved-cart']/form[@id='savedCartViewForm']/div[contains(@class, 'sc-list-body')]/div/@data-itemid")
            except Exception as err:
                print (err)
            if (quantities1):
                for quantity in quantities1:
                    quantities.append(quantity.strip())
            if (quantities2):
                for quantity in quantities2:
                    quantities.append(quantity.strip())
            if (offering_id1):
                for offeringid in offering_id1:
                    offering_id.append(offeringid)
            if(offering_id2):
                for offeringid in offering_id2:
                    offering_id.append(offeringid)
            if (item_id1):
                for itemid in item_id1:
                    item_id.append(itemid)
            if (item_id2):
                for itemid in item_id2:
                    item_id.append(itemid)
            for i in range(len(item_id)):
                queue.append(item_id[i]+"."+quantities[i])
        except Exception as err:
            print (err)
        # print (quantities)
        # print (item_id)
        # print (offering_id)
        # print (queue)
        data = dict(zip(offering_id, queue))
        # print (data)
        return data
