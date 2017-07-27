#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Service.Functions import Service_Functions
from Models.Scraper.Standard import Model_Scraper_Standard

class Model_Scraper_Product_Base(Model_Scraper_Standard):

    def __init__(self , region):
        super(Model_Scraper_Product_Base, self).__init__(region)
        self.region = region
        self.processor = Service_Functions().getProcessor('Product_Base', region)

    def scrape(self , asin):
        self.process = Model_Scraper_Standard(self.region)
        url = "https://www.amazon."+self.region+"/dp/"+asin+"?th=1&psc=1"
        print (url)
        try:
            content = self.process.process(url)
        except Exception as err:
            print (err)
        try:
            if(content):
                # 解析代码
                data = self.processor.process(content.encode('utf-8'))
                if(data):
                    return data
                else:
                    return False
            elif (content == None):
                return None
            else:
                return False
        except:
            return False
