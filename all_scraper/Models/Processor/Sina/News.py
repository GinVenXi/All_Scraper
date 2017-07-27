#coding: utf-8
'''
创建人：Javen
创建时间：
'''

from lxml import etree
import sys
from Models.processor import Model_Processor
'''
        # 新浪新闻中心首页解析代码
'''
class Model_Processor_Sina_News(Model_Processor):

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from http://news.sina.com.cn/"
            sys.exit()
        tree = etree.HTML(html)
        try:
            data = []
            xinwen_a_tags = tree.xpath("//ul[contains(@class, 'list_14') or @class='list']/li/a")
            if (xinwen_a_tags):
                # print len(xinwen_a_tags)
                for a_tag in xinwen_a_tags:
                    item = {}
                    try:
                        if ("sina.com.cn" in a_tag.xpath("@href")[0] and "html" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").strip() != ""):
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
                            item['title'] = a_tag.xpath("text()")[0].replace("\n", "").strip()
                            # print (item['title'])
                            item['url_id'] = item['url'].split("/")[-1].split(".")[0]
                            # print (item['url_id'])
                    except:
                        pass
                    if (len(item) > 0):
                        data.append(item)
            headlinexinwen_a_tags = tree.xpath("//div[contains(@class, 'ct_t_01')]//a")
            if (headlinexinwen_a_tags):
                # print len(xinwen_a_tags)
                for a_tag in headlinexinwen_a_tags:
                    item = {}
                    try:
                        if ("sina.com.cn" in a_tag.xpath("@href")[0] and "html" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").strip() != ""):
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
                            item['title'] = a_tag.xpath("text()")[0].replace("\n", "").strip()
                            # print (item['title'])
                            item['url_id'] = item['url'].split("/")[-1].split(".")[0]
                            # print (item['url_id'])
                    except:
                        pass
                    if (len(item) > 0):
                        data.append(item)
            focusnewsxinwen_a_tags = tree.xpath("//ul[@id='Blk01_Focus_Cont']/li/div[@class='text']/a")
            if (focusnewsxinwen_a_tags):
                for a_tag in focusnewsxinwen_a_tags:
                    item = {}
                    try:
                        if ("sina.com.cn" in a_tag.xpath("@href")[0] and "html" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").strip() != ""):
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
                            item['title'] = a_tag.xpath("text()")[0].replace("\n", "").strip()
                            # print (item['title'])
                            item['url_id'] = item['url'].split("/")[-1].split(".")[0]
                            # print (item['url_id'])
                    except:
                        pass
                    if (len(item) > 0):
                        data.append(item)
            if (len(data)>0):
                return data
        except Exception as err:
            print (err)
