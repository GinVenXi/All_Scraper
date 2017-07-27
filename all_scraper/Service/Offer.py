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
from Models.Mapper.AmazonProduct import Model_Mapper_AmazonProduct
from Models.Mapper.AmazonProductImage import Model_Mapper_AmazonProductImage
from Models.Mapper.AmazonSeller import Model_Mapper_AmazonSeller
from Models.Mapper.AmazonSellerProduct import Model_Mapper_AmazonSellerProduct
from Models.Mapper.AmazonSellerProductOffer import Model_Mapper_AmazonSellerProductOffer
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Abstract import Service_Abstract
from Models.Static.DownloadQueue.Type import Model_Static_DownloadQueue_Type
from Models.Static.Region import Model_Static_Region
from Models.Scraper.Product.offer import Model_Scraper_Product_Offer
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql

class Service_Offer(Service_Abstract):
    def __init__(self):
        super(Service_Offer, self).__init__()
        self.amazonProductMapper = Model_Mapper_AmazonProduct()
        self.amazonProductImageMapper = Model_Mapper_AmazonProductImage()
        self.amazonSellerMapper = Model_Mapper_AmazonSeller()
        self.amazonSellerProductMapper = Model_Mapper_AmazonSellerProduct()
        self.amazonSellerProductOfferMapper = Model_Mapper_AmazonSellerProductOffer()

    def getAmazonSellerProductOfferMapper(self):
        return self.amazonSellerProductOfferMapper

    def getAmazonSellerMapper(self):
        return self.amazonSellerMapper

    def getAmazonSellerProductMapper(self):
        return self.amazonSellerProductMapper

    def scrape(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            self.type = downloadQueue[3]
            self.value = downloadQueue[4].encode('utf-8')
            region = Model_Static_Region()
            reg = region.getText(self.region)
            type = self.type
            asin = self.value
            if (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
                self.offerScraper = Model_Scraper_Product_Offer(reg)
                data = self.offerScraper.scrape(asin)
            # 操作scrape表，写入抓取日志
            if (self.offerScraper.hasScrapes()):
                # 执行写入操作
                try:
                    self.saveScrapes(self.offerScraper.getScrapes(), downloadQueue)
                except:
                    pass
            scrapeSuccess = False
            if(data):
                scrapeSuccess = True
                for index in range(len(data)):
                    for items in data[index]:
                        # print (items)
                        if (items['seller_id'] != ''):
                            # 插入amazon_seller_product_offer表
                            try:
                                if (items['item_id']):
                                    self.getAmazonSellerProductOfferMapper().save(reg, asin, items)
                            except Exception as err:
                                print (err)
                            # 插入amazon_seller表
                            try:
                                self.getAmazonSellerMapper().save(reg, items)
                            except Exception as err:
                                print (err)
                            # 插入amazon_seller_product表
                            try:
                                self.getAmazonSellerProductMapper().save(reg, asin, items)
                            except Exception as err:
                                print (err)
                        else:
                            continue
                if (scrapeSuccess):
                    return Model_Static_DownloadQueue_Status.SCRAPED
                else:
                    return Model_Static_DownloadQueue_Status.FAILED
            elif (data == False):
                return Model_Static_DownloadQueue_Status.SCRAPED_WRONG
            else:
                return Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA
        except Exception as err:
            print (err)
            return Model_Static_DownloadQueue_Status.FAILED
