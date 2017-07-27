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
        # 新浪首页解析代码*
'''
class Model_Processor_Sina_Base(Model_Processor):
    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from http://www.sina.com.cn/")
            sys.exit()
        tree = etree.HTML(html)

        newsDom = tree.xpath("//a")
        if (newsDom):
            data = []
            for a_tag in newsDom:
                # print (a_tag.xpath("@href")[0])
                item = {}
                try:
                    if (("_" in a_tag.xpath("@href")[0] or "-" in a_tag.xpath("@href")[0]) and "sina.com.cn" in a_tag.xpath("@href")[0] and "shtml" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").strip() != ""):
                        if ("index" in a_tag.xpath("@href")[0]):
                            continue
                        # url
                        item['url'] = self.formatUrl(a_tag.xpath("@href")[0].strip(), "sina")
                        # print (item['url'])
                        # 新闻类型
                        if (item['url']):
                            type = item['url'].split(".sina.com.cn")[0].replace("http://", "")
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
            # print (len(data))
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