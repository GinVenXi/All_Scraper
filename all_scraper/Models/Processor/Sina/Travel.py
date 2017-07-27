#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys


class Model_Processor_Sina_Travel():
    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)
        hotPositionDom = tree.xpath("//div[contains(@class, 'traSlideCon')]//ul/li/div/h3/a")
        if (hotPositionDom):
            print (len(hotPositionDom))
            for a_tag in hotPositionDom:
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
        currentPageCount = tree.xpath("//div[@class='feed-card-page']/span[@class='pagebox_num_nonce']/text()")
        if (currentPageCount):
            return currentPageCount[0]