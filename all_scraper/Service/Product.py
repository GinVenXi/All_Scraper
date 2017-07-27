#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import sys
from Models.Keys import Model_Keys
from Models.Mapper.AmazonProduct import Model_Mapper_AmazonProduct
from Models.Mapper.MobileKeywords import Model_Mapper_MobileKeywords
from Models.Mapper.MobileUploadQueue import Model_Mapper_MobileUploadQueue
from Models.Mapper.Scrape import Model_Mapper_Scrape
from Models.Mapper.AmazonProductImage import Model_Mapper_AmazonProductImage
from Models.Scraper.Mobile_Product.Base import Model_Scraper_Mobile_Product_Base
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Abstract import Service_Abstract
from Models.Scraper.Product.Base import Model_Scraper_Product_Base
from Models.Scraper.Product.offer import Model_Scraper_Product_Offer
from Models.Static.Region import Model_Static_Region
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql

class Service_Product(Service_Abstract):
    def __init__(self):
        super(Service_Product, self).__init__()
        # self.amazon = Model_Mapper_Scrape().amazon
        self.amazonProductMapper = Model_Mapper_AmazonProduct()
        self.amazonProductImageMapper = Model_Mapper_AmazonProductImage()
        self.uploadMobileQueueMapper = Model_Mapper_MobileUploadQueue()
        self.mobilekeywordsMapper = Model_Mapper_MobileKeywords()

    def getAmazonProductMapper(self):
        return self.amazonProductMapper

    def getAmazonProductImageMapper(self):
        return self.amazonProductImageMapper

    def scrape(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            self.type = downloadQueue[3]
            self.value = downloadQueue[4].encode('utf-8')
            region = Model_Static_Region()
            reg = region.getText(self.region)
            asin = self.value
            self.scraper = Model_Scraper_Product_Base(reg)
            data = self.scraper.scrape(asin)
            # 操作scrape表，写入抓取日志
            if (self.scraper.hasScrapes()):
                try:
                    # 执行写入操作
                    self.saveScrapes(self.scraper.getScrapes(), downloadQueue)
                except:
                    pass
            position = 0
            scrapeSuccess = False
            if(data):
                # print (data)
                scrapeSuccess = True
                # 表amazon_product
                result = self.getAmazonProductMapper().save(reg, asin, data)

                # 表amazon_product_images
                if (result):
                    for i in data['images']:
                        try:
                            self.getAmazonProductImageMapper().save(reg, asin, i, position)
                            position += 1
                        except Exception as err:
                            print (err)
                if (scrapeSuccess):
                    return Model_Static_DownloadQueue_Status.SCRAPED
                else:
                    return Model_Static_DownloadQueue_Status.FAILED
            elif (data == False):
                return Model_Static_DownloadQueue_Status.SCRAPED_WRONG
            else:
                # 若未抓出数据，进行相应操作
                return Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA

        except Exception as err:
            print (err)
            return Model_Static_DownloadQueue_Status.FAILED

    def mobile_scrape(self, mobiledownloadQueue):
        try:
            region = Model_Static_Region()
            self.region = mobiledownloadQueue[2]
            reg = region.getText(self.region)
            keywords = mobiledownloadQueue[4].encode('utf-8')
            self.scraper = Model_Scraper_Mobile_Product_Base(reg)
            data = self.scraper.scrape(reg, keywords)
            scrapeSuccess = False
            if (data[-1]["total"] > 0):
                scrapeSuccess = True
                # 存储产品基本信息
                for index in range(len(data) - 1):
                    for page_data in data[index]:
                        try:
                            result = self.amazonProductMapper.saveFromKeywordsProduct(reg, page_data)
                            if (result):
                                # 插入或更新图片信息0-
                                try:
                                    asin = page_data['asin']
                                    if (page_data['image']):
                                        self.amazonProductImageMapper.save_img(reg, asin, page_data)
                                    self.uploadMobileQueueMapper.save(self.region, 0, asin)
                                except Exception as err:
                                    print (err)
                        except Exception as err:
                            print (err)
                # 存储关键词基本信息
                try:
                    self.mobilekeywordsMapper.save(reg, keywords, str(data[-1]["total"]))
                except:
                    print ("Mobile_Keywords insert error")
                if (scrapeSuccess):
                    return Model_Static_DownloadQueue_Status.SCRAPED
                    # 更改队列状态
                else:
                    return Model_Static_DownloadQueue_Status.FAILED
            else:
                return Model_Static_DownloadQueue_Status.FAILED
        except Exception as err:
            print (err)

    # 获取指定ASIN的amazonProduct数据和sellerProduct数据

    def getAmazonProductUploadData(self, region, asin, type):
        scrape = Model_Mapper_Scrape()
        amazon = scrape.amazon
        mapper = Model_Mapper_Scrape().mapper
        # 查询产品
        sql = amazon.product_select_sql_joint(region, asin)
        data = list(mapper.select(sql))
        key = Model_Keys.product_key
        try:
            data = dict(zip(key, data[0]))
        except Exception as err:
            print (err)
            return False
        if (data):
            # print (data)
            # 查询图片
            sql = amazon.product_uploadimage_select_sql_joint(region, asin)
            images = mapper.select(sql)
            image_key = Model_Keys.image_key
            images_list = []
            for image in images:
                images_list.append(dict(zip(image_key, image)))
            data['image'] = images_list
            if (type == 'OFFER'):
                sql = amazon.SellerProduct_upload_select_sql_joint(region, asin)
                sellerProducts = mapper.select(sql)
                if (sellerProducts):
                    sellerProducts_list = []
                    sellerProducts_key = Model_Keys.sellerProducts_key
                    for sellerProduct in sellerProducts:
                        sellerProducts_list.append(dict(zip(sellerProducts_key, sellerProduct)))
                    # data['seller_products'] = sellerProducts
                    data['seller_products'] = sellerProducts_list
                sql = amazon.SellerProductOffer_upload_select_sql_joint(region, asin)
                sellerProductOffers = mapper.select(sql)
                if (sellerProductOffers):
                    # print (sellerProductOffers)
                    sellerProductOffers_list = []
                    sellerProductOffers_key = Model_Keys.sellerProductOffers_key
                    for sellerProductOffer in sellerProductOffers:
                        sellerProductOffers_list.append(dict(zip(sellerProductOffers_key, sellerProductOffer)))
                    # data['seller_product_offers'] = sellerProductOffers
                    data['seller_product_offers'] = sellerProductOffers_list
            # print (data)
            return data
        return False