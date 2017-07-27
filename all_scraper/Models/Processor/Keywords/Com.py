#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.processor import Model_Processor
from lxml import etree
import bs4
import sys
import time
'''
#############################################################
解析函数(主要针对关键词页)
#############################################################
'''
class Model_Processor_Keywords_Com(Model_Processor):

    def process(self, html, page_id=1):

        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.com"
            sys.exit()

        tree = etree.HTML(html)
        data = []
        # https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=handbags
        try:
            # 处理中间产品
            # listDom1 = tree.xpath('//*[@id="atfResults"]/ul/li')
            # listDom2 = tree.xpath('//*[@id="btfResults"]/ul/li')
            listDoms = tree.xpath("//*[@class='a-row s-result-list-parent-container']/ul/li")
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
                        # print (item['asin'])
                    except:
                        print ("asin error")

                    # 标题 title
                    try:
                        title = itemDom.xpath("div//*[contains(@class, 's-access-detail-page')]/h2/text()")
                        if (title):
                            item['title'] = title[0]
                            # print (title[0])
                    except:
                        print ("title error")

                    # 图片 images
                    try:
                        try:
                            image = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@src")
                            if (image):
                                item['image'] = Model_Processor().formatImage(image[0])
                            # print (item['image'])
                        except:
                            print ("image error")
                        # 宽度
                        try:
                            width = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@width")
                            if (width):
                                item['width'] = width[0]
                            # print (item['width'])
                        except:
                            print ("width error")

                        # 高度
                        try:
                            height = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@height")
                            if (height):
                                item['height'] = height[0]
                                # print (item['height'])
                        except:
                            print ("height error")
                    except:
                        print ("images error")
                        # bestsellerDom
                    try:
                        bestsellerDom = itemDom.xpath("div//*[contains(@class, 'sx-badge-rectangle')]/span/text()")
                        if (bestsellerDom):
                            if (bestsellerDom[0] == "Best Seller"):
                                bestseller_node_id = itemDom.xpath("div//*[contains(@class, 'sx-badge-region')]/div/a/@href")
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
                        fba = itemDom.xpath("div//*[contains(@class, 'a-icon-prime')]/span/text()")
                        if (fba):
                            if (fba[0].strip() == "Prime"):
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
                            if (Model_Processor().formatNumber(price[0], "com").isdigit()):
                                item['price'] = Model_Processor().formatNumber(price[0], "com")
                        else:
                            price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/text()")
                            if (price):
                                if (Model_Processor().formatNumber(price[0], "com").isdigit()):
                                    item['price'] = Model_Processor().formatNumber(price[0], "com")
                            else:
                                price = itemDom.xpath("div//*[contains(@class, 's-price')]/text()")
                                if (price):
                                    if (Model_Processor().formatNumber(price[0], "com").isdigit()):
                                        item['price'] = Model_Processor().formatNumber(price[0], "com")
                    except:
                        print ("price error")

                    # 原价 list_price
                    try:
                        list_price = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
                        if (list_price):
                            if (Model_Processor().formatNumber(list_price[0], "com").isdigit()):
                                item['list_price'] = Model_Processor().formatNumber(list_price[0], "com")
                    except:
                        print ("list_price error")

                    # 评级 rating a-icon-star
                    try:
                        rating = itemDom.xpath("div//*[contains(@class, 'a-icon-star')]/span/text()")
                        if (rating):
                            item['rating'] = Model_Processor().formatRating(rating[0], "com")
                            # print item['rating']
                    except:
                        print ("rating error")

                    # 评论数 review_count //*[@id="result_0"]/div/div[3]/div[3]/a
                    try:
                        review_count = itemDom.xpath("div//*[contains(@class, 'a-span5')]/div/a/text()")
                        if (review_count):
                            count = Model_Processor().formatNumber(review_count[0], "com")
                            if (count.isdigit()):
                                item['review_count'] = count
                            # print (item['review_count'])
                        else:
                            review_count = itemDom.xpath("div//*[contains(@class, 'a-spacing-top-mini')]/a/text()")
                            if (review_count):
                                count = Model_Processor().formatNumber(review_count[0], "com")
                                if (count.isdigit()):
                                    item['review_count'] = count
                            else:
                                pass
                    except:
                        print ("review_count error")

                    # print (item)
                    data.append(item)

            # if (listDom1):
            #     page_position = 1
            #     sponsor_position = 1
            #     previous_sponsor_position_type = 'top'
            #     # print (len(listDom1))
            #     for itemDom in listDom1:
            #         item = {'sponsor': 0, 'page_id': page_id, 'page_position': page_position}
            #         # 标记为sponsor的产品 s-sponsored-list-header //*[@id="result_48"]/div/h5 //*[@id="result_24"]/div/div/div/div[a-fixed-left-grid-col a-col-right]/h5
            #         sponsorDom = itemDom.xpath("div//*[contains(@class, 's-sponsored-list-header')]/text()")
            #         # sponsorDom = soup.select(".s-sponsored-list-header")
            #         if (sponsorDom):
            #             item['sponsor'] = 1
            #         else:
            #             # a-color-tertiary
            #             sponsorDom = itemDom.xpath("div//h5[contains(@class, 'a-color-tertiary')]/text()")
            #             if (sponsorDom):
            #                 item['sponsor'] = 1
            #         if (item['sponsor'] == 1):
            #             if (page_position <= 4):
            #                 sponsor_position_type = 'top'
            #             else:
            #                 sponsor_position_type = 'bottom'
            #                 if (sponsor_position_type != previous_sponsor_position_type):
            #                     sponsor_position = 1
            #                     previous_sponsor_position_type = 'bottom'
            #             item['sponsor_position_type'] = sponsor_position_type
            #             item['sponsor_position'] = sponsor_position
            #             sponsor_position += 1
            #         page_position += 1
            #
            #         # asin
            #         try:
            #             asin = itemDom.xpath("@data-asin")
            #             if (asin):
            #                 item['asin'] = asin[0]
            #             # print (item['asin'])
            #         except:
            #             print ("asin error")
            #
            #         # 标题 title
            #         try:
            #             title = itemDom.xpath("div//*[contains(@class, 's-access-detail-page')]/h2/text()")
            #             if (title):
            #                 item['title'] = title[0]
            #                 # print (title[0])
            #         except:
            #             print ("title error")
            #
            #         # 图片 images
            #         try:
            #             try:
            #                 image = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@src")
            #                 if (image):
            #                     item['image'] = Model_Processor().formatImage(image[0])
            #                 # print (item['image'])
            #             except:
            #                 print ("image error")
            #             # 宽度
            #             try:
            #                 width = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@width")
            #                 if (width):
            #                     item['width'] = width[0]
            #                 # print (item['width'])
            #             except:
            #                 print ("width error")
            #
            #             # 高度
            #             try:
            #                 height = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@height")
            #                 if (height):
            #                     item['height'] = height[0]
            #                     # print (item['height'])
            #             except:
            #                 print ("height error")
            #         except:
            #             print ("images error")
            #             # bestsellerDom
            #         try:
            #             bestsellerDom = itemDom.xpath("div//*[contains(@class, 'sx-badge-rectangle')]/span/text()")
            #             if (bestsellerDom):
            #                 if (bestsellerDom[0] == "Best Seller"):
            #                     bestseller_node_id = itemDom.xpath("div//*[contains(@class, 'sx-badge-region')]/div/a/@href")
            #                     if (bestseller_node_id):
            #                         bestseller_id = bestseller_node_id[0].strip().split("bestsellers/")[1].strip().split("/")[1].strip()
            #                         if (bestseller_id.isdigit()):
            #                             item['bestseller_node_id'] = bestseller_id
            #                         # print (item['bestseller_node_id'])
            #         except:
            #             print ("bestseller error")
            #
            #         # fba
            #         # 一般产品的xpath
            #         try:
            #             fba = itemDom.xpath("div//*[contains(@class, 'a-icon-prime')]/span/text()")
            #             if (fba):
            #                 if (fba[0].strip() == "Prime"):
            #                     item['is_fba'] = "1"
            #                 else:
            #                     item['is_fba'] = "0"
            #             else:
            #                 item['is_fba'] = "0"
            #         except:
            #             print ("fba error")
            #
            #         # 价格 price
            #         try:
            #             price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/@aria-label")
            #             if (price):
            #                 if (Model_Processor().formatNumber(price[0], "com").isdigit()):
            #                     item['price'] = Model_Processor().formatNumber(price[0], "com")
            #             else:
            #                 price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/text()")
            #                 if (price):
            #                     if (Model_Processor().formatNumber(price[0], "com").isdigit()):
            #                         item['price'] = Model_Processor().formatNumber(price[0], "com")
            #                 else:
            #                     price = itemDom.xpath("div//*[contains(@class, 's-price')]/text()")
            #                     if (price):
            #                         if (Model_Processor().formatNumber(price[0], "com").isdigit()):
            #                             item['price'] = Model_Processor().formatNumber(price[0], "com")
            #         except:
            #             print ("price error")
            #
            #         # 原价 list_price
            #         try:
            #             list_price = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
            #             if (list_price):
            #                 if (Model_Processor().formatNumber(list_price[0], "com").isdigit()):
            #                     item['list_price'] = Model_Processor().formatNumber(list_price[0], "com")
            #         except:
            #             print ("list_price error")
            #
            #         # 评级 rating a-icon-star
            #         try:
            #             rating = itemDom.xpath("div//*[contains(@class, 'a-icon-star')]/span/text()")
            #             if (rating):
            #                 item['rating'] = Model_Processor().formatRating(rating[0], "com")
            #                 # print item['rating']
            #         except:
            #             print ("rating error")
            #
            #         # 评论数 review_count //*[@id="result_0"]/div/div[3]/div[3]/a
            #         try:
            #             review_count = itemDom.xpath("div//*[contains(@class, 'a-span5')]/div/a/text()")
            #             if (review_count):
            #                 count = Model_Processor().formatNumber(review_count[0], "com")
            #                 if (count.isdigit()):
            #                     item['review_count'] = count
            #                 # print (item['review_count'])
            #             else:
            #                 review_count = itemDom.xpath("div//*[contains(@class, 'a-spacing-top-mini')]/a/text()")
            #                 if (review_count):
            #                     count = Model_Processor().formatNumber(review_count[0], "com")
            #                     if (count.isdigit()):
            #                         item['review_count'] = count
            #                 else:
            #                     pass
            #         except:
            #             print ("review_count error")
            #
            #         # print (item)
            #         data.append(item)
            # # print (len(listDom2))
            # if (listDom2):
            #     page_position = page_position
            #     sponsor_position = 1
            #     previous_sponsor_position_type = 'top'
            #     for itemDom in listDom2:
            #         item = {'sponsor': 0, 'page_id': page_id, 'page_position': page_position}
            #         # 标记为sponsor的产品
            #         sponsorDom = itemDom.xpath("div//*[contains(@class, 's-sponsored-list-header')]/text()")
            #         # sponsorDom = soup.select("h5.s-sponsored-list-header")
            #         # print (sponsorDom)
            #         if (sponsorDom):
            #             item['sponsor'] = 1
            #         else:
            #             # a-color-tertiary
            #             sponsorDom = itemDom.xpath("div//h5[contains(@class, 'a-color-tertiary')]/text()")
            #             if (sponsorDom):
            #                 item['sponsor'] = 1
            #         if (item['sponsor'] == 1):
            #             if (page_position <= 4):
            #                 sponsor_position_type = 'top'
            #             else:
            #                 sponsor_position_type = 'bottom'
            #                 if (sponsor_position_type != previous_sponsor_position_type):
            #                     sponsor_position = 1
            #                     previous_sponsor_position_type = 'bottom'
            #             item['sponsor_position_type'] = sponsor_position_type
            #             item['sponsor_position'] = sponsor_position
            #             sponsor_position += 1
            #         page_position += 1
            #
            #         # asin
            #         try:
            #             asin = itemDom.xpath("@data-asin")
            #             if (asin):
            #                 item['asin'] = asin[0]
            #                 # print (item['asin'])
            #         except:
            #             print ("asin2 error")
            #
            #         # 标题 title
            #         try:
            #             title = itemDom.xpath("div//*[contains(@class, 's-access-detail-page')]/h2/text()")
            #             if (title):
            #                 item['title'] = title[0]
            #                 # print (title[0])
            #         except:
            #             print ("title2 error")
            #
            #         # 图片 images
            #         try:
            #             try:
            #                 image = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@src")
            #                 if (image):
            #                     item['image'] = Model_Processor().formatImage(image[0])
            #                     # print (item['image'])
            #             except:
            #                 print ("image2 error")
            #             # 宽度
            #             try:
            #                 width = itemDom.xpath("div//*[contains(@class, 's-access-image')]/@width")
            #                 if (width):
            #                     item['width'] = width[0]
            #                     # print (item['width'])
            #             except:
            #                 print ("image2 width error")
            #             # 高度
            #             try:
            #                 height = itemDom.xpath("//*[contains(@class, 's-access-image')]/@height")
            #                 if (height):
            #                     item['height'] = height[0]
            #                 # print (item['height'])
            #             except:
            #                 print ("image2 height error")
            #         except:
            #             print ("images2 error")
            #
            #         # Bestseller
            #         try:
            #             bestsellerDom = itemDom.xpath("div//*[contains(@class, 'sx-badge-rectangle')]/span/text()")
            #             if (bestsellerDom):
            #                 if (bestsellerDom[0] == "Best Seller"):
            #                     bestseller_node_id = itemDom.xpath(
            #                         "div//*[contains(@class, 'sx-badge-region')]/div/a/@href")
            #                     if (bestseller_node_id):
            #                         # /gp/bestsellers/electronics/2407761011/ref=sr_bs_19_2407761011_1
            #                         # /gp/bestsellers/electronics/12557637011/ref=sr_bs_25_12557637011_1
            #                         # /gp/bestsellers/electronics/15124502011/ref=sr_bs_27_15124502011_1
            #                         bestseller_id = bestseller_node_id[0].strip().split("bestsellers/")[1].strip().split("/")[1].strip()
            #                         if (bestseller_id.isdigit()):
            #                             item['bestseller_node_id'] = bestseller_id
            #                         # print (item['bestseller_node_id'])
            #         except:
            #             print ("bestseller2 error")
            #
            #         # fba
            #         try:
            #             fba = itemDom.xpath("div//*[contains(@class, 'a-icon-prime')]/span/text()")
            #             if (fba):
            #                 if (fba[0].strip() == "Prime"):
            #                     item['fba'] = 1
            #                     # print (item['fba'])
            #                 else:
            #                     item['fba'] = 0
            #             else:
            #                 item['fba'] = 0
            #         except:
            #             print ("fba2 error")
            #
            #         # 价格 price
            #         try:
            #             price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/@aria-label")
            #             if (price):
            #                 if (Model_Processor().formatNumber(price[0], "com").isdigit()):
            #                     item['price'] = Model_Processor().formatNumber(price[0], "com")
            #                 # print (item['price'])
            #             else:
            #                 price = itemDom.xpath("div//*[contains(@class, 'a-color-base')]/text()")
            #                 if (price):
            #                     if (Model_Processor().formatNumber(price[0], "com").isdigit()):
            #                         item['price'] = Model_Processor().formatNumber(price[0], "com")
            #         except:
            #             print ("price2 error")
            #
            #         # 原价 list_price
            #         try:
            #             list_price   = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
            #             if (list_price):
            #                 if (Model_Processor().formatNumber(list_price[0], "com").isdigit()):
            #                     item['list_price'] = Model_Processor().formatNumber(list_price[0], "com")
            #         except:
            #             print ("list_price2 error")
            #
            #         # 评级 rating
            #         try:
            #             rating = itemDom.xpath("div//*[contains(@class, 'a-icon-star')]/span/text()")
            #             if (rating):
            #                 item['rating'] = Model_Processor().formatRating(rating[0], "com")
            #                 # print item['rating']
            #         except:
            #             print ("rating2 error")
            #
            #         # 评论数 review_count
            #         try:
            #             review_count = itemDom.xpath("div//*[contains(@class, 'a-span5')]/div/a/text()")
            #             try:
            #                 if (review_count):
            #                     count = Model_Processor().formatNumber(review_count[0], "com")
            #                     if (count.isdigit()):
            #                         item['review_count'] = count
            #                     # print (item['review_count'])
            #                 else:
            #                     review_count = itemDom.xpath("div//*[contains(@class, 'a-spacing-top-mini')]/a/text()")
            #                     if (review_count):
            #                         count = Model_Processor().formatNumber(review_count[0], "com")
            #                         if (count.isdigit()):
            #                             item['review_count'] = count
            #             except Exception as err:
            #                 print (err)
            #         except:
            #             print ("review_count2 error")
            #
            #         # print (item)
            #         data.append(item)

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
                                            item['review_count'] = Model_Processor().formatNumber(review_countDom[0], "com")
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
                                        if (Model_Processor().formatNumber(priceDom[0], "com").isdigit()):
                                            item['price'] = Model_Processor().formatNumber(priceDom[0], "com")
                                except:
                                    print ("ad price error")
                                # 获取广告原价
                                try:
                                    list_priceDom = itemDom.xpath("div//*[contains(@class, 'a-text-strike')]/text()")
                                    if (list_priceDom):
                                        if (Model_Processor().formatNumber(list_priceDom[0], "com").isdigit()):
                                            item['list_price'] = Model_Processor().formatNumber(list_priceDom[0], "com")
                                except:
                                    print ("ad list_price error")
                                # 获取rating a-icon-star
                                try:
                                    ratingDom = itemDom.xpath("div//*[contains(@class, 'a-icon-star')]/span/text()")
                                    if (ratingDom):
                                        item['rating'] = Model_Processor().formatRating(ratingDom[0], "com")
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
                try:
                    total = Model_Processor().formatNumber(totalDom[0].split(" ")[2], "com")
                except:
                    total = Model_Processor().formatNumber(totalDom[0].split(" ")[0], "com")
                if (total.isdigit()):
                    total = {"total": total}
                    data.append(total)
                else:
                    # 总数 ==1
                    total = Model_Processor().formatNumber(totalDom[0].split(" ")[0], "com")
                    if (total.isdigit()):
                        total = {"total": total}
                        data.append(total)
                # print (Model_Processor().formatNumber(totalDom[0].split(" ")[2]))
            else:
                # 总数为0 //*[@id="noResultsTitle"]/span[1]
                totalDom = tree.xpath("//*[@id='noResultsTitle']/span/text()")
                if (totalDom):
                    if (totalDom[0] == "0" and totalDom[1] == "results"):
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
        else:
            listDom = tree.xpath("//*[@id='pagn']//span[@class='pagnLink']/a/text()")
            if (listDom):
                if (listDom[-1].isdigit()):
                    pageCount = listDom[-1]
        # print (pageCount)
        return (pageCount)