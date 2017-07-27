#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-24'
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

class Model_Scraper_Mobile_Product_Base(Model_Scraper_Standard):

    def __init__(self , region):
        self.region = region
        self.processor = Service_Functions().getProcessor('MobileProduct_Base', region)

    def scrape(self , region, keywords):
        result = []
        self.process = Model_Scraper_Standard(region)
        requrl = "https://www.amazon."+region+"/s?page="+str(1)+"&keywords="+keywords+"&dataVersion=v0.2&cid=08e6b9c8bdfc91895ce634a035f3d00febd36433&format=json"
        content = self.process.mobile_process(requrl)
        if(content):
            # 解析代码
            # print (content)
            data = self.processor.mobile_process(region, content)
            if(data):
                # print (data)
                result.append(data)
                page_count = content['pagination']['numPages']
                # print (page_count)
                if (int(page_count) > 20):
                    page_count = 20
                for k in range(2, page_count + 1):
                    try:
                        requrl = "https://www.amazon." + region + "/s?page=" + str(k) + "&keywords=" + keywords + "&dataVersion=v0.2&cid=08e6b9c8bdfc91895ce634a035f3d00febd36433&format=json"
                        # print (requrl)
                        content = self.process.mobile_process(requrl)
                        result.append(self.processor.mobile_process(region, content))
                    except Exception as err:
                        print (err)
                try:
                    total = {}
                    total['total'] = content['resultsMetadata']['totalResults']
                except Exception as err:
                    print (err)
                result.append(total)
            return result