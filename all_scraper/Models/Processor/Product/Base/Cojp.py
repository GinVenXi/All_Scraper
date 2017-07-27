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
import bs4
import sys
import time
'''
#############################################################
解析函数(主要针对产品页)
#############################################################
'''

class Model_Processor_Product_Base_Cojp(Model_Processor):

    def process(self, html):

        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.co.jp"
            sys.exit()
        tree = etree.HTML(html)
        soup = bs4.BeautifulSoup(html , "lxml")
        data = {}

        # 标题 title
        title = tree.xpath("//*[@id='productTitle']/text()")
        try:
            if(title):
                if (title[0] != ''):
                    data['title'] = title[0].strip()
                    # print (data['title'])
            else:
                title = tree.xpath("//*[@id='title_feature_div']/h1/text()")
                if (title):
                    if (title[0] != ''):
                        data['title'] = title[0].strip()
                    else:
                        print ("no title")
                else:
                    title = tree.xpath("//*[@id='ebooksProductTitle']/text()")
                    if (title):
                        if (title[0] != ''):
                            data['title'] = title[0].strip()
                        else:
                            print ("no title")
                    else:
                        title = tree.xpath("//*[@id='aiv-content-title']/text()")
                        if (title):
                            if (title[0] != ''):
                                data['title'] = title[0].strip()
                        else:
                            title = tree.xpath("//*[@id='btAsinTitle']/text()")
                            if (title):
                                if (title[0] != ''):
                                    data['title'] = title[0].strip()
                            else:
                                print ("no title")
        except:
            print ("title error")
        # print (data["title"])

        # 是否 fba 将其切换至fulfillment
        fba = tree.xpath("//*[@id='alternativeOfferEligibilityMessaging_feature_div' and @class='a-icon-prime']")
        if(fba != []):
            data['is_fba'] = '1'
        else:
            data['is_fba'] = '0'

        # 价格 price
        try:
            price = tree.xpath("//*[@id='priceblock_ourprice']/text()")
            if(price):
                if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                    data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                    # print (data['price'])
            else:
                price = tree.xpath("//*[@id='priceblock_saleprice']/text()")
                if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                    data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                    # print (data['price'])
                else:
                    price = tree.xpath("//*[@id='priceblock_dealprice']/text()")
                    if (price):
                        if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                            data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                    else:
                        price = tree.xpath(
                            "//*[@id='price-quantity-container']//span(contains(@class, 'guild_priceblock_ourprice'))")
                        if (price):
                            if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                                data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                        else:
                            print ("no price")
        except:
            try:
                price = tree.xpath("//*[@id='usedBuySection']//span[contains(@class, 'a-color-price')]/text()")
                if (price and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                    data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                    # print (price[0])
                else:
                    price = tree.xpath("//*[@id='buyNewSection']//span[contains(@class, 'a-color-price')]/text()")
                    if (price and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                        data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                    else:
                        price = tree.xpath(
                            "//*[@id='price-quantity-container']//span[contains(@class, 'guild_priceblock_ourprice')]/text()")
                        if (price and self.formatNumber(price[0].replace("\n", "").strip(), "co.jp").isdigit()):
                            data['price'] = self.formatNumber(price[0].replace("\n", "").strip(), "co.jp")
                            # print self.formatNumber(price[0].replace("\n", "").strip(), "co.uk")
                        else:
                            price = tree.xpath("//*[@id='priceBlock']//span[@class='banjoPrice']/text()")
                            if (price and self.formatNumber(price[0].replace("\n", "").strip(), "co.jp").isdigit()):
                                data['price'] = self.formatNumber(price[0].replace("\n", "").strip(), "co.jp")
                            else:
                                price = tree.xpath("//*[@id='priceblock_dealprice']/text()")
                                if (price):
                                    if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                                        data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                                else:
                                    price = tree.xpath("//*[@id='actualPriceValue']//strong/text()")
                                    if (price):
                                        if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                                            data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                                    else:
                                        price = tree.xpath("//*[@id='buybox']//tr[@class='kindle-price']//td[contains(@class, 'a-color-price')]/text()")
                                        if (price):
                                            if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                                                data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                                        else:
                                            price = tree.xpath("//*[@id='actualPriceValue']/text()")
                                            if (price):
                                                if (price[0].strip() != '' and self.formatNumber(price[0].strip(), "co.jp").isdigit()):
                                                    data['price'] = self.formatNumber(price[0].strip(), "co.jp")
                                            else:
                                                price = tree.xpath("//*[contains(@class, 'a-button-selected')]//span[contains(@class, 'a-color-base')]/text()")
                                                if (price):
                                                    if (self.formatNumber(price[0].replace("\n", "").strip(), "co.jp").isdigit()):
                                                        data['price'] = self.formatNumber(price[0].replace("\n", "").strip(), "co.jp")
                                                    else:
                                                        print ("no price")
                                                else:
                                                    print ("no price")
            except:
                print ("price error")
        # print (data["price"])

        # 原价 listprice
        # listprice = soup.select("#price span.a-text-strike")
        listprice = tree.xpath("//*[@class='a-text-strike']/text()")
        try:
            if(listprice):
                if (listprice[0].strip() != ''):
                    data['list_price'] = self.formatNumber(listprice[0].strip(), "co.jp")
                    # print (data['list_price'])
            else:
                listprice = tree.xpath("//*[@id='priceBlock']//span[@class='banjoListPrice']/text()")
                if (listprice):
                    data['list_price'] = self.formatNumber(listprice[0].replace("\n", "").strip(), "co.jp")
                else:
                    print ("no list_price")
        except:
            print ("list_price error")
        # print (data["list_price"])

        # 包邮方式 shipping
        shipping1 = tree.xpath("//*[@id='price-shipping-message']/b/text()")
        shipping2 = tree.xpath("//*[@id='price-shipping-message']/text()[2]")
        try:
            if (shipping1 or shipping2):
                try:
                    ship1 = ""
                    if (shipping1):
                        if (shipping1[0].strip() != '' and shipping1[0].strip() != '詳細'):
                            ship1 = shipping1[0].strip()
                        else:
                            shipping1 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/b/text()")
                            if (shipping1):
                                if (shipping1[0].strip() != ''):
                                    ship1 = shipping1[0].strip()
                    else:
                        shipping1 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/b/text()")
                        if (shipping1):
                            if (shipping1[0].strip() != ''):
                                ship1 = shipping1[0].strip()
                    ship2 = ""
                    if (shipping2):
                        if (shipping2[0].strip() != ''):
                            ship2 = shipping2[0].strip()
                        else:
                            shipping2 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/text()")
                            if (shipping2):
                                for i in shipping2:
                                    if (i.replace("\n", "").strip() != ''):
                                        ship2 = i.replace("\n", "").strip()
                    else:
                        shipping2 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/text()")
                        if (shipping2):
                            if (shipping2[0].strip() != ''):
                                for i in shipping2:
                                    if (i.replace("\n", "").strip() != ''):
                                        ship2 = i.replace("\n", "").strip()
                    if (ship1 and ship2):
                        data['shipping'] = (ship1 + " " + ship2).replace(".", "").replace("&", "").strip()
                    elif (ship1):
                        data['shipping'] = (ship1).replace(".", "").replace("&", "").strip()
                    elif (ship2):
                        data['shipping'] = (ship2).replace(".", "").replace("&", "").strip()
                except Exception as err:
                    print (err)
                    # print (data['shipping'])
            else:
                shipping1 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/b/text()")
                shipping2 = tree.xpath("//span[contains(@class, 'buyboxShippingLabel')]/text()")
                if (shipping1 or shipping2):
                    try:
                        ship1 = ""
                        if (shipping1):
                            if (shipping1[0].strip() != ''):
                                ship1 = shipping1[0].strip()
                        ship2 = ""
                        if (shipping2):
                            for i in shipping2:
                                if (i.replace("\n", "").strip() != ''):
                                    ship2 = i.replace("\n", "").strip()
                        if (ship1 and ship2):
                            data['shipping'] = (ship1 + " " + ship2).replace(".", "").replace("&", "").strip()
                        elif (ship1):
                            data['shipping'] = (ship1).replace(".", "").replace("&", "").strip()
                        elif (ship2):
                            data['shipping'] = (ship2).replace(".", "").replace("&", "").strip()
                    except Exception as err:
                        print (err)
                else:
                    shipping = tree.xpath("//*[@id='ourprice_shippingmessage']/span/text()")
                    if (shipping):
                        shipping = shipping[0].replace("\n", "").replace("&", "").strip()
                        if (shipping.strip() != ""):
                            data['shipping'] = shipping.strip()
                        else:
                            shipping = tree.xpath("//*[@id='ourprice_shippingmessage']//span[contains(@class, 'a-text-bold')]/text()")
                            if (shipping):
                                shipping = shipping[0].replace("\n", "").replace("&", "").strip()
                                if (shipping.strip() != ""):
                                    data['shipping'] = shipping.strip()
                    else:
                        shipping = tree.xpath(
                            "//*[@id='usedbuyBox']/div[@class='a-section a-spacing-mini']/div[@class='a-row']/text()")
                        if (shipping):
                            shipping = shipping[0].replace("&", "").strip()
                            data['shipping'] = shipping
                            # print (shipping[0])
                        else:
                            shipping = tree.xpath(
                                "//*[@id='soldByThirdParty']//span[contains(@class, 'shipping3P')]/text()")
                            if (shipping):
                                # print (shipping[0].replace("\n", "").replace("+", "").strip())
                                data['shipping'] = shipping[0].replace("\n", "").strip()
                            else:
                                shipping = tree.xpath(
                                    "//*[@id='price-quantity-container']//span[contains(@class, 'a-color-tertiary')]/text()")
                                if (shipping):
                                    data['shipping'] = shipping[0].replace("\n", "").strip()
                                else:
                                    shipping = tree.xpath("//*[contains(@class, 'buyboxShippingLabel')]/b/text()")
                                    if (shipping):
                                        data['shipping'] = shipping[0].replace("\n", "").strip()
                                    else:
                                        data['shipping'] = ''
                                        print ("no shipping")
        except:
            try:
                shipping1 = tree.xpath("//*[contains(@class, 'buyboxShippingLabel')]/a/text()")
                shipping2 = tree.xpath("//*[contains(@class, 'buyboxShippingLabel')]/text()")
                if (shipping1):
                    if (shipping1[0].strip() != ''):
                        ship1 = shipping1[0].strip()
                        # print (shipping1[0].strip())
                if (shipping2):
                    for ship in shipping2:
                        if (ship.replace("\n", "").strip() != ''):
                            ship2 = ship.replace("\n", "").strip()
                            # print (ship.replace("\n", "").strip())
                data['shipping'] = (ship1 + ship2).replace(".", "").replace("&", "").strip()
            except:
                print ("shipping error")

        # offer数 offer_count
        try:
            offer_count = tree.xpath("//*[@id='mbc']//div[@class='a-box-inner a-padding-base']//a/text()")
            if(offer_count):
                if(offer_count[0].strip() != ''):
                    count = offer_count[0].strip().replace("(", "").replace(")", "").strip().split("の新品")[0]
                    if (count.isdigit()):
                        data['offer_count'] = count
                    # print (data['offer_count'])
                    else:
                        offer_count = tree.xpath("//*[@id='mbc']/div[@class='a-box']//span/a/text()")
                        if (offer_count):
                            if (offer_count[0].strip() != ''):
                                # print (offer_count[0].strip())
                                count = offer_count[0].replace("新品の出品：", "").strip().replace("(", "").replace(")", "").strip().split(" ")[0].strip()
                                if (count.isdigit()):
                                    data['offer_count'] = count
                        else:
                            print ("no offer_count")
            else:
                # //*[@id="mbc"]/div[4]/div/div/span/a/text()
                offer_count = tree.xpath("//*[@id='mbc']")
                if (offer_count):
                    if (offer_count[0].strip() != ''):
                        count = offer_count[0].strip().replace("(", "").replace(")", "")[:2].strip()
                        if (count.isdigit()):
                            data['offer_count'] = count
                            # print (data['offer_count'])
                else:
                    print ("no offer_count")
        except:
            print ("offer_count error")

        # bestseller_node_id
        bestseller_node_id = tree.xpath("//*[@id='zeitgeistBadge_feature_div']/a/@href")
        try:
            if(bestseller_node_id):
                data['bestseller_node_id'] = bestseller_node_id[0].replace("/gp/bestsellers/" , "").split("/")[1]
            else:
                bestseller_node_id = tree.xpath("//*[@id='zeitgeistBadge_feature_div']/div/a/@href")
                if(bestseller_node_id):
                    if(bestseller_node_id[0].replace("/gp/bestsellers/" , "").split("/")[1] != ''):
                        data['bestseller_node_id'] = bestseller_node_id[0].replace("/gp/bestsellers/" , "").split("/")[1]
                    else:
                        print("no bestseller_node_id")
                else:
                    print("no bestseller_node_id")
        except:
            print ("bestseller_node_id error")

        # variation_count 子ASIN数(还要多测试几个页面) 暂时先使用该解析方法
        try:
            variation_count = tree.xpath("//*[@id='twisterJsInitializer_feature_div']/script/text()")
            if (variation_count):
                for count in variation_count:
                    for i in count.split(","):
                        if(i.strip()[:25] == '"num_total_variations" : '):
                            data['variation_count'] = i.strip()[25:].strip()
                            break
            # else:
            #     print ("no variation_count")
        except:
            print ("variation_count error")
        # print (data['variation_count'])

        # description 描述 还要在考虑其他情况
        description = []
        try:
            descriptionDom = tree.xpath("//*[@id='productDescription']//p/text()")
            if(descriptionDom):
                # print (description[1])
                try:
                    for des in descriptionDom:
                        if(des.replace("\n", "").strip() != ''):
                            # print (des.replace("\n", "").strip())
                            description.append(des.replace("\"", "").strip())
                except Exception as err:
                    print (err)
                descriptionDom = tree.xpath("//*[@id='productDescription']//strong//text()")
                if (descriptionDom):
                    for des in descriptionDom:
                        if(des.replace("\n", "").strip() != ''):
                            # print (des.replace("\n", "").strip())
                            des = des.replace("\n", "").strip()
                            description.append(des)
                if (description[0] != ""):
                    data['description'] = " ".join(description)
            else:
                descriptionDom = tree.xpath("//*[@id='mas-product-description']/div/text()")
                if (descriptionDom):
                    for des in descriptionDom:
                        if (des.replace("\n", "").strip() != ''):
                            description.append(des.replace("\"", "").strip())
                    data['description'] = " ".join(description)
                else:
                    print("no description")
        except:
            print ("description error")


        # seller fulfillment seller.name seller.id 卖家信息，发货信息，卖家名和卖家ID
        seller_link = tree.xpath("//*[@id='merchant-info']")
        try:
            if(seller_link):
                for sel in seller_link:
                    if ("が販売、発送します。" in sel.xpath("text()")[1].replace("\n", "").strip()):
                        # print (sel.xpath("text()")[1].replace("\n", "").strip())
                        if (sel.xpath("a/text()")[0].strip() == "Amazon.co.jp"):
                            # print "Amazon.co.jp"
                            data['seller_name'] = 'Amazon.co.jp'
                            data['fulfillment'] = 'AFN'
                            data['is_fba'] = '1'
                            print ("Amazon no seller_id")
                            break
                        else:
                            if (sel.xpath("a/text()")[0].strip() != ''):
                                # print (sel.xpath("a/text()")[0].strip())
                                data['seller_name'] = sel.xpath("a/text()")[0].strip()
                                data['fulfillment'] = 'MFN'
                                data['is_fba'] = '0'
                                seller_id = tree.xpath(".//*[@id='merchant-info']/a/@href")
                                if(seller_id):
                                    # print (seller_id[0])
                                    if(seller_id[0].strip().split("&")[1][7:] != ''):
                                        data['seller_id'] = seller_id[0].strip().split("&")[1][7:]
                                    else:
                                        print("no seller_id")
                    elif ("Amazon.co.jp が発送" in sel.xpath("a/text()")[1].replace("\n", "").strip()):
                        data['fulfillment'] = 'AFN'
                        data['is_fba'] = '1'
                        data['seller_name'] = sel.xpath("a/text()")[0].replace("\n", "").strip()
                        # print (sel.xpath("a/text()")[0].replace("\n", "").strip())
                        seller_id = tree.xpath(".//*[@id='merchant-info']/a/@href")
                        if (seller_id):
                            # print (seller_id[0])
                            if (seller_id[0].strip().split("&")[1][7:] != ''):
                                data['seller_id'] = seller_id[0].strip().split("&")[1][7:]
                            else:
                                print("no seller_id")
        except:
            try:
                seller_link = tree.xpath("//*[@id='sold-by']//span/text()")
                if (seller_link[1].strip() == "Amazon Services International, Inc."):
                    data['seller_name'] = 'Amazon.co.jp'
                    data['fulfillment'] = 'AFN'
                    data['is_fba'] = '1'
                    print ("Amazon no seller_id")
                    # print (seller_link[1].strip())
            except:
                try:
                    seller_link = tree.xpath("//*[@id='pe-text-availability-merchant-info']")
                    if (seller_link):
                        for i in seller_link:
                            for text in i.xpath("text()"):
                                # print (text.replace("\n", "").strip())
                                if (text.replace("\n", "").strip() == "が販売、発送します。"):
                                    if (i.xpath("a/text()")[0].strip() == "Amazon.co.jp"):
                                        # print (i.xpath("a/text()")[0].strip())
                                        data['seller_name'] = 'Amazon.co.jp'
                                        data['fulfillment'] = 'AFN'
                                        data['is_fba'] = '1'
                                        print ("Amazon no seller_id")
                                    else:
                                        if (i.xpath("a/text()")[0].strip() != ""):
                                            data['seller_name'] = i.xpath("a/text()")[0].strip()
                                            data['fulfillment'] = 'MFN'
                                            data['is_fba'] = '0'
                                            seller_id = tree.xpath("a/@href")
                                            if (seller_id):
                                                # print (seller_id[0])
                                                if (seller_id[0].strip().split("&")[1][7:] != ''):
                                                    data['seller_id'] = seller_id[0].strip().split("&")[1][7:]
                                                else:
                                                    print("no seller_id")
                except:
                    print ("seller info error")

        # first_available_date 首次上架时间
        first_available_date = tree.xpath("//*[@id='detailBullets_feature_div']/ul/li//span")
        try:
            if(first_available_date):
                first_cnt = 0
                for first_available in first_available_date:
                    for first in first_available:
                        try:
                            if(first.text != None):
                                if(first.text.strip() == "Amazon.co.jp での取り扱い開始日"):
                                    first_cnt = 1
                                    continue
                                if(first_cnt == 1):
                                    data['first_available_date'] = first.text.strip()
                                    break
                            else:
                                break
                        except Exception as err:
                            print (err)
            else:
                # //*[@id="productDetails_detailBullets_sections1"] //*[@id="productDetails_detailBullets_sections1"]/tbody/tr[7]/td
                first_available_date = tree.xpath("//*[@id='detail_bullets_id']//ul/li")
                if (first_available_date):
                    for i in first_available_date:
                        # print (i.xpath("b/text()")[0].replace("\n", "").strip())
                        if (i.xpath("b/text()")[0].replace("\n", "").strip() != ''):
                            if (i.xpath("b/text()")[0].strip() == "Amazon.co.jp での取り扱い開始日:"):
                                # print (i.xpath("text()")[0].strip())
                                data['first_available_date'] = i.xpath("text()")[0].strip()
                                break
                            if (i.xpath("b/text()")[0].strip() == "出版社:"):
                                # print (i.xpath("text()")[0].strip().split("(")[1].replace(")", "").strip())
                                data['first_available_date'] = i.xpath("text()")[0].strip().split("(")[1].replace(")", "").strip()
                                break
                else:
                    first_available_date = tree.xpath("//*[@id='productDetailsTable']//ul/li")
                    if (first_available_date):
                        for i in first_available_date:
                            try:
                                try:
                                    if (i.xpath("strong/text()")[0].strip() == "Amazon.co.jp での取り扱い開始日:"):
                                        data['first_available_date'] = i.xpath("text()")[0].strip()
                                        break
                                except:
                                    pass
                                try:
                                    if (i.xpath("b/text()")[0].strip() == "Amazon.co.jp での取り扱い開始日:"):
                                        data['first_available_date'] = i.xpath("text()")[0].strip()
                                        break
                                except:
                                    pass
                                try:
                                    if (i.xpath("strong/text()")[0].strip() == "Vinyl"):
                                        data['first_available_date'] = i.xpath("text()")[0].strip()
                                        break
                                except:
                                    pass
                                try:
                                    if (i.xpath("b/text()")[0].strip() == "Vinyl"):
                                        # print(i.xpath("text()")[0].strip())
                                        data['first_available_date'] = i.xpath("text()")[0].strip()
                                        break
                                except:
                                    pass
                                    # print (i.xpath("text()")[0].strip())
                            except:
                                continue
                    else:
                        first_available_date = tree.xpath("//*[@id='prodDetails']//tr[@class='date-first-available']/td[2]/text()")
                        if (first_available_date):
                            # print (first_available_date[0])
                            data['first_available_date'] = first_available_date[0].strip()
                        else:
                            print("no first_available_date")
        except:
            try:
                first_available_date = tree.xpath("//*[@id='productDetailsTable']//ul/li")
                if (first_available_date):
                    for i in first_available_date:
                        try:
                            if (i.xpath("b/text()")[0].strip() == "Publication Date:"):
                                data['first_available_date'] = i.xpath("text()")[0].strip()
                                break
                                # print (i.xpath("text()")[0].strip())
                        except:
                            continue
                else:
                    print("no first_available_date")
            except:
                print ("first_available_date error")
        # print (data['first_available_date'])

        # sale_rank 销售排名
        try:
            sales_rank = tree.xpath("//*[@id='SalesRank']/text()")
            if(sales_rank):
                if(sales_rank[1].replace("\n", "").replace("(", "").split("-")[1].replace(",", "").replace("位", "").strip() != "" and self.formatNumber(sales_rank[1].replace("\n", "").replace("(", "").split("-")[1].replace(",", "").replace("位", "").strip(), "co.jp").isdigit()):
                    data['sales_rank'] = self.formatNumber(sales_rank[1].replace("\n", "").replace("(", "").split("-")[1].replace(",", "").replace("位", "").strip(), "co.jp")
                else:
                    # cloth 分类下
                    sales_rank = tree.xpath(".//*[@id='SalesRank']/ul/li[1]/span[1]")
                    if (sales_rank):
                        if (self.formatNumber(sales_rank[0].text.strip(), "co.jp").isdigit()):
                            data['sales_rank'] = self.formatNumber(sales_rank[0].text.strip(), "co.jp")
                        else:
                            print ("no sales_rank")
                    else:
                        print("no sales_rank")
            else:
                sales_rank = tree.xpath("//*[@id='SalesRank']//td[@class='value']/text()")
                if (sales_rank):
                    for i in sales_rank:
                        if (i.replace("\n", "").strip() != ""):
                            # print (i)
                            if (i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[1].replace("位", "").strip() != '' and self.formatNumber(i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[1].replace("位", "").strip(), "co.jp").isdigit()):
                                # print (i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[1].replace("位", "").strip())
                                data['sales_rank'] = self.formatNumber(i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[1].replace("位", "").strip(), "co.jp")
                                break
                else:
                    print("no sales_rank")
        except:
            print ("sales_rank error")
        # print (data['sales_rank'])

        # category 分类
        try:
            category = tree.xpath("//*[@id='SalesRank']/text()")
            if (category):
                # print (category[1].replace("\n", "").replace("(", "").split("-")[0].strip())
                if (category[1].replace("\n", "").replace("(", "").split("-")[0].strip() != ""):
                    data['category'] = category[1].replace("\n", "").replace("(", "").split("-")[0].strip()
            else:
                category = tree.xpath("//*[@id='SalesRank']/a/text()")
                if(category):
                    if (category[1].replace("\n", "").replace("(", "").split("-")[0].strip() != ""):
                        data['category'] = category[1].replace("\n", "").replace("(", "").split("-")[0].strip()
                else:
                    category = tree.xpath("//*[@id='SalesRank']//td[@class='value']/text()")
                    if (category):
                        for i in category:
                            if (i.replace("\n", "").strip() != ""):
                                if (i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[0].strip() != ''):
                                    # print (i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[0].strip())
                                    data['category'] = i.replace(")", "").replace("(", "").replace("\n", "").strip().split("-")[0].strip()
                                    break
                    else:
                        print ("no category")
        except:
            print ("category error")


        # browse_node 浏览节点
        try:
            browse_node = tree.xpath(".//*[@id='SalesRank']//a[1]/@href")
            if(browse_node):
                if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/" , "").split("/")[0] != ''):
                    if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/" , "").split("/")[0] != "https:"):
                        data['browse_node'] = browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/" , "").split("/")[0]
                    else:
                        if (browse_node[0].split("/")[-3]):
                            data['browse_node'] = browse_node[0].split("/")[-3]
                        else:
                            print ("no browse_node")
                else:
                    if (browse_node[0].replace("/gp/bestsellers/" , "").split("/")[0] != ''):
                        data['browse_node'] = browse_node[0].replace("/gp/bestsellers/" , "").split("/")[0]
                    else:
                        if (browse_node[0].split("/")[-3]):
                            data['browse_node'] = browse_node[0].split("/")[-3]
                        else:
                            print ("no browse_node")
            else:
                browse_node = tree.xpath("//*[@id='productDetails_detailBullets_sections1']//tr")
                if (browse_node):
                    for i in range(len(browse_node)):
                        # print (sales_rank[i][0].text.strip())
                        if (browse_node[i][0].text.strip() == "Best Sellers Rank"):
                            browse_node = tree.xpath("//*[@id='productDetails_detailBullets_sections1']//tr[" + str(i + 1) + "]/td/span/span/a/@href")
                            browse_node = browse_node[0].replace("gp/bestsellers/" , "").strip().split("/")[1]
                            # print (browse_node)
                            if (browse_node):
                                data['browse_node'] = browse_node
                                break
                            else:
                                print ("no browse_node")
                                break
                else:
                    browse_node = tree.xpath("//*[@id='prodDetails']//tr[@id='SalesRank']/td[@class='value']/a/@href")
                    if (browse_node):
                        if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[0] != ''):
                            if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[
                                    0] != "https:"):
                                data['browse_node'] = \
                                browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[0]
                            else:
                                if (browse_node[0].split("/")[-3]):
                                    data['browse_node'] = browse_node[0].split("/")[-3]
                                else:
                                    print ("no browse_node")
                        else:
                            if (browse_node[0].replace("/gp/bestsellers/", "").split("/")[0] != ''):
                                data['browse_node'] = browse_node[0].replace("/gp/bestsellers/", "").split("/")[0]
                            else:
                                if (browse_node[0].split("/")[-3]):
                                    data['browse_node'] = browse_node[0].split("/")[-3]
                                else:
                                    print ("no browse_node")
                    else:
                        browse_node = tree.xpath("//*[@id='detail-bullets']//ul/li[@id='SalesRank']/a/@href")
                        if (browse_node):
                            if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[0] != ''):
                                if (browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[
                                        0] != "https:"):
                                    data['browse_node'] = \
                                        browse_node[0].replace("https://www.amazon.co.jp/gp/bestsellers/", "").split("/")[
                                            0]
                                else:
                                    if (browse_node[0].split("/")[-3]):
                                        data['browse_node'] = browse_node[0].split("/")[-3]
                                    else:
                                        print ("no browse_node")
                            else:
                                if (browse_node[0].replace("/gp/bestsellers/", "").split("/")[0] != ''):
                                    data['browse_node'] = browse_node[0].replace("/gp/bestsellers/", "").split("/")[0]
                                else:
                                    if (browse_node[0].split("/")[-3]):
                                        data['browse_node'] = browse_node[0].split("/")[-3]
                                    else:
                                        print ("no browse_node")
                        else:
                            print ("no browse_node")
        except:
            print ("browse_node error")

        # rating 评级
        rating = tree.xpath("//*[@id='averageCustomerReviews']//i[contains(@class, 'a-icon-star')]/span/text()")
        try:
            if(rating):
                if(rating[0].strip() != ''):
                    data['rating'] = self.formatRating(rating[0].strip(), "co.jp")
                    # print (data['rating'])
                else:
                    print("no rating")
            else:
                rating = tree.xpath("//*[@id='reviewStars']/span/text()")
                if (rating):
                    if (rating[0].strip() != ''):
                        data['rating'] = self.formatRating(rating[0].strip(), "co.jp")
                        # print (data['rating'])
                    else:
                        print("no rating")
                else:
                    rating = tree.xpath("//*[contains(@class, 'a-spacing-top-micro')]//i[contains(@class, 'a-icon a-icon-star')]/span/text()")
                    if (rating):
                        if (rating[0].strip() != ''):
                            data['rating'] = self.formatRating(rating[0].strip(), "co.jp")
                            # print (data['rating'])
                        else:
                            print("no rating")
                    else:
                        print("no rating")
        except:
            print ("rating error")

        # review_count 评论数
        review_count = tree.xpath("//*[@id='acrCustomerReviewText']/text()")
        try:
            if(review_count):
                if (review_count[0].strip() != ''):
                    data['review_count'] = self.formatReviewCount(review_count[0].strip(), "co.jp")
                    # print (data['review_count'])
                else:
                    print("no review_count")
            else:
                review_count = tree.xpath("//*[@id='reviewLink']/a/text()")
                if (review_count):
                    if (review_count[0].strip() != ''):
                        data['review_count'] = self.formatReviewCount(review_count[0].strip(), "co.jp")
                        # print (data['review_count'])
                    else:
                        print("no review_count")
                else:
                    review_count = tree.xpath("//*[contains(@class, 'a-spacing-top-micro')]//span[@class='a-size-small']/a/text()")
                    if (review_count):
                        data['review_count'] = self.formatReviewCount(review_count[0].strip(), "co.jp")
                    else:
                        print("no review_count")
        except:
            print ("review_count error")

        # images 图片
        images_data = []
        spans = tree.xpath(".//*[@id='altImages']/ul/li/span/span/span")
        try:
            if(spans):
                for span in spans:
                    if (span != ''):
                        try:
                            if(span.xpath(".//*[@class='a-button-text']/img/@src") != None):
                                images = span.xpath(".//*[@class='a-button-text']/img/@src")
                                if(images):
                                    for image in images:
                                        if (image):
                                            images_data.append(self.formatImage(image))
                                        else:
                                            print ("no image")
                            else:
                                print ("no images span_xpath")
                        except:
                            continue
                    else:
                        print ("no images span")
            else:
                spans = tree.xpath("//*[@id='dv-dp-left-content']//div[contains(@class, 'dp-img-bracket')]//img/@src")
                if (spans):
                    for span in spans:
                        if (span):
                            images_data.append(self.formatImage(span))
                        else:
                            print ("no image span")
                else:
                    spans = tree.xpath("//ol[@class='a-carousel']/li/a/img/@src")
                    if (spans):
                        for span in spans:
                            if (span):
                                images_data.append(self.formatImage(span))
                            else:
                                print ("no image span")
                    else:
                        spans = tree.xpath("//div[contains(@class, 'imageThumb')]/img/@src")
                        if (spans):
                            for span in spans:
                                if (span):
                                    images_data.append(self.formatImage(span))
                                else:
                                    print ("no image span")
                        else:
                            spans = tree.xpath("//div[contains(@class, 'dp-img-bracket')]//img/@src")
                            if (spans):
                                for span in spans:
                                    if (span):
                                        images_data.append(self.formatImage(span))
                                    else:
                                        print ("no image span")
                            else:
                                spans = tree.xpath("//div[@id='coverArt_feature_div']//img/@src")
                                if (spans):
                                    for span in spans:
                                        if (span):
                                            images_data.append(self.formatImage(span))
                                        else:
                                            print ("no image span")
                                else:
                                    spans = tree.xpath("//div[@id='ebooks-img-canvas']//img/@src")
                                    if (spans):
                                        for span in spans:
                                            if (span):
                                                try:
                                                    images_data.append(self.formatImage(span))
                                                except:
                                                    pass
                                            else:
                                                print ("no image span")
                                    else:
                                        spans = tree.xpath("//*[contains(@class, 'masrw-thumb-card')]/a/img/@src")
                                        if (spans):
                                            for span in spans:
                                                images_data.append(self.formatImage(span))
                                        else:
                                            print ("no images spans")
            if (images_data):
                data['images'] = images_data
            else:
                data['images'] = ''
        except:
            print ("images error")

        return data