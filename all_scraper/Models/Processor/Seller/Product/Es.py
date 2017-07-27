#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
from lxml import etree
from Models.processor import Model_Processor

class Model_Processor_Seller_Product_Es(Model_Processor):
    def __init__(self):
        pass

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.es"
            sys.exit()
        tree = etree.HTML(html)
        data = []

        # 总产品页
        listDoms = tree.xpath("//*[contains(@class, 's-result-list-parent-container')]/ul/li")
        # print (len(listDoms))
        if (listDoms):
            for itemDom in listDoms:
                # print (itemDom)
                item = {}
                # 抓取asin
                try:
                    asin = itemDom.xpath("@data-asin")
                    if (asin):
                        item['asin'] = asin[0].strip()
                        # print (item['asin'])
                except:
                    print ("asin error")

                # 抓取title
                try:
                    titleDom = itemDom.xpath("div//a[contains(@class, 's-access-detail-page')]/@title")
                    if (titleDom):
                        item['title'] = titleDom[0].strip()
                        # print (item['title'])
                except:
                    print ("title error")

                # 抓取image
                try:
                    imageDom = itemDom.xpath("div//img[contains(@class, 's-access-image')]/@src")
                    if (imageDom):
                        item['image'] = Model_Processor().formatImage(imageDom[0])
                        # print (item['image_url'])
                        imagewidthDom = itemDom.xpath("div//img[contains(@class, 's-access-image')]/@width")
                        if (imagewidthDom):
                            item['width'] = imagewidthDom[0].strip()
                            # print (item['image_width'])
                        imageheightDom = itemDom.xpath("div//img[contains(@class, 's-access-image')]/@height")
                        if (imageheightDom):
                            item['height'] = imageheightDom[0].strip()
                            # print (item['image_height'])
                except:
                    print ("image error")

                # 抓取price
                try:
                    priceDom = itemDom.xpath("div//span[contains(@class, 's-price')]/text()")
                    if (priceDom):
                        item['price'] = Model_Processor().formatNumber(priceDom[0], "es")
                except:
                    print ("price error")

                # 抓取list_price
                try:
                    list_priceDom = itemDom.xpath("div//span[contains(@class, 'a-text-strike')]/text()")
                    if (list_priceDom):
                        item['list_price'] = Model_Processor().formatNumber(list_priceDom[0], "es")
                except:
                    print ("list_price error")

                # 抓取rating
                try:
                    ratingDom = itemDom.xpath("div//i[contains(@class, 'a-icon-star')]/span/text()")
                    if (ratingDom):
                        item['seller_rating'] = Model_Processor().formatRating(ratingDom[0], "es")
                        # print (item['seller_rating'])
                except Exception as err:
                    print ("seller_rating error")

                # 抓取review_count
                try:
                    review_countDom = itemDom.xpath("div//div[@class='a-row a-spacing-none']/a/text()")
                    if (review_countDom):
                        item['review_count'] = Model_Processor().formatNumber(review_countDom[0], "es")
                        # print (item['review_count'])
                except:
                    print ("review_count error")

                # 抓取bestseller
                try:
                    bestsellerDom = itemDom.xpath("div//div[contains(@class, 'sx-badge-region')]/a/@href")
                    href = bestsellerDom[0].replace("/gp/bestsellers/", "").split("/")
                    if (len(href) > 2):
                        item['bestseller_search_index'] = href[0]
                        item['bestseller_browse_node_id'] = href[1]
                        # print (item['bestseller_search_index'])
                        # print (item['bestseller_browse_node_id'])
                    elif (len(href) == 2):
                        item['bestseller_search_index'] = href[0]
                        # print (item['bestseller_search_index'])
                except:
                    pass
                # print (item)
                data.append(item)
        # # 产品结果页1 btfResult
        # listDom1 = tree.xpath("//*[@id='atfResults']/ul/li")
        # # print (len(listDom1))
        # # 产品结果页2 btfResult
        # listDom2 = tree.xpath("//*[@id='btfResults']/ul/li")
        # # print (len(listDom2))
        # print (len(data))
        return data

    def getPageCount(self, html):
        pageCount = 1
        if (html == '' or html == None):
            return pageCount
        tree = etree.HTML(html)
        listDom = tree.xpath("//*[@id='pagn']/span[@class='pagnDisabled']/text()")
        if (listDom):
            for list in listDom:
                if (list.isdigit()):
                    pageCount = list
                    # print (pageCount)
        else:
            listDom = tree.xpath("//*[@id='pagn']/span[@class='pagnLink']/a")
            if (listDom):
                if (listDom[-1].text.isdigit()):
                    pageCount = listDom[-1].text
                    # print (listDom[-1].text)
        return (pageCount)