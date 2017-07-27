#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Processor.Sina.Content import Model_Processor_Sina_Content
from Models.Scraper.Sina.Standard import Model_Scraper_Sina_Standard
from Service.Functions import Service_Functions


class Model_Scraper_Sina_Base():

    def __init__(self):
        self.processor = Service_Functions().getSinaProcessor('Sina_Base')

    def scrape(self, url):
        self.process = Model_Scraper_Sina_Standard()
        html = self.process.process(url)
        if (html):
            content = self.processor.process(html)
            return (content)

    def process_content(self, html, url_id, url):
        scrape = Model_Processor_Sina_Content()
        content = scrape.process(html)
        content['url_id'] = url_id
        content['url'] = url
        return content