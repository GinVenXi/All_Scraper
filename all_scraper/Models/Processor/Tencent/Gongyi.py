#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree

import re

from Models.processor import Model_Processor
import sys

'''
        # 腾讯公益首页解析代码*
'''
class Model_Processor_Tencent_Gongyi(Model_Processor):
    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from http://gongyi.qq.cn/")
            sys.exit()
        tree = etree.HTML(html)

        newsDom = tree.xpath("//a")
        if (newsDom):
            data = []
            for a_tag in newsDom:
                # print (a_tag.xpath("@href"))
                item = {}
                try:
                    # ("_" in a_tag.xpath("@href")[0] or "-" in a_tag.xpath("@href")[0]) and
                    if ("/a/" in a_tag.xpath("@href")[0] and ".qq.com/" in a_tag.xpath("@href")[0] and ".htm" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").replace("\r", "").strip() != ""):
                        if (a_tag.xpath("@href")[0].strip() == ""):
                            continue
                        else:
                            # print (a_tag.xpath("@href")[0].strip())
                            # url
                            item['url'] = self.formatUrl(a_tag.xpath("@href")[0].replace("#p=1", "").strip(), "tencent")
                            # print (item['url'])
                            # 新闻类型
                            if (item['url']):
                                type = item['url'].split(".qq.com")[0].replace("http://", "")
                                if ("slide" in type and "." in type):
                                    type = "slide"
                                elif ("." in type):
                                    type = type.split(".")[1]
                                item['type'] = type
                                # print (item['type'])
                            # title 标题
                            item['title'] = a_tag.xpath("text()")[0].replace("\n", "").replace("\"", "").strip()
                            # print (item['title'])
                            # 新闻id
                            try:
                                item['url_id'] = str(item['url'].split("/")[-1].split(".")[0])
                                # print (item['url_id'])
                            except:
                                pass
                    elif ("/a/" in a_tag.xpath("@href")[0] and ".htm" in a_tag.xpath("@href")[0] and ".htm" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").replace("\r", "").strip() != ""):
                        if (".qq.com" not in a_tag.xpath("@href")[0].strip()):
                            url = "http://gongyi.qq.com"+a_tag.xpath("@href")[0].strip()
                            # url
                            item['url'] = self.formatUrl(url.replace("#p=1", "").strip(), "tencent")
                            # print (item['url'])
                            # 新闻类型
                            if (item['url']):
                                type = item['url'].split(".qq.com")[0].replace("http://", "")
                                if ("slide" in type and "." in type):
                                    type = "slide"
                                elif ("." in type):
                                    type = type.split(".")[1]
                                item['type'] = type
                                # print (item['type'])
                            # title 标题
                            item['title'] = a_tag.xpath("text()")[0].replace("\n", "").replace("\"", "").strip()
                            # print (item['title'])
                            # 新闻id
                            try:
                                item['url_id'] = str(item['url'].split("/")[-1].split(".")[0])
                                # print (item['url_id'])
                            except:
                                pass

                except:
                    pass
                try:
                    # 判断url中是否有数字，即url中是否包含id
                    url_id = (re.search('.*([0-9]+).*', item['url_id']))
                except:
                    pass
                if (len(item) > 0 and url_id != None):
                    # print (item)
                    data.append(item)
        if (len(data)>0):
            print (len(data))
            return data

            # 获取当前页面页码

    def getCurrnetPage(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html")
            sys.exit()
        tree = etree.HTML(html)
        currentPageCount = tree.xpath("//span[@class='pagebox_num_nonce']/text()")
        if (currentPageCount):
            return currentPageCount