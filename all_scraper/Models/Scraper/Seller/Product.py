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
from Models.Scraper.Standard import Model_Scraper_Standard
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Functions import Service_Functions


class Model_Scraper_Seller_Product(Model_Scraper_Standard):
    def __init__(self, region):
        self.region = region
        self.processor = Service_Functions().getProcessor('Seller_Product', region)

    def scrape(self, merchantId):
        if not merchantId:
            return False
        url = "https://www.amazon."+self.region+"/s?merchant="+merchantId
        print (url)
        content = Model_Scraper_Standard(self.region).processSellerProduct(url)
        if (content):
            result = self.processor.process(content)
            if (result):
                data = []
                data.append(result)
                pagecount = int(self.processor.getPageCount(content))
                pagecount = 1 # 测试
                if (pagecount > 1):
                    if(pagecount > 50):
                        pagecount = 50 # 测试 原为50
                    for i in range(2, pagecount+1):
                        pageurl = "https://www.amazon."+self.region+"/s?merchant="+merchantId+"&page="+str(i)
                        print (pageurl)
                        pageContent = Model_Scraper_Standard(self.region).processSellerProduct(pageurl)
                        if not pageContent:
                            continue
                        pageResult = self.processor.process(pageContent)
                        if (pageResult):
                            data.append(pageResult)
                return data
            return Model_Static_DownloadQueue_Status().SCRAPED_NO_DATA
        return Model_Static_DownloadQueue_Status().FAILED