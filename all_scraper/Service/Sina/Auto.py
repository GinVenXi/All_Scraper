#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time

from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Service.Abstract import Service_Abstract
from Downloader.Selenium import Downloader_Selenium
from Models.Scraper.Sina.Auto import Model_Scraper_Sina_Auto


class Service_Sina_Auto(Service_Abstract):

    def __init__(self):
        super(Service_Sina_Auto, self).__init__()
        self.sinaBaseMapper = Model_Mapper_Sina_Base()

    def scrape(self, url):
        self.scraper = Model_Scraper_Sina_Auto()
        try:
            data = self.scraper.scrape(url)
            if (data):
                # 此处应该进行数据插入
                # print (data)
                for item in data:
                    self.sinaBaseMapper.save(item)
                if (len(data) > 0):
                    return True
            else:
                return False
        except Exception as err:
            print (err)
            return False

    # def get_autopage_by_phantomjs(self, url):
    #     try:
    #         downloader_perform = Downloader_Selenium("chrome")
    #         downloader_perform.set_page_load_timeout(20)
    #         downloader_perform.get_html(url)
    #     except:
    #         downloader_perform.quit()
    #         self.get_autopage_by_phantomjs(url)
    #     time.sleep(2)
    #     # 抓取汽车时需要相应操作，点击显示更多
    #     try:
    #         while True:
    #             downloader_perform.driver.find_element_by_xpath("//div[@data-sudaclick='auto_feedgengduo']").click()
    #             time.sleep(2)
    #     except:
    #         print ("no found")
    #     html = downloader_perform.get_page_source()
    #     downloader_perform.quit()
    #     return html