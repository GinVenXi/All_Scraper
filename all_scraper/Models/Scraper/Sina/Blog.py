#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Scraper.Sina.Standard import Model_Scraper_Sina_Standard


class Model_Scraper_Sina_Blog():

    def __init__(self):
        pass

    def scrape(self, url):
        self.process = Model_Scraper_Sina_Standard()
        data = self.process.process_blog(url)
        if (data):
            return (data)