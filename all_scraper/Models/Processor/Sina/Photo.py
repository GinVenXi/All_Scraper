#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys

class Model_Processor_Sina_Photo():

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)

        # box
        boxesDom = tree.xpath("//div[@class='scroll_cont']/div/div[1]/div[@class='box']")
        if (boxesDom):
            for boxDom in boxesDom:
                print (boxDom.xpath("a/@href")[0].strip())
                print (boxDom.xpath("span[@class='title']/text()")[0].replace("\n", "").strip())


