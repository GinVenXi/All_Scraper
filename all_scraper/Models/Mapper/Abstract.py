#!/usr/bin/env python
#--coding:utf-8-*-
'''
创建人： Javen
创建时间：2017/2/9
'''
import sys
from Models.DbTable.Abstract import Model_DbTable_Abstract

class Model_Mapper_Abstract(object):
    def __init__(self):
        self.dbTable = Model_DbTable_Abstract()
        self.mapper = self.dbTable.mapper
        self.amazon = self.dbTable.amazon
        self.conn = self.dbTable.db

    def findData(self, data=None, From=None, where=None, limit=None, offset=None, order=None):
        v = []
        if (where):
            for key, value in where.items():
                v.append('`%s` = "%s"' % (key, value))
            where = " and ".join(v)
        else:
            sql = "SELECT * FROM %s" % (From)
            # print (sql)
            results = self.mapper.select(sql)
            return results
        if (data == "all"):
            if (order):
                if (limit):
                    if (offset):
                        sql = 'SELECT * FROM %s WHERE %s ORDER BY %s LIMIT %s OFFSET %s' % (From, where, order, limit, offset)
                    else:
                        sql = 'SELECT * FROM %s WHERE %s ORDER BY %s LIMIT %s' % (From, where, order, limit)
                else:
                    sql = 'SELECT * FROM %s WHERE %s ORDER BY %s' % (From, where, order)
            else:
                if (limit):
                    if (offset):
                        sql = 'SELECT * FROM %s WHERE %s LIMIT %s OFFSET %s' % (From, where, limit, offset)
                    else:
                        sql = 'SELECT * FROM %s WHERE %s LIMIT %s' % (From, where, limit)
                else:
                    sql = 'SELECT * FROM %s WHERE %s' % (From, where)
        else:
            if (order):
                if (limit):
                    if (offset):
                        sql = 'SELECT %s FROM %s WHERE %s ORDER BY %s LIMIT %s OFFSET %s' % (data, From, where, order, limit, offset)
                    else:
                        sql = 'SELECT %s FROM %s WHERE %s ORDER BY %s LIMIT %s' % (data, From, where, order, limit)
                else:
                    sql = 'SELECT %s FROM %s WHERE %s ORDER BY %s' % (data, From, where, order)
            else:
                if (limit):
                    if (offset):
                        sql = 'SELECT %s FROM %s WHERE %s LIMIT %s OFFSET %s' % (data, From, where, limit, offset)
                    else:
                        sql = 'SELECT %s FROM %s WHERE %s LIMIT %s' % (data, From, where, limit)
                else:
                    sql = 'SELECT %s FROM %s WHERE %s' % (data, From, where)
        results = self.mapper.select(sql)
        return results

    def update(self, table=None, data=None, searchData=None):
        # 一般抓取时更新下载队列
        if (table == "download_queue"):
            id = searchData['id']
            sql = self.amazon.update_download_queue(id, data)
            result = self.mapper.update(sql)
        # 抓取评论时更新下载队列
        elif (table == "download_queue_review"):
            id = searchData['id']
            sql = self.amazon.update_download_queue_review(str(id), data)
            result = self.mapper.update(sql)
        # 移动端抓取时更新下载队列
        elif (table == "mobile_download_queue"):
            region = data["region"]
            type = data["type"]
            value = data["value"].strip()
            status = data["status"]
            scrape_count = data["scrape_count"]
            sql = self.amazon.update_mobile_download_queue(str(region), str(type), value, str(status), str(scrape_count))
            result = self.mapper.update(sql)
        # 抓取产品时更新产品表
        elif (table == "amazon_product"):
            region = searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.product_update_sql_joint(region, asin, data)
            result = self.mapper.update(sql)
        # 抓取产品时更新图片表
        elif (table == "amazon_product_images"):
            region = searchData["region"]
            asin = searchData["asin"]
            url = searchData["url"]
            sql = self.amazon.product_images_update_sql_joint(region, asin, url, data)
            result = self.mapper.update(sql)
        # 抓取关键词时更新关键词表
        elif (table == "keywords"):
            region = searchData["region"]
            keywords = searchData["name"]
            sql = self.amazon.keywordsObject_update_sql_joint(region, keywords, data)
            result = self.mapper.update(sql)
        # 移动端抓取关键词时更新移动关键词表
        elif (table == "mobile_keywords"):
            region = searchData["region"]
            keywords = searchData["name"]
            sql = self.amazon.mobilekeywordsObject_update_sql_joint(region, keywords, data)
            result = self.mapper.update(sql)
        # 一般抓取时更新上传队列表
        elif (table == "upload_queue"):
            region = data["region"]
            type = data["type"]
            asin = data["value"]
            sql = self.amazon.getUploadQueue_update_sql_joint(region, type, asin)
            result = self.mapper.update(sql)
        # 移动端抓取时更新上传队列表
        elif (table == "mobile_upload_queue"):
            region = data["region"]
            type = data["type"]
            asin = data["value"]
            sql = self.amazon.getMobileUploadQueue_update_sql_joint(region, type, asin)
            result = self.mapper.update(sql)
        # 抓取卖家产品时更新卖家offer表
        elif (table == "amazon_seller_product_offer"):
            region =  searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.offer_update_sql_joint(region, asin, data)
            result = self.mapper.update(sql)
        # 抓取卖家信息时更新卖家信息表
        elif (table == "amazon_seller"):
            region = searchData["region"]
            sql = self.amazon.seller_update_sql_joint(region, data)
            result = self.mapper.update(sql)
        # 抓取卖家产品时更新卖家产品信息表
        elif (table == "amazon_seller_product"):
            region = searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.sellerproduct_update_sql_joint(region, asin, data)
            result = self.mapper.update(sql)
        # 抓取seller时卖家表更新
        elif (table == "seller"):
            region = searchData["region"]
            seller_id = searchData["seller_id"]
            sql = self.amazon.sellerinfo_update_sql_joint(region, seller_id, data)
            result = self.mapper.update(sql)
        # 抓取seller产品时先重置产品排名
        elif (table == "productssellerrank"):
            region = data["region"]
            seller_id = data["seller_id"]
            sql = self.amazon.sellerproducts_rankupdate_sql_joint(region, seller_id)
            result = self.mapper.update(sql)
        # 抓取评论列表时
        elif (table == "amazon_product_review"):
            region = searchData['region']
            asin = searchData['asin']
            review_id = searchData['review_id']
            sql = self.amazon.productReview_update_sql_joint(region, asin, review_id, data)
            result = self.mapper.update(sql)
        # 抓取评论页图片信息(更新)
        elif (table == "amazon_product_review_image"):
            region = searchData['region']
            review_id = searchData['review_id']
            url = searchData['url']
            sql = self.amazon.productReviewImage_update_sql_joint(region, review_id, url, data)
            result = self.mapper.update(sql)
        # 抓取评论页视频信息(更新)
        elif (table == "amazon_product_review_video"):
            region = searchData['region']
            review_id = searchData['review_id']
            sql = self.amazon.productReviewVideo_update_sql_joint(region, review_id, data)
            result = self.mapper.update(sql)
        return result

    def insert(self, table=None, data=None, searchData=None):
        # 抓取产品时插入产品信息表
        if (table == "amazon_product"):
            region = searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.product_insert_sql_joint(region, asin, data)
            result = self.mapper.insert(sql)
        # 抓取产品时插入产品图片表
        elif (table == "amazon_product_images"):
            region = searchData["region"]
            asin = searchData["asin"]
            url = searchData["url"]
            sql = self.amazon.product_images_insert_sql_joint(region, asin, url, data)
            result = self.mapper.insert(sql)
        elif (table == "amazon_product_image"):
            region = searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.product_image_insert_sql_joint(region, asin, data)
            result = self.mapper.insert(sql)
        # 抓取关键词时插入广告关键词表
        elif (table == "amazon_product_keywords_ad"):
            region = searchData["region"]
            keywords = searchData["keywords"]
            node_id = searchData["node_id"]
            ad_position = searchData["ad_position"]
            ad_position_type = searchData["ad_position_type"]
            position = searchData["position"]
            sql = self.amazon.keywords_ad_insert_sql_joint(region, keywords, node_id, ad_position, ad_position_type, position, data)
            result = self.mapper.insert(sql)
        # 抓取关键词插入广告排名表
        elif (table == "amazon_product_keywords_rank"):
            region = searchData["region"]
            keywords = searchData["keywords"]
            node_id = searchData["node_id"]
            rank = searchData["rank"]
            sql = self.amazon.keywords_rank_insert_sql_joint(region, keywords, node_id, rank, data)
            result = self.mapper.insert(sql)
        # 抓取关键词时插入关键词信息表
        elif (table == "keywords"):
            region = searchData["region"]
            keywords = searchData["name"]
            sql = self.amazon.keywordsObject_insert_sql_joint(region, keywords, data)
            result = self.mapper.insert(sql)
        # 移动端抓取关键词时插入移动端关键词信息表
        elif (table == "mobile_keywords"):
            region = searchData["region"]
            keywords = searchData["name"]
            sql = self.amazon.mobilekeywordsObject_insert_sql_joint(region, keywords, data)
            result = self.mapper.insert(sql)
        # 抓取关键词时插入上传产品队列表
        elif (table == "upload_queue"):
            region = data["region"]
            type = data["type"]
            asin = data["value"]
            time = data["time"]
            sql = self.amazon.getUploadQueue_insert_sql_joint(region, type, asin, time)
            result = self.mapper.insert(sql)
        # 移动端抓取关键词时插入上传产品队列表
        elif (table == "mobile_upload_queue"):
            region = data["region"]
            type = data["type"]
            asin = data["value"]
            sql = self.amazon.getMobileUploadQueue_insert_sql_joint(region, type, asin)
            result = self.mapper.insert(sql)
        # 抓取卖家offer时插入卖家offer表
        elif (table == "amazon_seller_product_offer"):
            region =  searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.offer_insert_sql_joint(region, asin, data)
            result = self.mapper.insert(sql)
        # 抓取卖家offer时插入卖家信息表
        elif (table == "amazon_seller"):
            region = searchData["region"]
            sql = self.amazon.seller_insert_sql_joint(region, data)
            result = self.mapper.insert(sql)
        # 抓取卖家offer时插入卖家产品信息表
        elif (table == "amazon_seller_product"):
            region = searchData["region"]
            asin = searchData["asin"]
            sql = self.amazon.sellerproduct_insert_sql_joint(region, asin, data)
            result = self.mapper.insert(sql)
        # 抓取卖家信息页时抓取卖家信息表
        elif (table == "seller"):
            region = searchData["region"]
            seller_id = searchData["seller_id"]
            sql = self.amazon.sellerinfo_insert_sql_joint(region, seller_id, data)
            result = self.mapper.insert(sql)
        # 插入产品前先插入卖家信息
        elif (table == "product_seller"):
            region = data["region"]
            seller_id = data["seller_id"]
            sql = self.amazon.product_seller_insert_sql_joint(region, seller_id)
            result = self.mapper.insert(sql)
        # 插入表scrape
        elif (table == "scrape"):
            sql = self.amazon.insert_scrape(data)
            try:
                result = self.mapper.insert(sql)
            except:
                pass
        # 插入product_review表
        elif (table == "amazon_product_review"):
            sql = self.amazon.productReview_insert_sql_joint(data)
            result = self.mapper.insert(sql)
        # 抓取评论页图片信息(插入)
        elif (table == "amazon_product_review_image"):
            sql = self.amazon.productReviewImage_insert_sql_joint(data)
            result = self.mapper.insert(sql)
        # 抓取评论页图片信息(插入)
        elif (table == "amazon_product_review_video"):
            sql = self.amazon.productReviewVideo_insert_sql_joint(data)
            result = self.mapper.insert(sql)
        return result

    def delete(self, table=None, searchData=None):
        if (table == "amazon_product_keywords_ad"):
            region = searchData["region"]
            keywords = searchData["keywords"]
            node_id = searchData["node_id"]
            sql = self.amazon.keywords_ad_delete_sql_joint(region, keywords, node_id)
            result = self.mapper.delete(sql)
        elif (table == "amazon_product_keywords_rank"):
            region = searchData["region"]
            keywords = searchData["keywords"]
            node_id = searchData["node_id"]
            sql = self.amazon.keywords_rank_delete_sql_joint(region, keywords, node_id)
            result = self.mapper.delete(sql)
        return result
