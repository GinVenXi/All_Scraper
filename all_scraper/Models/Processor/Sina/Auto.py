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
        # 新浪汽车解析代码*
'''
class Model_Processor_Sina_Auto(Model_Processor):
    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from https://www.amazon.com")
            sys.exit()
        tree = etree.HTML(html)
        try:
            # 首页右上角要闻
            try:
                qiche_a_tags = tree.xpath("//div[@class='headline fR']/div[@class='oftype']//a")
                if (qiche_a_tags):
                    for a_tag in qiche_a_tags:
                        try:
                            if ("http" in a_tag.xpath("@href")[0]):
                                print (a_tag.xpath("@href")[0])
                                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                        except:
                            pass
            except:
                pass
            # 首页下方最新要闻
            try:
                qiche_more_a_tags = tree.xpath("//div[@data-sudaclick='auto_feedxinxiliu']//ul/li/div[@class='info']//*[@class='title']/a")
                if (qiche_more_a_tags):
                    print (len(qiche_more_a_tags))
                    for a_tag in qiche_more_a_tags:
                        try:
                            if ("http" in a_tag.xpath("@href")[0]):
                                print (a_tag.xpath("@href")[0])
                                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                        except:
                            pass
            except Exception as err:
                print (err)
        except Exception as err:
            print (err)