#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import requests
from requests import RequestException

from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Models.Scraper.Sina.Base import Model_Scraper_Sina_Base
from Service.Abstract import Service_Abstract

class Service_Sina_Base(Service_Abstract):

    def __init__(self):
        super(Service_Sina_Base, self).__init__()
        self.sinaBaseMapper = Model_Mapper_Sina_Base()

    def getSinaBaseMapper(self):
        return self.sinaBaseMapper

    def scrape(self, url):
        self.scraper = Model_Scraper_Sina_Base()
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

    def scrape_content(self, download_queue):
        print (download_queue[3])
        if ("slide" in download_queue[3]):
            html = self.get_gb2312_page(download_queue[3])
            # print (html)
        else:
            html = self.get_utf8_page(download_queue[3])
            # print (html)
        url_id = download_queue[1]
        url = download_queue[3]
        if (html):
            try:
                # 对某个详细页面进行解析
                self.scraper = Model_Scraper_Sina_Base()
                content = self.scraper.process_content(html, url_id, url)
                result = self.getSinaBaseMapper().save_content(content)
                return result
            except Exception as err:
                print (err)
        return False

    def getDownloadQueueContent(self):
        downloadqueues = self.getSinaBaseMapper().find()
        return downloadqueues

    def get_utf8_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "utf-8"
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None

    def get_gbk_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "gbk"
            # print (response.encoding)
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None

    def get_gb2312_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "gb2312"
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None