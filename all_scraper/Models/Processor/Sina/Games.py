#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys


class Model_Processor_Sina_Games():
    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)
        hotGamesDom = tree.xpath("//div[@class='news-list-detail']/div[@class='listboxwp']/h3/a")
        if (hotGamesDom):
            for a_tag in hotGamesDom:
                try:
                    print (a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                except:
                    pass

    def getCurrnetPage(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)
        currentPageCount = tree.xpath("//div[@class='page_more']/div[@class='pageZone']/span[@class='isNow']/a/text()")
        if (currentPageCount):
            return currentPageCount[0]