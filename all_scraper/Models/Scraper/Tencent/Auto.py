#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Processor.Tencent.Content import Model_Processor_Tencent_Content
from Models.Scraper.Tencent.Standard import Model_Scraper_Tencent_Standard
from Service.Functions import Service_Functions


class Model_Scraper_Tencent_Auto():

    def __init__(self):
        self.processor = Service_Functions().getTencentProcessor('Tencent_Auto')

    def scrape(self, url):
        self.process = Model_Scraper_Tencent_Standard()
        html = self.process.process_gb2312(url)
        # print (html)
        if (html):
            content = self.processor.process(html)
            return (content)

    def process_content(self, html, url_id, url):
        scrape = Model_Processor_Tencent_Content()
        content = scrape.process(html)
        content['url_id'] = url_id
        content['url'] = url
        return content