#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Scraper.Sina.Standard import Model_Scraper_Sina_Standard
from Service.Functions import Service_Functions


class Model_Scraper_Sina_Auto():

    def __init__(self):
        self.processor = Service_Functions().getSinaProcessor('Sina_Base')

    def scrape(self, url):
        self.process = Model_Scraper_Sina_Standard()
        html = self.process.process_auto(url)
        if (html):
            content = self.processor.process(html)
            return (content)