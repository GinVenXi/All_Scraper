#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import requests
from requests import RequestException

from Models.Mapper.Tencent.Base import Model_Mapper_Tencent_Base
from Models.Scraper.Tencent.Sports import Model_Scraper_Tencent_Sports
from Service.Abstract import Service_Abstract

class Service_Tencent_Sports(Service_Abstract):

    def __init__(self):
        super(Service_Tencent_Sports, self).__init__()
        self.tencentBaseMapper = Model_Mapper_Tencent_Base()

    def getTencentBaseMapper(self):
        return self.tencentBaseMapper

    def scrape(self, url):
        self.scraper = Model_Scraper_Tencent_Sports()
        try:
            data = self.scraper.scrape(url)
            if (data):
                # 此处应该进行数据插入
                # print (data)
                for item in data:
                    self.getTencentBaseMapper().save(item)
                if (len(data)>0):
                    return True
            else:
                return False
        except Exception as err:
            print (err)
            return False

    def scrape_content(self, download_queue):
        print (download_queue[3])
        if ("le.qq.com" in download_queue[3]):
            html = self.get_utf8_page(download_queue[3])
            # print (html)
        else:
            html = self.get_gb2312_page(download_queue[3])
            # print (html)
        url_id = download_queue[1]
        url = download_queue[3]
        if (html):
            try:
                # 对某个详细页面进行解析
                self.scraper = Model_Scraper_Tencent_Sports()
                content = self.scraper.process_content(html, url_id, url)
                result = self.getTencentBaseMapper().save_content(content)
                return result
            except Exception as err:
                print (err)
        return False

    def getDownloadQueueContent(self):
        downloadqueues = self.getTencentBaseMapper().find()
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