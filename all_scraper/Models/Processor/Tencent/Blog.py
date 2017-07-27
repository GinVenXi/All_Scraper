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
        # 腾讯博客解析代码*
'''
class Model_Processor_Tencent_Blog(Model_Processor):

    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from http://blog.sina.com.cn/")
            sys.exit()
        tree = etree.HTML(html)
        # 新浪博客首页解析代码
        try:
            # boke_a_tags = tree.xpath("//*[@id='feedCardContent']//div[contains(@class, 'feed-card-item-blog')]/div[@class='feed-card-item-hd']/h2/a")
            boke_a_tags = tree.xpath("//a")
            if (boke_a_tags):
                data = []
                for a_tag in boke_a_tags:
                    item = {}
                    try:
                        if ("blog.sina.com.cn" in a_tag.xpath("@href")[0] and "html?" in a_tag.xpath("@href")[0] and a_tag.xpath("text()")[0].replace("\n", "").strip() != ""):
                            if (a_tag.xpath("text()")[0].replace("\n", "").strip() == u"[详细]"):
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
                            if (len(item)>0):
                                data.append(item)
                    except:
                        pass
            if (len(data)>0):
                # print (len(data))
                return data
        except Exception as err:
            print (err)

    # 获取当前页面页码
    def getCurrnetPage(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html")
            sys.exit()
        tree = etree.HTML(html)
        currentPageCount = tree.xpath("//span[@class='pagebox_num_nonce']/text()")
        if (currentPageCount):
            return currentPageCount