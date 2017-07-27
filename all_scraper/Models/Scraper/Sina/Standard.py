#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 21：59
'''
import requests
import time

from Models.Processor.Sina.Base import Model_Processor_Sina_Base
from Models.Processor.Sina.Blog import Model_Processor_Sina_Blog
from pyvirtualdisplay import Display

from Downloader.Selenium import Downloader_Selenium
from requests import RequestException

from Models.Processor.Sina.Edu import Model_Processor_Sina_Edu


class Model_Scraper_Sina_Standard():
    def __init__(self):
        pass

    def process(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "utf-8"
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None

    def process_gbk(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "gbk"
            # print (response.encoding)
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None

    def process_auto(self, url):
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                downloader_perform = Downloader_Selenium("chrome")
                downloader_perform.set_page_load_timeout(20)
                downloader_perform.get_html(url)
            except:
                downloader_perform.quit()
                self.process_auto(url)
            time.sleep(2)
            # 抓取汽车时需要相应操作，点击显示更多
            try:
                while True:
                    downloader_perform.driver.find_element_by_xpath("//div[@data-sudaclick='auto_feedgengduo']").click()
                    time.sleep(2)
            except:
                pass
            html = downloader_perform.get_page_source()
            downloader_perform.quit()
        return html

    def process_blog(self, url):
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                downloader_perform = Downloader_Selenium("all")
                downloader_perform.set_page_load_timeout(20)
                downloader_perform.get_html(url)
            except:
                downloader_perform.quit()
                self.process_blog(url)
            time.sleep(2)
            # 抓取新浪博客时需要进行相应操作，点击下一页
            try:
                self.processor = Model_Processor_Sina_Blog()
                count = 0
                data = []
                while True:
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    html = downloader_perform.get_page_source()
                    time.sleep(1)
                    result = self.processor.process(html)
                    if (result):
                        data.append(result)
                        count += 1
                    pageCount = self.processor.getCurrnetPage(html)
                    print (pageCount)
                    if (count >= 2):
                        break
                    time.sleep(1)
                    try:
                        downloader_perform.driver.find_element_by_xpath("//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    except:
                        downloader_perform.driver.find_element_by_xpath(
                            "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    time.sleep(2)
                    # anotherpageCount = self.processor.getCurrnetPage(html)
                    # # print (anotherpageCount)
                    # try:
                    #     if (pageCount == anotherpageCount):
                    #         downloader_perform.driver.find_element_by_xpath(
                    #             "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # except:
                    #     downloader_perform.driver.find_element_by_xpath(
                    #         "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # time.sleep(5)
                downloader_perform.quit()
            except Exception as err:
                print (err)
                downloader_perform.quit()
                self.process_blog(url)
        if (len(data) > 0):
            return data
        return False

    def process_edu(self, url):
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                downloader_perform = Downloader_Selenium("all")
                downloader_perform.set_page_load_timeout(60)
                downloader_perform.get_html(url)
            except:
                downloader_perform.quit()
                self.process_edu(url)
            time.sleep(2)
            # 抓取新浪博客时需要进行相应操作，点击下一页
            try:
                self.processor = Model_Processor_Sina_Base()
                count = 0
                data = []
                while True:
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    html = downloader_perform.get_page_source()
                    time.sleep(1)
                    result = self.processor.process(html)
                    if (result):
                        data.append(result)
                        count += 1
                    pageCount = self.processor.getCurrnetPage(html)
                    print (pageCount)
                    if (count >= 5):
                        break
                    time.sleep(1)
                    try:
                        downloader_perform.driver.find_element_by_xpath("//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    except:
                        downloader_perform.driver.find_element_by_xpath(
                            "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    time.sleep(2)
                    # anotherpageCount = self.processor.getCurrnetPage(html)
                    # # print (anotherpageCount)
                    # try:
                    #     if (pageCount == anotherpageCount):
                    #         downloader_perform.driver.find_element_by_xpath(
                    #             "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # except:
                    #     downloader_perform.driver.find_element_by_xpath(
                    #         "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # time.sleep(5)
                downloader_perform.quit()
            except Exception as err:
                print (err)
                downloader_perform.quit()
                self.process_edu(url)
        if (len(data) > 0):
            return data
        return False

    def process_travel(self, url):
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                downloader_perform = Downloader_Selenium("all")
                downloader_perform.set_page_load_timeout(60)
                downloader_perform.get_html(url)
            except:
                downloader_perform.quit()
                self.process_travel(url)
            time.sleep(2)
            # 抓取新浪博客时需要进行相应操作，点击下一页
            try:
                self.processor = Model_Processor_Sina_Base()
                count = 0
                data = []
                while True:
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    downloader_perform.scrollTo(0, 9000)
                    time.sleep(1)
                    html = downloader_perform.get_page_source()
                    time.sleep(1)
                    result = self.processor.process(html)
                    if (result):
                        data.append(result)
                        count += 1
                    pageCount = self.processor.getCurrnetPage(html)
                    print (pageCount)
                    if (count >= 5):
                        break
                    time.sleep(1)
                    try:
                        downloader_perform.driver.find_element_by_xpath("//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    except:
                        downloader_perform.driver.find_element_by_xpath(
                            "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    time.sleep(2)
                    # anotherpageCount = self.processor.getCurrnetPage(html)
                    # # print (anotherpageCount)
                    # try:
                    #     if (pageCount == anotherpageCount):
                    #         downloader_perform.driver.find_element_by_xpath(
                    #             "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # except:
                    #     downloader_perform.driver.find_element_by_xpath(
                    #         "//div[@class='feed-card-page']/span[@class='pagebox_next']").click()
                    # time.sleep(5)
                downloader_perform.quit()
            except Exception as err:
                print (err)
                downloader_perform.quit()
                self.process_travel(url)
        if (len(data) > 0):
            return data
        return False