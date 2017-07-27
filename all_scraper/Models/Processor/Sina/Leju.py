#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys

class Model_Processor_Sina_Leju():

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)

        TitDom = tree.xpath("//div[@class='ty_NewsTit']//h3/a")
        if (TitDom):
            for a_tag in TitDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())

        MainDom = tree.xpath("//div[@class='ty_NewsMain']/div[@class='ty_News_M']//a")
        if (MainDom):
            for a_tag in MainDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())


        BlockDom = tree.xpath("//div[contains(@class, 'z_index_box')]/div[contains(@class, 'b_mainBox')]//ul[contains(@class, 'd-imglist')]/li/h2/span/a[1]")
        if (BlockDom):
            for a_tag in BlockDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("@title")[0].strip())