#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-24'
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

class Model_Processor_MobileProduct_Base_Com(Model_Processor):

    def mobile_process(self, region, data):
        try:
            result = []
            for i in data['results']['sections'][0]['items']:
                item = {}
                try:
                    item['asin'] = i['asin']
                    # print (i['asin'])
                except:
                    continue
                try:
                    item['parent_asin'] = i['parentAsin']
                    # print (i['parentAsin'])
                except:
                    pass
                    # try:
                    #     item['group'] = i['group']
                    #     # print (i['group'])
                    # except:
                    pass
                try:
                    item['title'] = i['title']
                    # print (i['title'])
                except:
                    pass
                # try:
                #     item['truncatedTitle'] = i['truncatedTitle']
                #     # print (i['truncatedTitle'])
                # except:
                #     pass
                try:
                    item['decorations'] = i['decorations']
                    # print (i['decorations'])
                except:
                    pass
                try:
                    description = []
                    for j in i['description']:
                        if (j['text'].replace("\n", "").strip() != ""):
                            description.append(j['text'].replace("\n", "").strip())
                    item['description'] = " ".join(description)
                    # print (item['description'])
                except:
                    pass
                # try:
                #     item['brandName'] = i['brandName']
                #     # print (i['brandName'])
                # except:
                #     pass
                # try:
                #     item['offerId'] = i['offerId']
                #     # print (i['offerId'])
                # except:
                #     pass
                try:
                    item['image'] = self.formatImage(i['image']['url'])
                    # print (i['image']['url'])
                except:
                    pass
                try:
                    list_price = self.formatNumber(i['prices']['buy']['listPrice'].encode("utf-8"), region)
                    if (list_price.isdigit()):
                        item['list_price'] = self.formatNumber(i['prices']['buy']['listPrice'].encode("utf-8"), region)
                        # print (item['list_price'])
                except:
                    pass
                try:
                    price = self.formatNumber(i['prices']['buy']['price'].encode("utf-8"), region)
                    # print (type(price))
                    if (price.isdigit()):
                        item['price'] = self.formatNumber(i['prices']['buy']['price'].encode("utf-8"), region)
                        # print (item['price'])
                except:
                    try:
                        price = self.formatNumber(i['prices']['buy']['price'].encode("utf-8"), region)
                        if (price.isdigit()):
                            item['price'] = self.formatNumber(i['prices']['usedAndNewOffers']['price'].encode("utf-8"),
                                                              region)
                            # print (item['price'])
                    except:
                        pass
                try:
                    item['offer_count'] = str(i['prices']['usedAndNewOffers']['offerCount'])
                    # print (item['offer_count'])
                except:
                    pass
                try:
                    item['review_count'] = i['ratings']['count']
                    # print (i['ratings']['count'])
                except:
                    pass
                try:
                    item['rating'] = i['ratings']['rating']
                    # print (i['ratings']['rating'])
                except:
                    pass
                try:
                    shipping = []
                    for j in i['shipping']['priceLabel']:
                        shipping.append(j['text'])
                    item['shipping'] = " ".join(shipping)
                    # print (item['shipping'])
                    # print (i['shipping']['priceLabel'][0]['text'])
                except:
                    try:
                        shipping = []
                        for j in i['shipping']['sss']:
                            shipping.append(j['text'])
                        item['shipping'] = " ".join(shipping)
                        # print (item['shipping'])
                        # print (i['shipping']['sss'][0]['text'])
                    except:
                        pass
                try:
                    item['seller_id'] = i['merchant']['id']
                    # print (i['merchant']['id'])
                except:
                    pass
                try:
                    item['seller_name'] = i['merchant']['displayName']
                    # print (i['merchant']['displayName'])
                except:
                    pass
                # print (item)
                result.append(item)
            return result
        except Exception as err:
            print (err)