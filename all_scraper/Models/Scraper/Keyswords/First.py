#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import urllib

from Models.Scraper.Standard import Model_Scraper_Standard
from Service.Functions import Service_Functions

class Model_Scraper_Keywords_First(Model_Scraper_Standard):
    def __init__(self, region):
        super(Model_Scraper_Keywords_First, self).__init__(region)
        self.region = region
        self.processor = Service_Functions().getProcessor('Keywords_First', region)

    def scraper(self, keywords):
        self.process = Model_Scraper_Standard(self.region)
        url = "https://www.amazon." + self.region + "/gp/search?keywords=" + keywords + "&page=1"
        print (url)
        try:
            content = self.process.processkeywords(url)
        except Exception as err:
            print (err)
        try:
            if (content):
                # 这边写解析代码
                result = self.processor.process(content)
                if (result):
                    return result
            elif (content == None):
                return None
            else:
                return False
        except:
            return False