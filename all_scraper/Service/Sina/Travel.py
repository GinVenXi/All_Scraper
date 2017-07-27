#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time
from Downloader.Selenium import Downloader_Selenium
from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Models.Scraper.Sina.Travel import Model_Scraper_Sina_Travel
from Service.Abstract import Service_Abstract

class Service_Sina_Travel(Service_Abstract):

    def __init__(self):
        super(Service_Sina_Travel, self).__init__()
        self.sinaBaseMapper = Model_Mapper_Sina_Base()

    def scrape(self, url):
        self.scraper = Model_Scraper_Sina_Travel()
        try:
            data = self.scraper.scrape(url)
            if (data):
                # 此处应该进行数据插入
                # print len(data)
                for items in data:
                    # print len(items)
                    for item in items:
                        self.sinaBaseMapper.save(item)
                if (len(data) > 0):
                    return True
            else:
                return False
        except Exception as err:
            print (err)
            return False


    # def get_travelpage_by_phantomjs(self, key, url):
    #     try:
    #         downloader_perform = Downloader_Selenium("all")
    #         downloader_perform.set_page_load_timeout(60)
    #         downloader_perform.get_html(url)
    #     except:
    #         downloader_perform.quit()
    #         self.get_travelpage_by_phantomjs(key, url)
    #     time.sleep(2)
    #     # 抓取新浪旅游首页，需要进行下一步操作，进行翻页(OK)
    #     try:
    #         count = 0
    #         while count < 5:
    #             time.sleep(2)
    #             downloader_perform.scrollTo(0, 100000)
    #             time.sleep(2)
    #             downloader_perform.scrollTo(0, 100000)
    #             time.sleep(2)
    #             downloader_perform.scrollTo(0, 100000)
    #             time.sleep(5)
    #             html = downloader_perform.get_page_source()
    #             if (html != ""):
    #                 time.sleep(2)
    #                 process(key, html)
    #                 try:
    #                     pageCount = getCurrnetPage(html)
    #                 except:
    #                     print ("no page count")
    #                 print (pageCount)
    #                 time.sleep(2)
    #                 try:
    #                     downloader_perform.driver.find_element_by_xpath("//span[@class='pagebox_next']").click()
    #                 except:
    #                     print ("wro")
    #                 # time.sleep(5)
    #                 # try:
    #                 #     anotherpageCount = getCurrnetPage(html)
    #                 #     if (pageCount == anotherpageCount):
    #                 #         downloader_perform.driver.find_element_by_xpath("//span[@class='pagebox_next']").click()
    #                 # except:
    #                 #     print ("wrong")
    #                 time.sleep(5)
    #                 count += 1
    #         downloader_perform.quit()
    #     except Exception as err:
    #         print (err)
    #         downloader_perform.quit()
    #         self.get_travelpage_by_phantomjs(key, url)
    #     return False