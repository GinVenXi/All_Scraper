#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import sys

class Model_Processor_Sina_Edu():

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)
        MainContentDom = tree.xpath("//div[@class='wrap mainContent']")
        # MainContentLeftDom 教育首页左侧链接
        MainContentLeftDom = MainContentDom[0].xpath("div[@class='mainContent_l']")
        if (MainContentLeftDom):
            l_pDom = MainContentLeftDom[0].xpath("div[@class='mainContent_l_p']")
            if (l_pDom):
                l_p_title_tags = l_pDom[0].xpath("div[@class='slide_box_title']/h2/a")
                if (l_p_title_tags):
                    for a_tag in l_p_title_tags:
                        print (a_tag.xpath("@href")[0].strip())
                        print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                l_p_tags = l_pDom[0].xpath("div[@class='slide_box']/div/div/div[1]/div[@class='item']/a")
                if (l_p_tags):
                    for a_tag in l_p_tags:
                        print (a_tag.xpath("@href")[0].strip())
                        print (a_tag.xpath("@title")[0].strip())
            # mainContent_l_p_content
            l_p_contents_tags = MainContentLeftDom[0].xpath("div[contains(@class, 'mainContent_l_p_content')]")
            if (l_p_contents_tags):
                for l_p_content_tags in l_p_contents_tags:
                    l_p_content_imgs = l_p_content_tags.xpath("div[contains(@class, 'mainContent_l_p_img')]")
                    if (l_p_content_imgs):
                        for l_p_contents_img in l_p_content_imgs:
                            try:
                                print (l_p_contents_img.xpath('a/@href')[0].strip())
                                print (l_p_contents_img.xpath('div/text()')[0].replace("\n", "").strip())
                            except:
                                pass
                    l_p_content_ul_a = l_p_content_tags.xpath("ul/li/a")
                    if (l_p_content_ul_a):
                        for a_tag in l_p_content_ul_a:
                            try:
                                if (a_tag.xpath("text()")[0].replace("\n", "").strip()):
                                    print (a_tag.xpath("@href")[0].strip())
                                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())
                            except:
                                pass
        # MainContentRightDom 教育首页右侧链接
        MainContentRightDom = MainContentDom[0].xpath("div[@class='mainContent_r']")
        if (MainContentRightDom):
            try:
                r_pDom = MainContentRightDom[0].xpath("div[contains(@class, 'mainContent_r_p')]//a")
                for a_tag in r_pDom:
                    print (a_tag.xpath("@href")[0].strip())
                    print (a_tag.xpath("text()")[0].replace("\n", "").strip())
            except Exception as err:
                print (err)


        # 教育首页下侧最新报道
        NewContentDom = tree.xpath("//div[@id='feedCardContent']//div[@class='feed-card-item']/h2/a")
        if (NewContentDom):
            print (len(NewContentDom))
            for a_tag in NewContentDom:
                print (a_tag.xpath("@href")[0].strip())
                print (a_tag.xpath("text()")[0].replace("\n", "").strip())

    def getCurrnetPage(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()
        tree = etree.HTML(html)
        currentPageCount = tree.xpath("//div[@class='feed-card-page']/span[@class='pagebox_num_nonce']/text()")
        if (currentPageCount):
            return currentPageCount