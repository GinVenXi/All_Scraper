#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Models.Scraper.Sina.Video import Model_Scraper_Sina_Video
from Service.Abstract import Service_Abstract

class Service_Sina_Video(Service_Abstract):

    def __init__(self):
        super(Service_Sina_Video, self).__init__()
        self.sinaBaseMapper = Model_Mapper_Sina_Base()

    def getSinaBaseMapper(self):
        return self.sinaBaseMapper

    def scrape(self, url):
        self.scraper = Model_Scraper_Sina_Video()
        try:
            data = self.scraper.scrape(url)
            if (data):
                # 此处应该进行数据插入
                # print (data)
                for item in data:
                    self.getSinaBaseMapper().save(item)
                if (len(data)>0):
                    return True
            else:
                return False
        except Exception as err:
            print (err)
            return False