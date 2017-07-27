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
        # 新浪文章页通用解析代码*
'''
class Model_Processor_Sina_Content(Model_Processor):
    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from https://www.sina.com")
            sys.exit()
        tree = etree.HTML(html)
        data = {}
        # title 标题
        try:
            titleDom = tree.xpath("head/title/text()")
            if (titleDom):
                title = titleDom[0]
                # print (titleDom[0].split("_")[0])
                data['title'] = titleDom[0].split("_")[0].strip()
        except Exception as err:
            print (err)

        # summary 摘要（也可以说是description）
        try:
            descriptionDom = tree.xpath("head/meta[@name='Description' or @name='description']/@content")
            if (descriptionDom):
                description = descriptionDom[0]
                # print (description)
                # print (descriptionDom[0])
                data['summary'] = descriptionDom[0]
        except Exception as err:
            print (err)

        # Keywords 关键词
        try:
            keywordsDom = tree.xpath("head/meta[@name='keywords' or @name='Keywords']/@content")
            if (keywordsDom):
                if (title in keywordsDom[0]):
                    # print (self.formatSinaKeywords(keywordsDom[0].replace(title, ""), "sina"))
                    data['keywords'] = self.formatSinaKeywords(keywordsDom[0].replace(title, ""), "sina")
                elif (description in keywordsDom[0]):
                    # print (self.formatSinaKeywords(keywordsDom[0].replace(description, ""), "sina"))
                    data['keywords'] = self.formatSinaKeywords(keywordsDom[0].replace(description, ""), "sina")
                else:
                    # print (self.formatSinaKeywords(keywordsDom[0], "sina"))
                    data['keywords'] = self.formatSinaKeywords(keywordsDom[0], "sina")
        except Exception as err:
            print (err)

        # 新闻出版时间 published_time article:published_time
        try:
            published_timeDom = tree.xpath("head/meta[contains(@property, 'published_time')]/@content")
            if (published_timeDom):
                # print (published_timeDom[0])
                data['published_time'] = self.formatTime(published_timeDom[0], "sina")
                # print (data['published_time'])
        except Exception as err:
            print (err)

        if (len(data)>0):
            return data
        return False