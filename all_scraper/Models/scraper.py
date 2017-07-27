#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-18'
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
from Models.Message import Model_Message
import sys

class Model_Scraper(Model_Message):
    availableRegions = ['com', 'co.uk', 'de', 'co.jp', 'fr', 'es', 'it', 'ca']
    scrapes = []

    def __init__(self, region):
        if region not in self.availableRegions:
            sys.exit("Region "+region+" is not valid.")
        self.region = region

    def addScrape(self, scrape):
        self.scrapes.append(scrape)

    def getScrapes(self):
        for scrape in self.scrapes:
            try:
                if (scrape['download_queue_id']):
                    self.scrapes.remove(scrape)
            except:
                pass

        return self.scrapes

    def hasScrapes(self):
        try:
            # print (self.getScrapes())
            if (len(self.getScrapes()) > 0):
                return True
            return False
        except Exception as err:
            print (err)