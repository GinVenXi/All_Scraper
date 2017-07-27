#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-12'
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
from Models.processor import Model_Processor
from lxml import etree
import sys

class Model_Processor_Product_Offer_De(Model_Processor):
    def __init__(self):
        pass

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.de/offerlist"
            sys.exit()

        tree = etree.HTML(html)
        queue = []
        div = tree.xpath("//*[@id='olpOfferList']//*[@class = 'a-row a-spacing-mini olpOffer']")
        for itemDom in div:
            data = {}
            # 价格 price
            try:
                price = itemDom.xpath("div//*[contains(@class, 'olpOfferPrice')]/text()")
                if (price):
                    data['price'] = self.formatNumber(price[0].strip(), "de")
            except:
                print ("price found error")

            # 包邮方式 shipping
            try:
                shipping1 = itemDom.xpath("div//p[contains(@class, 'olpShippingInfo')]/span/b/text()")
                shipping2 = itemDom.xpath("div//p[contains(@class, 'olpShippingInfo')]/span/text()[2]")
                try:
                    ship1 = ""
                    if (shipping1):
                        ship1 = shipping1[0].strip()
                    else:
                        shipping1 = tree.xpath("div//span[@class='olpShippingPrice']/text()")
                        if (shipping1):
                            ship1 = shipping1[0].strip()
                        else:
                            shipping1 = itemDom.xpath(
                                "div//p[contains(@class, 'olpShippingInfo')]/span/span/text()")
                            if (shipping1):
                                ship1 = shipping1[0].strip()
                except Exception as err:
                    print (err)
                try:
                    ship2 = ""
                    if (shipping2 and shipping2 != '' and shipping2[0].strip() != ""):
                        ship2 = shipping2[0].strip()
                    else:
                        shipping2 = tree.xpath("div//span[@class='olpShippingPriceText']/text()")
                        if (shipping2):
                            ship2 = shipping2[0].strip()
                        else:
                            shipping2 = itemDom.xpath(
                                "div//p[contains(@class, 'olpShippingInfo')]/span/span/text()")
                            if (shipping2):
                                ship2 = shipping2[1].strip()
                except Exception as err:
                    print (err)
                if (ship1 and ship2):
                    data['shipping'] = ("+ " + ship1 + " " + ship2).replace(".", "").replace("&", "").strip()
                elif (ship1):
                    data['shipping'] = (ship1).replace(".", "").replace("&", "").strip()
                elif (ship2):
                    data['shipping'] = (ship2).replace(".", "").replace("&", "").strip()
                else:
                    shipping = itemDom.xpath("div//p[contains(@class, 'olpShippingInfo')]/span/text()")
                    if (shipping):
                        data['shipping'] = (shipping[0]).replace(".", "").replace("&", "").strip()
                        # print (data['shipping'])
            except:
                try:
                    shipping = itemDom.xpath("div//p[contains(@class, 'olpShippingInfo')]/span/text()")
                    if (shipping):
                        data['shipping'] = (shipping[0]).replace(".", "").replace("&", "").strip()
                        # print (data['shipping'])
                except:
                    print ("shipping found error")

            # 状态 condition
            try:
                condition = itemDom.xpath("div//span[contains(@class, 'olpCondition')]/text()")
                if (condition):
                    if (condition[0].replace("\n", "").strip() != ''):
                        data['condition'] = self.formatCondition(condition[0].replace("\n", "").replace(" ", "").strip(), "de")
                        # print (data['condition'])
                else:
                    print ("no condition")
            except:
                print ("condition found error")

            # 发货方式 fulfillment
            try:
                fulfillment = itemDom.xpath("div//a[contains(@class, 'olpFbaPopoverTrigger')]/text()")
                if (fulfillment):                         # Versand durch Amazon.de
                    if (fulfillment[0].strip() == 'Versand durch Amazon.de'):
                        data['fulfillment'] = 'AFN'
                    else:
                        data['fulfillment'] = 'MFN'
                else:
                    data['fulfillment'] = 'MFN'
                # print (data['fulfillment'])
            except:
                print ("fulfillment found error")

            # 卖家信息 seller_name seller_id seller_logo
            try:
                seller = itemDom.xpath("div//h3[contains(@class, 'olpSellerName')]/span/a/text()")
                if (seller):
                    if (seller[0].strip() != ''):
                        data['seller_name'] = seller[0].strip()
                        # print (data['seller_name'])
                    else:
                        print ("no seller_name")
                    seller_image = itemDom.xpath("div//h3[contains(@class, 'olpSellerName')]/img/@src")
                    if(seller_image):
                        data['seller_logo_url'] = seller_image[0]
                        # print (img)
                        # 还要在获取图片的宽和高(目前好像美国站没有logo)
                else:
                    print ("Amazon no seller_info")
            except:
                print ("seller_info found error")

            # seller_id
            try:
                seller_id = itemDom.xpath("div//h3[contains(@class, 'olpSellerName')]/span/a/@href")
                if (seller_id):
                    data['seller_id'] = seller_id[0].split("&")[3].replace("seller=", "")
                    # print (data['seller_id'])
                else:
                    data['seller_id'] = ''
            except:
                print ("seller_id found error")

            # 卖家评级 seller_rating
            try:
                seller_rating = itemDom.xpath("div//i[contains(@class, 'a-icon-star')]/span/text()")
                if (seller_rating):
                    data['seller_rating'] = self.formatRating(seller_rating[0].strip(), "de")
                    # print (data['seller_rating'])
                # else:
                #     print ("no seller_rating")
            except:
                print ("seller_rating found error")

            # 卖家评级数 seller_rating_count
            try:
                seller_rating_count = itemDom.xpath("div[contains(@class, 'olpSellerColumn')]/p[contains(@class, 'a-spacing-small')]/text()")
                if (seller_rating_count):
                    try:
                        # print (seller_rating_count[2].strip().split("(")[1].replace(")", "").strip())
                        rating_count = self.formatSellerRatingCount(seller_rating_count[2].strip().split("(")[1].replace(")", "").strip(), "de")
                    except:
                        pass
                    if (rating_count.isdigit()):
                        data['seller_rating_count'] = rating_count
                    # print (data['seller_rating_count'])
                # else:
                #     print ("no seller_rating_count")
            except:
                # print ("seller_rating_count found error")
                pass

            # 卖家评级率 seller_positive
            try:
                seller_positive = itemDom.xpath("div[contains(@class, 'olpSellerColumn')]//b/text()")
                if (seller_positive):
                    if (seller_positive[0].strip() != ""):
                        if (self.formatPositive(seller_positive[0].replace(".", "").strip(), "de").isdigit()):
                            data['seller_positive'] = self.formatPositive(seller_positive[0].replace(".", "").strip(), "de")
                # else:
                #     print ("no seller_positive")
            except:
                print ("seller_positive found error")

            # session_id
            try:
                session_id = itemDom.xpath("div[contains(@class, 'olpBuyColumn')]/div/form/input[@name='session-id']/@value")
                if (session_id):
                    if (session_id[0].strip()):
                        data['session_id'] = session_id[0].strip()
                        # print (data['session_id'])
                else:
                    print ("no session_id")
            except:
                print ("session_id found error")

            # 获取offering_id
            try:
                offering_id = itemDom.xpath("div[contains(@class, 'olpBuyColumn')]/div/form/input[@name='offeringID.1']/@value")
                if (offering_id):
                    if (offering_id[0].strip() != ''):
                        data['offering_id'] = offering_id[0].strip()
                    # print (data['offering_id'])
                else:
                     print ("no offering_id")
            except:
                print ("offering_id found error")
            queue.append(data)
            # print (data)
        return queue

    # 获取当前offer的总页面数目
    def getPageCount(self, html):
        pageCount = 1
        if(html == '' or html == None):
            return pageCount
        tree = etree.HTML(html)
        listDom = tree.xpath("//*[@id='olpOfferListColumn']/div[@class='a-text-center a-spacing-large']/ul/li/a/text()")
        for list in listDom:
            if(list.isdigit()):
                pageCount = list
        # print (pageCount)
        return (pageCount)