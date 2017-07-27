#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-20'
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
from Service.Functions import Service_Functions
from Models.Scraper.Standard import Model_Scraper_Standard
from Models.Static.Scrape.Status import Model_Static_Scrape_Status
import sys

class Model_Scraper_Product_Offer1(Model_Scraper_Standard):
    def __init__(self, region):
        self.region = region
        self.processor = Service_Functions().getProcessor('Product_Offer', region)

    def process(self, asin):
        self.processOffer = Model_Scraper_Standard(self.region)
        content = self.processOffer.processOffer(self.region, asin)
        if(content):
            return content

    # def scrapeInventory(self, data):
    #     if (data == '' or data == None):
    #         return Model_Static_Scrape_Status.FAILED
    #     url ="http://www.amazon."+self.region+"/gp/aws/cart/add.html"
    #     fields = []
    #     session_id = None


    def scrape(self, asin):
        content = self.process(asin)
        if(content):
            # 这边写解析代码, 通过解析返回的数据再进行库存的抓取
            print (content)
            data = self.processor.process(content.encode('utf-8'))
            if(data):
                print (data)
                # 通过解析得到的数据进行库存的计算
                # Inventory = self.scrapeInventory(asin, data)
                # print (Inventory)
        pageCount = self.processor.getPageCount(content)
        # print (pageCount)
        if (pageCount > 1):
            for i in range(2, int(pageCount) + 1):
                # print (i)
                index = str((i - 1) * 10)
                pageUrl = "http://www.amazon." + "com" + "/gp/offer-listing/" + asin + "/ref=olpOffersSuppressed?ie=UTF8&f_new=true&overridePriceSuppression=1&startIndex=" + index
                # print (pageUrl)
                pageContent = self.processPageOffer(pageUrl)
                if (pageContent):
                    print (pageContent)
                    pageResult = self.processor.process(pageContent.encode('utf-8'))
                    if (pageResult):
                        print (pageResult)
                        # pageInventory = self.scrapeInventory(asin, pageResult)
                        # print (pageInventory)
        # return 返回拼接后的值，否则返回首页值
