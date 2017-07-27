#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time

from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Models.Scraper.Sina.Blog import Model_Scraper_Sina_Blog
from Service.Abstract import Service_Abstract
from Downloader.Selenium import Downloader_Selenium

class Service_Sina_Blog(Service_Abstract):

    def __init__(self):
        super(Service_Sina_Blog, self).__init__()
        self.sinaBaseMapper = Model_Mapper_Sina_Base()

    def scrape(self, url):
        self.scraper = Model_Scraper_Sina_Blog()
        try:
            data = self.scraper.scrape(url)
            if (data):
                # 此处应该进行数据插入
                print len(data)
                for items in data:
                    print len(items)
                    print (items)
                    for item in items:
                        self.sinaBaseMapper.save(item)
                if (len(data) > 0):
                    return True
            else:
                return False
        except Exception as err:
            print (err)
            return False


    # def get_blogpage_by_phantomjs(self, key, url):
    #     try:
    #         downloader_perform = Downloader_Selenium("chrome")
    #         downloader_perform.set_page_load_timeout(20)
    #         downloader_perform.get_html(url)
    #     except:
    #         downloader_perform.quit()
    #         self.get_blogpage_by_phantomjs(key, url)
    #     time.sleep(2)
    #     # 抓取新浪博客时需要进行相应操作，点击下一页
    #     try:
    #         count = 0
    #         while count < 5:
    #             time.sleep(2)
    #             downloader_perform.scrollTo(0, 9000)
    #             time.sleep(2)
    #             html = downloader_perform.get_page_source()
    #             time.sleep(2)
    #             process(key, html)
    #             pageCount = getCurrnetPage(html)
    #             print (pageCount)
    #             time.sleep(2)
    #             downloader_perform.driver.find_element_by_xpath(
    #                 "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
    #             time.sleep(5)
    #             anotherpageCount = getCurrnetPage(html)
    #             # print (anotherpageCount)
    #             if (pageCount == anotherpageCount):
    #                 downloader_perform.driver.find_element_by_xpath(
    #                     "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
    #             time.sleep(5)
    #             count += 1
    #         downloader_perform.quit()
    #     except Exception as err:
    #         print (err)
    #         downloader_perform.quit()
    #         self.get_blogpage_by_phantomjs(key, url)
    #     return False