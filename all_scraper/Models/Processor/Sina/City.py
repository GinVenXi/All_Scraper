#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys


class Model_Processor_Sina_City():
    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from http://city.sina.com.cn/"
            sys.exit()
        tree = etree.HTML(html)
        # hotnews
        hotNewsDom = tree.xpath("//ul[@class='hot-news']/li/h2/a")
        if (hotNewsDom):
            for a_tag in hotNewsDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())

        # morenews
        moreNewsDom = tree.xpath("//ul[contains(@class, 'ull')]/li/a")
        if (moreNewsDom):
            for a_tag in moreNewsDom:
                if ("http" in a_tag.xpath("@href")[0].strip()):
                    print (a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                else:
                    print ("http://city.sina.com.cn" + a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())
