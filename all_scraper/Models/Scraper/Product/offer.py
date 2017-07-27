#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-20'
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
from Models.Scraper.Standard import Model_Scraper_Standard
from Models.Static.Scrape.Status import Model_Static_Scrape_Status
from Models.Processor.Product.offer import Model_Processor_Product_Offer
from Service.Functions import Service_Functions
from Models.Downloader_Method import Model_Downloader_Method
from pyvirtualdisplay import Display


class Model_Scraper_Product_Offer(Model_Scraper_Standard):
    def __init__(self, region):
        super(Model_Scraper_Product_Offer, self).__init__(region)
        self.region = region
        self.processor = Service_Functions().getProcessor('Product_Offer', region)
        self.processorInventory = Model_Processor_Product_Offer()

    # 处理首页OfferList
    def process(self, url):
        self.processOffer = Model_Scraper_Standard(self.region)
        content = self.processOffer.processOffer(url)
        if(content):
            return (content)
        else:
            return False

    def processInventory(self, url, fields):
        urls = []
        for i in range(self.len):
            urls.append(
                "OfferListingId." + str(i + 1) + "=" + fields["OfferListingId." + str(i + 1)] + "&Quantity." + str(
                    i + 1) + "=" + str(fields["Quantity." + str(i + 1)]) + "&ASIN." + str(i + 1) + "=" + fields[
                    "ASIN." + str(i + 1)])
            # print ("OfferListingId."+str(i+1)+"="+fields["OfferListingId."+str(i+1)]+"&Quantity."+str(i+1)+"="+str(fields["Quantity."+str(i+1)])+"&ASIN."+str(i+1)+"="+fields["ASIN."+str(i+1)])
        url = url + "&".join(urls) + "&SessionId=" + fields["SessionId"] #+ "&ConfirmPage=" + fields["ConfirmPage"]
        # print (url)
        # url1 = "https://www.amazon.com/gp/aws/cart/add.html?OfferListingId.1=S6IsVPoZdOcW%2FKYrN3LS3x0lD3Tz%2BC4LzWH5iGHsSjGyvMAjoCJFoM2T9MTkkdGA6ZHGyVQL3%2FGKLAhBIKPS07xeSwh9I5sfC1SI42wEh10xQplkbhROZJwFJQ0kaEsgAw9UwsZ6RPDpiOXczsn2XA%3D%3D&Quantity.1=999&ASIN.1=B06WRVKB1H&OfferListingId.2=W2%2FalqZrKcrwrpZF0C7OVXi8RhnDXQFtCNPmKTxF2S9dZxhXecAXmcCy2SLeVtrsoEtGL0v1hJlLbSOoOjZDA2%2FMAYlIcpB0JUxFVuQNR1BC4Qa9gLZlKjkMIlRGGt52r6sK8Jxod2c3wakZSer9gx3A%2FYFeI%2B57&Quantity.2=999&ASIN.2=B00YD548Q0"
        self.Inventory = Model_Scraper_Standard(self.region)
        content = self.Inventory.processInventory(url)
        if (content):
            return (content)

    def scrapeInventory(self, asin, data):
        self.len = len(data)
        if (data == '' or data == None):
            return Model_Static_Scrape_Status.FAILED
        url ="https://www.amazon."+self.region+"/gp/aws/cart/add.html?"
        fields = {}
        session_id = None
        index = 1
        for item in data:
            if (item['session_id']):
                session_id = item['session_id']
            if (item['offering_id']):
                fields['ASIN.' + str(index)] = asin
                # 填写数量要视情况而定
                fields['Quantity.' + str(index)] = 999
                fields['OfferListingId.' + str(index)] = item['offering_id']
                index += 1
        if not fields:
            return Model_Static_Scrape_Status.FAILED
        if not session_id:
            return Model_Static_Scrape_Status.FAILED
        fields['SessionId'] = session_id
        fields['ConfirmPage'] = 'confirm'
        try:
            content = self.processInventory(url, fields)
        except Exception as err:
            print (err)
        if (content):
            result = self.processorInventory.processInventory(content.encode('utf-8'))
            return result
        else:
            return Model_Static_Scrape_Status.FAILED

    def scrape(self, asin):
        url = "https://www.amazon." + self.region + "/gp/offer-listing/" + asin
        print (url)
        try:
            content = self.process(url)
        except Exception as err:
            print (err)
        try:
            result = []
            if(content):
                # 这边写解析代码, 通过解析返回的数据再进行库存的抓取
                # Model_Processor_Product_Offer_Com
                data = self.processor.process(content.encode('utf-8'))
                if(data):
                    # print (data)
                    # 通过解析得到的数据进行库存的计算
                    try:
                        Inventory = self.scrapeInventory(asin, data)
                    # print (Inventory)
                    except Exception as err:
                        print (err)
                    # 将offer数据与库存数据结合
                    try:
                        # print (Inventory)
                        result.append(Service_Functions().mergeDict(data, Inventory))
                    except Exception as err:
                        print (err)
                pageCount = self.processor.getPageCount(content)
                # print (pageCount)
            else:
                pageCount = 0
            if (pageCount > 1):
                for i in range(2, int(pageCount) + 1):
                    index = str((i - 1) * 10)
                    pageUrl = "http://www.amazon." + self.region + "/gp/offer-listing/" + asin + "/ref=olpOffersSuppressed?ie=UTF8&f_new=true&overridePriceSuppression=1&startIndex=" + index
                    # print (pageUrl)
                    pageContent = self.process(pageUrl)
                    if (pageContent):
                        pageResult = self.processor.process(pageContent.encode('utf-8'))
                        if (pageResult):
                            # print (pageResult)
                            pageInventory = self.scrapeInventory(asin, pageResult)
                            # print (pageInventory)
                            try:
                                result.append(Service_Functions().mergeDict(pageResult, pageInventory))
                            except Exception as err:
                                print (err)
            return result
        # except Exception as err:
        #     print (err)
        except:
            return False