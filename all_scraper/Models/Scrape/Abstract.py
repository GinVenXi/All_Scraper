#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.scrape import Model_Scrape

class Model_Scrape_Abstract(object):
    def __init__(self , region):
        self.region = region
        self.scrape = {}

    def getScrape(self):
        return self.scrape

    def getStatus(self):
        return self.scrape['status']