#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-23'
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
from Models.Static.Scrape.Status import Model_Static_Scrape_Status
from Service.Functions import Service_Functions


class Model_Scraper_TopReviewer(Model_Scraper_Standard):
    def __init__(self, region):
        self.region = region
        self.processor = Service_Functions().getProcessor('TopReviewer', region)

    def scrape(self, begin, end):
        if not str(begin).isdigit() and not str(end).isdigit() and begin > end:
            return Model_Static_Scrape_Status.FAILED
        self.process = Model_Scraper_Standard(self.region)
        data = []
        for i in range(begin, end):
            pageUrl = "https://www.amazon."+self.region+"/review/top-reviewers?page="+str(i)
            pageContent = self.process.processTopReviewer(pageUrl)
            if not pageContent:
                continue
            rankEnd = i * 10
            rankBegin = rankEnd - 9
            pageResult = self.processor.process(pageContent, rankBegin, rankEnd+1)
            if (pageResult):
                # 数组合并
                data.append(pageResult)
        if (len(data)):
            return data
