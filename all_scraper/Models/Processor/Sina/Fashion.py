#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys

class Model_Processor_Sina_Fashion():

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)

        # 今日热点
        FocusTodayDom = tree.xpath("//div[contains(@class, 'part0')]//div[@class='blk00_c']//h5/a")
        if (FocusTodayDom):
            for a_tag in FocusTodayDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
        FocusTodayMoreDom = tree.xpath("//div[contains(@class, 'part0')]//div[@class='blk00_c']//p/a")
        if (FocusTodayMoreDom):
            for a_tag in FocusTodayMoreDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())

        # 时尚潮流，美容美体，尚品生活
        blk06Dom = tree.xpath("//div[@class='blk06']//div[contains(@class, 'imgwrap')]/a")
        if (blk06Dom):
            for a_tag in blk06Dom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("span/text()")[0].replace("\n", "").strip())
        blk07h4Dom = tree.xpath("//div[@class='blk07']/div[contains(@class, 'blk07_item')]/h4/a")
        if (blk07h4Dom):
            for a_tag in blk07h4Dom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
        blk07liDom = tree.xpath("//div[@class='blk07']/div[contains(@class, 'blk07_item')]/ul/li/a")
        if (blk07liDom):
            for a_tag in blk07liDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())

        # 婚嫁新娘，艺术生活，星座心理
        blk22Dom = tree.xpath("//div[contains(@class, 'blk22')]/div[contains(@class, 'imgwrap')]/a")
        if (blk22Dom):
            for a_tag in blk22Dom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("span/text()")[0].replace("\n", "").strip())
        blk23headDom = tree.xpath("//div[contains(@class, 'blk23')]/div[@class='blk23_hdline']/h4/a")
        if (blk23headDom):
            for a_tag in blk23headDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
        blk23liDom = tree.xpath("//div[contains(@class, 'blk23')]/ul/li/a")
        if (blk23liDom):
            for a_tag in blk23liDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())
        # 时尚大片
        blk36Dom = tree.xpath("//div[contains(@class, 'blk36')]/div[contains(@class, 'imgwrap')]/a")
        if (blk36Dom):
            for a_tag in blk36Dom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("span/text()")[0].replace("\n", "").strip())
        # 合作媒体
        wrap37Doms = tree.xpath("//div[contains(@class, 'wrap37')]/div[contains(@class, 'blk38')]")
        for wrap37Dom in wrap37Doms:
            blk38imgDom = wrap37Dom.xpath("div[contains(@class, 'imgwrap')]/a")
            if (blk38imgDom):
                for a_tag in blk38imgDom:
                    print (a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("span/text()")[0].replace("\n", "").strip())
            blk38liDom = wrap37Dom.xpath("ul/li/a")
            if (blk38liDom):
                for a_tag in blk38liDom:
                    print (a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())