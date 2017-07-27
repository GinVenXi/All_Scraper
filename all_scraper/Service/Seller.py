#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-25'
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
from Models.Keys import Model_Keys
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.AmazonProduct import Model_Mapper_AmazonProduct
from Models.Mapper.AmazonProductImage import Model_Mapper_AmazonProductImage
from Models.Mapper.AmazonSeller import Model_Mapper_AmazonSeller
from Models.Mapper.AmazonSellerProduct import Model_Mapper_AmazonSellerProduct
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Mapper.Scrape import Model_Mapper_Scrape
from Models.Scraper.Seller.Base import Model_Scraper_Seller_Base
from Models.Scraper.Seller.Product import Model_Scraper_Seller_Product
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Models.Static.Region import Model_Static_Region
from Service.Abstract import Service_Abstract

class Service_Seller(Service_Abstract):
    def __init__(self):
        super(Service_Seller, self).__init__()
        self.amazonSellerMapper = Model_Mapper_AmazonSeller()
        self.amazonProductMapper = Model_Mapper_AmazonProduct()
        self.amazonSellerProductMapper = Model_Mapper_AmazonSellerProduct()
        self.amazonProductImageMapper = Model_Mapper_AmazonProductImage()

    def getAmazonSellerMapper(self):
        return self.amazonSellerMapper

    def getAmazonProductMapper(self):
        return self.amazonProductMapper

    def getAmazonSellerProductMapper(self):
        return self.amazonSellerProductMapper

    def getAmazonProductImageMapper(self):
        return self.amazonProductImageMapper

    def scrape(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            region = Model_Static_Region()
            reg = region.getText(self.region)
            merchant_id = downloadQueue[4]
            self.scraper = Model_Scraper_Seller_Base(reg)
            data = self.scraper.scrape(merchant_id)

            # # 数据库连接
            # scrape = Model_Mapper_Scrape()
            # amazon = scrape.amazon
            # mapper = Model_Mapper_Scrape().mapper

            if (data):
                print (data)
                # 先查找数据库ASIN，若有则执行更新操作，若无则执行插入操作
                result = self.getAmazonSellerMapper().save_seller(reg, merchant_id, data)
                # sql = amazon.seller_select_sql_joint(reg, merchant_id)
                # result = mapper.select(sql)
                # if (result):
                #     sql = amazon.sellerinfo_update_sql_joint(reg, merchant_id, data)
                #     result = mapper.update(sql)
                # else:
                #     sql = amazon.sellerinfo_insert_sql_joint(reg, merchant_id, data)
                #     result = mapper.update(sql)
                if (result):
                    return Model_Static_DownloadQueue_Status.SCRAPED
                else:
                    return Model_Static_DownloadQueue_Status.FAILED
            else:
                # 若未抓出数据，进行相应操作
                return Model_Static_DownloadQueue_Status.FAILED
        except Exception as err:
            print (err)

    def scrapeProduct(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            region = Model_Static_Region()
            reg = region.getText(self.region)
            merchant_id = downloadQueue[4]
            self.scraper = Model_Scraper_Seller_Product(reg)
            results = self.scraper.scrape(merchant_id)
            if (results):
                # print (results)
                # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
                amazon = Model_Mapper_Amazon()
                # 连接数据库
                db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
                conn = db.connects()
                mapper = Model_Mapper_Mysql(conn)

                # 插入卖家产品信息前先将卖家信息插入卖家信息表
                self.getAmazonSellerMapper().save_productsseller(reg, merchant_id)
                # sql = amazon.seller_select_sql_joint(reg, merchant_id)
                # seller = mapper.select(sql)
                # if (seller):
                #     pass
                # else:
                #     sql = amazon.product_seller_insert_sql_joint(reg, merchant_id)
                #     mapper.insert(sql)

                # 插入卖家产品信息
                rank = 1
                # 更新排名前现将该店铺产品rank清空
                self.getAmazonSellerMapper().save_updaterank(reg, merchant_id)
                # sql = amazon.sellerproducts_rankupdate_sql_joint(reg, merchant_id)
                # mapper.update(sql)
                for items in results:
                    # print (result)
                    for item in items:
                        asin = item['asin']
                        sql = amazon.sellerproduct_select_sql_joint(reg, asin, merchant_id)
                        result = mapper.select(sql)
                        if (result):
                            sql = amazon.sellerproducts_update_sql_joint(reg, asin, merchant_id, rank, item)
                            result = mapper.update(sql)
                        else:
                            sql = amazon.sellerproducts_insert_sql_joint(reg, merchant_id, rank, item)
                            result = mapper.insert(sql)
                        if (result):
                            rank += 1
                        # 插入产品数据(amazon_product表)
                        sql = amazon.product_select_sql_joint(reg, asin)
                        result = mapper.select(sql)
                        if (result):
                            sql =  amazon.products_update_sql_joint(reg, asin, item)
                            result = mapper.update(sql)
                        else:
                            sql = amazon.products_insert_sql_joint(reg, asin, item)
                            result = mapper.insert(sql)
                        if (result):
                            # 插入图片数据(amazon_product_image表)
                            if (item['image']):
                                sql = amazon.product_image_select_sql_joint(reg, asin)
                                result = mapper.select(sql)
                                if (result):
                                    pass
                                else:
                                    sql = amazon.product_image_insert_sql_joint(reg, asin, item)
                                    mapper.insert(sql)
                        conn.close()
                        if (result):
                            return Model_Static_DownloadQueue_Status.SCRAPED
                        else:
                            return Model_Static_DownloadQueue_Status.FAILED
            else:
                return Model_Static_DownloadQueue_Status.FAILED
        except Exception as err:
            print (err)


    def getAmazonSellerUploadData(self, region, merchant_id, includeProducts=False):
        try:
            # 数据库连接
            scrape = Model_Mapper_Scrape()
            amazon = scrape.amazon
            mapper = Model_Mapper_Scrape().mapper
            sql = amazon.seller_select_sql_joint(region, merchant_id)
            data = list(mapper.select(sql))
            seller_key = Model_Keys.seller_key
            data = dict(zip(seller_key, data[0]))
            if (data):
                if (includeProducts):
                    sql = amazon.sellerproducts_select_sql_joint(region, merchant_id)
                    sellerProducts = mapper.select(sql)
                    if (sellerProducts):
                        sellerProducts_list = []
                        sellerProducts_key = Model_Keys.sellerProducts_key
                        for sellerProduct in sellerProducts:
                            sellerProducts_list.append(dict(zip(sellerProducts_key, sellerProduct)))
                        data['seller_products'] = sellerProducts_list
                return data
            return False
        except Exception as err:
            print (err)