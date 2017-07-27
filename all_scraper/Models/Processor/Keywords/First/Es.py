#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-14'
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
from Models.processor import Model_Processor
from lxml import etree

class Model_Processor_Keywords_First_Es(Model_Processor):
    def __init__(self):
        pass

    def process(self, html, page_id=1):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.es"
            sys.exit()

        tree = etree.HTML(html)
        data = []
        # https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=handbags
        try:
            # 处理中间产品
            listDom1 = tree.xpath('//*[@id="atfResults"]/ul/li')
            listDom2 = tree.xpath('//*[@id="btfResults"]/ul/li')
            listDoms = tree.xpath("//*[@class='a-row s-result-list-parent-container']/ul/li")
            # print (len(listDoms))
            if (listDoms):
                page_position = 1
                sponsor_position = 1
                previous_sponsor_position_type = 'top'
                for itemDom in listDoms:
                    item = {'sponsor': 0, 'page_id': page_id, 'page_position': page_position}
                    # 标记为sponsor的产品 s-sponsored-list-header //*[@id="result_48"]/div/h5 //*[@id="result_24"]/div/div/div/div[a-fixed-left-grid-col a-col-right]/h5
                    sponsorDom = itemDom.xpath("div//*[contains(@class, 's-sponsored-list-header')]/text()")
                    # sponsorDom = soup.select(".s-sponsored-list-header")
                    if (sponsorDom):
                        item['sponsor'] = 1
                    else:
                        # a-color-tertiary
                        sponsorDom = itemDom.xpath("div//h5[contains(@class, 'a-color-tertiary')]/text()")
                        if (sponsorDom):
                            item['sponsor'] = 1
                    if (item['sponsor'] == 1):
                        if (page_position <= 4):
                            sponsor_position_type = 'top'
                        else:
                            sponsor_position_type = 'bottom'
                            if (sponsor_position_type != previous_sponsor_position_type):
                                sponsor_position = 1
                                previous_sponsor_position_type = 'bottom'
                        item['sponsor_position_type'] = sponsor_position_type
                        item['sponsor_position'] = sponsor_position
                        sponsor_position += 1
                    page_position += 1

                    # asin
                    try:
                        asin = itemDom.xpath("@data-asin")
                        if (asin):
                            item['asin'] = asin[0]
                        else:
                            continue
                    except:
                        print ("asin error")

                    # 标题 title
                    try:
                        title = itemDom.xpath("div//*[contains(@class, 's-access-detail-page')]/h2/text()")
                        if (title):
                            item['title'] = title[0]
                    except:
                        print ("title error")

                    # 图片 images
                    try:
                        try:
                            image = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@src")
                            if (image):
                                item['image'] = Model_Processor().formatImage(image[0])
                        except:
                            print ("image error")
                        # 宽度
                        try:
                            width = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@width")
                            if (width):
                                item['width'] = width[0]
                        except:
                            print ("width error")

                        # 高度
                        try:
                            height = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@height")
                            if (height):
                                item['height'] = height[0]
                        except:
                            print ("height error")
                    except:
                        print ("images error")
                    # bestsellerDom
                    try:
                        bestsellerDom = itemDom.xpath("div//*[contains(@class, 'sx-badge-rectangle')]/span/text()")
                        if (bestsellerDom):
                            if (bestsellerDom[0] == "Best Seller"):
                                bestseller_node_id = itemDom.xpath(
                                    "div//*[contains(@class, 'sx-badge-region')]/div/a/@href")
                                if (bestseller_node_id):
                                    bestseller_id = bestseller_node_id[0].strip().split("bestsellers/")[1].strip().split("/")[1].strip()
                                    if (bestseller_id.isdigit()):
                                        item['bestseller_node_id'] = bestseller_id
                                        # print (item['bestseller_node_id'])
                    except:
                        print ("bestseller error")

                    # fba
                    # 一般产品的xpath
                    try:
                        fba = itemDom.xpath("div//*[contains(@class, 'a-icon-premium')]/span/text()")
                        if (fba):
                            if (fba[0].strip() == "Premium"):
                                item['is_fba'] = "1"
                            else:
                                item['is_fba'] = "0"
                        else:
                            item['is_fba'] = "0"
                    except:
                        print ("fba error")

                    # 价格 price
                    try:
                        price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/@aria-label")
                        if (price):
                            if (Model_Processor().formatNumber(price[0], "es").isdigit()):
                                item['price'] = Model_Processor().formatNumber(price[0], "es")
                        else:
                            price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/text()")
                            if (price):
                                if (Model_Processor().formatNumber(price[0], "es").isdigit()):
                                    item['price'] = Model_Processor().formatNumber(price[0], "es")
                            else:
                                price = itemDom.xpath("div//*[contains(@class, 's-price')]/text()")
                                if (price):
                                    if (Model_Processor().formatNumber(price[0], "es").isdigit()):
                                        item['price'] = Model_Processor().formatNumber(price[0], "es")
                                else:
                                    price = itemDom.xpath("div//*[contains(@class, 'a-size-base a-color-price a-text-bold')]/text()")
                                    if (price):
                                        if (Model_Processor().formatNumber(price[0], "es").isdigit()):
                                            item['price'] = Model_Processor().formatNumber(price[0], "es")
                    except:
                        print ("price error")

                    # 原价 list_price
                    try:
                        list_price = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
                        if (list_price):
                            if (Model_Processor().formatNumber(list_price[0], "es").isdigit()):
                                item['list_price'] = Model_Processor().formatNumber(list_price[0], "es")
                    except:
                        print ("list_price error")

                    # 评级 rating a-icon-star
                    try:
                        rating = itemDom.xpath("div//i[contains(@class, 'a-icon-star')]/span/text()")
                        if (rating):
                            item['rating'] = Model_Processor().formatRating(rating[0], "es")
                    except:
                        print ("rating error")

                    # 评论数 review_count //*[@id="result_0"]/div/div[3]/div[3]/a
                    try:
                        review_count = itemDom.xpath("div//*[contains(@class, 'a-span5')]/div/a/text()")
                        if (review_count):
                            count = Model_Processor().formatNumber(review_count[0], "es")
                            if (count.isdigit()):
                                item['review_count'] = count
                        else:
                            review_count = itemDom.xpath("div//*[contains(@class, 'a-spacing-top-mini')]/a/text()")
                            if (review_count):
                                count = Model_Processor().formatNumber(review_count[0], "es")
                                if (count.isdigit()):
                                    item['review_count'] = count
                    except:
                        print ("review_count error")

                    # print (item)
                    data.append(item)

            # 处理右侧广告
            try:
                rightTitleDom = tree.xpath("//*[@id='paRightContent']//h1/text()")
                if (rightTitleDom):
                    if (rightTitleDom[0].strip() == "Sponsored"):
                        rightListDom = tree.xpath("//*[@id='paRightContent']//*[contains(@class, 'pa-ad-details')]")
                        if (rightListDom):
                            sponsor_position = 1
                            for itemDom in rightListDom:
                                item = {'sponsor': 1, 'sponsor_position_type': 'right', 'page_id': page_id, 'page_position': page_position, 'sponsor_position': sponsor_position}
                                page_position += 1
                                sponsor_position += 1
                                # 获取广告ASIN
                                linkDoms = itemDom.xpath("div/a/@href")
                                if (linkDoms):
                                    for linkDom in linkDoms:
                                        item['asin'] = linkDom.split("%2F")[4]
                                        # if not item['asin']:
                                        # //*[@id="desktop-rhs-carousels_click_within_right"]/div/div[3]/div[2]/div[3]/a[1]
                                    if not item['asin']:
                                        linkDoms = itemDom.xpath("div/div['a-section']/a")
                                        if (linkDoms):
                                            # for linkDom in linkDoms:
                                            if (linkDom.text):
                                                item['review_count'] = linkDom.text
                                                item['asin'] = linkDom.xpath("@href")[0].split("/")[4]
                                    else:
                                        # 获取评论数
                                        review_countDom = itemDom.xpath("div/div['a-section']/a[2]/text()")
                                        if (review_countDom):
                                            item['review_count'] = Model_Processor().formatNumber(review_countDom[0], "es")
                                            # print (review_countDom[0])
                                            # item['review_count']
                                # 获取广告图片
                                try:
                                    imageDom = itemDom.xpath("div//*[@alt='Product Details']/@src")
                                    if (imageDom):
                                        item['image'] = Model_Processor().formatImage(imageDom[0])
                                except:
                                    print ("ad image error")
                                # 获取广告标题
                                try:
                                    titleDom = itemDom.xpath("div['a-section']/div/a/@title")
                                    if (titleDom):
                                        item['title'] = titleDom[0]
                                except:
                                    print ("ad title error")
                                # 获取广告价格
                                try:
                                    priceDom = itemDom.xpath("div//*/@aria-label")
                                    if (priceDom):
                                        if (Model_Processor().formatNumber(priceDom[0], "es").isdigit()):
                                            item['price'] = Model_Processor().formatNumber(priceDom[0], "es")
                                except:
                                    print ("ad price error")
                                # 获取广告原价
                                try:
                                    list_priceDom = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
                                    if (list_priceDom):
                                        if (Model_Processor().formatNumber(list_priceDom[0], "es").isdigit()):
                                            item['list_price'] = Model_Processor().formatNumber(list_priceDom[0], "es")
                                except:
                                    print ("ad list_price error")
                                # 获取rating a-icon-star
                                try:
                                    ratingDom = itemDom.xpath("div//*[contains(@class, 'a-icon-star')]/span/text()")
                                    if (ratingDom):
                                        item['rating'] = Model_Processor().formatRating(ratingDom[0], "es")
                                except:
                                    print ("ad rating error")
                                # print (item)
                                data.append(item)
            except:
                print ("right ad error")
            #计算总数
            totalDom = tree.xpath("//*[@id='s-result-count']/text()")
            if (totalDom):
                # 总数 >1
                # print (totalDom[0].split(" "))
                try:
                    total = Model_Processor().formatNumber(totalDom[0].split("de")[1].strip().split("resultados")[0].replace(".", "").strip(), "es")
                except:
                    total = Model_Processor().formatNumber(totalDom[0].split(" ")[0], "es")
                if (total.isdigit()):
                    total = {"total": total}
                    data.append(total)
                else:
                    # 总数 ==1
                    total = Model_Processor().formatNumber(totalDom[0].split(" ")[0], "es")
                    if (total.isdigit()):
                        total = {"total": total}
                        data.append(total)
                # print (Model_Processor().formatNumber(totalDom[0].split(" ")[2]))
            else:
                # 总数为0 //*[@id="noResultsTitle"]/span[1]
                totalDom = tree.xpath("//*[@id='noResultsTitle']//span/text()")
                if (totalDom):
                    if (totalDom[0] == "0" and totalDom[1] == "resultado"):
                        print totalDom[0]
                        print totalDom[1]
                        total = {"total": "0"}
                        data.append(total)
        except Exception as err:
            print (err)
        # print (len(data)-1)
        # print (data[-1])
        if (len(data)>0):
            return data