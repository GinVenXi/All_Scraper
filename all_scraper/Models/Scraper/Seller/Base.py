#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-25'
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
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Functions import Service_Functions
from Models.Scraper.Standard import Model_Scraper_Standard

class Model_Scraper_Seller_Base(Model_Scraper_Standard):
    def __init__(self, region):
        self.region = region
        self.processor = Service_Functions().getProcessor('Seller_Base', region)

    def scrape(self, merchantId):
        if not merchantId:
            return False
        url = "http://www.amazon."+self.region+"/gp/aag/main?seller="+merchantId
        content = Model_Scraper_Standard(self.region).processSeller(url)
        if (content):
            data = self.processor.process(content)
            if (data):
                return data
            return Model_Static_DownloadQueue_Status().SCRAPED_NO_DATA
        return Model_Static_DownloadQueue_Status().FAILED
