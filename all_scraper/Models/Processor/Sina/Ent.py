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
        # 新浪娱乐解析代码*
'''
class Model_Processor_Sina_Ent(Model_Processor):
    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from https://www.amazon.com")
            sys.exit()
        tree = etree.HTML(html)
        try:
            yule_a_tags = tree.xpath("//*[contains(@id, 'toutiao')]//a")
            if (yule_a_tags):
                for a_tag in yule_a_tags:
                    try:
                        if ("http" in a_tag.xpath("@href")[0]):
                            print (a_tag.xpath("@href")[0])
                            print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                    except:
                        pass
        except Exception as err:
            print (err)