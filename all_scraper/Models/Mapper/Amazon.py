#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-17'
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
import time
# from Models.Mapper.Abstract import Model_Mapper_Abstract
import urllib
import sys
reload(sys)
import pytz
import datetime
sys.setdefaultencoding('utf-8')

class Model_Mapper_Amazon():

    '''
    amazon sql语句拼接
    '''
    '''
    产品信息sql语句拼接
    '''
    # 产品信息查找sql语句拼接
    def product_select_sql_joint(self, region, asin):
        sql = 'select * from amazon_product WHERE region='+'"'+region+'"'+' and asin='+'"'+asin+'"'
        return sql

    # 产品信息更新sql语句拼接
    def product_update_sql_joint(self, region, asin, data):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        # import time
        # last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        k = []
        try:
            for key, value in data.items():
                if (key != "total" and key != "asin" and key != "images" and key != "image" and key != "page_position" and key != "height" and key != "width" and key != "sponsor" and key != "page_id" and key != "sponsor_position" and key != "sponsor_position_type" and value != ''):
                    if (key == "title"):
                        value = value.replace("\"", "")
                    if (key == "description"):
                        try:
                            value = value.encode("utf-8").replace("\"", "").replace("#", "")
                        except:
                            value = value.replace("\"", "").replace("#", "")
                    if (key == "offer_count" or key == "shipping" or key == "seller_name"):
                        value = value.encode("utf-8").replace("\"", "")
                    if (key == 'rating'):
                        value = str(int(float(value) * 10))
                    k.append('`'+key+'`' + '=' + '"'+str(value).encode("utf-8")+'"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_product set last_updated_time = '+'"'+last_updated_time+'"'+', '+ str(v) +' WHERE region =' + '"' + region + '"' + ' and asin=' + '"' + asin + '"'
        # print (sql)
        return sql

    # 产品信息插入sql语句拼接
    def product_insert_sql_joint(self, region, asin, data):
        k = []
        v = []
        try:
            for key, value in data.items():
                if (key != "total" and key != "asin" and key != "images" and key != "image" and key != "page_position" and key != "height" and key != "width" and key != "sponsor" and key != "page_id" and key != "sponsor_position" and key != "sponsor_position_type" and value != ''):
                    if (key == "title"):
                        try:
                            value = value.encode("utf-8").replace("\"", "").replace("#", "")
                        except:
                            value = value.replace("\"", "").replace("#", "")
                    if (key == "description"):
                        try:
                            value = value.encode("utf-8").replace("\"", "").replace("#", "")
                        except:
                            value = value.replace("\"", "").replace("#", "")
                    if (key == "offer_count" or key == "shipping" or key == "seller_name"):
                        value = value.encode("utf-8").replace("\"", "")
                    if (key == 'rating'):
                        value = int(float(value) * 10)
                    k.append("`" + key + "`")
                    v.append('"' + str(value) + '"')
        except Exception as err:
            print (err)
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        try:
            sql = 'insert into amazon_product(`region`, `asin`, ' + sql_key + ') VALUES (' + '"'+region+'", ' + '"'+asin +'", ' + sql_value + ')'
            # print (sql)
            return sql
        except:
            print ("sql error")

    # 产品信息更新sql语句(抓取sellerproduct时)
    def products_update_sql_joint(self, region, asin, data):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        # import time
        # products_last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        k = []
        try:
            for key, value in data.items():
                if (key == "title" or key == "seller_rating" or key == "review_count" or key == "price" or key == "list_price" or key == "bestseller_browse_node_id" and value != ''):
                    if (key == "title"):
                        value = value.replace("\"", "")
                    if (key == "seller_rating"):
                        key = "rating"
                    if (key == 'rating'):
                        value = str(int(float(value) * 10))
                    if (key == "bestseller_browse_node_id"):
                        key = "bestseller_node_id"
                    k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_product set last_updated_time = '+'"'+last_updated_time+'"'+', '+ str(v) + ' WHERE region =' + '"' + region + '"' + ' and asin=' + '"' + asin + '"'
        # print (sql)
        return sql

    # 产品信息插入sql语句(抓取sellerproduct时)
    def products_insert_sql_joint(self, region, asin, data):
        k = []
        v = []
        try:
            for key, value in data.items():
                if (key == "title" or key == "seller_rating" or key == "review_count" or key == "price" or key == "list_price" or key == "bestseller_browse_node_id" and value != ''):
                    if (key == "title"):
                        try:
                            value = value.encode("utf-8").replace("\"", "").replace("#", "")
                        except:
                            value = value.replace("\"", "").replace("#", "")
                    if (key == 'seller_rating'):
                        key = 'rating'
                    if (key == 'rating'):
                        value = int(float(value) * 10)
                    if (key == 'bestseller_browse_node_id'):
                        key = 'bestseller_node_id'
                    k.append("`" + key + "`")
                    v.append('"' + str(value) + '"')
        except Exception as err:
            print (err)
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        try:
            sql = 'insert into amazon_product(`region`, `asin`, ' + sql_key + ') VALUES (' + '"' + region + '", ' + '"' + asin + '", ' + sql_value + ')'
            # print (sql)
            return sql
        except:
            print ("products insert sql error")

    # 产品图片信息sql语句拼接
    def product_image_select_sql_joint(self, region, asin):
        sql = 'select * from amazon_product_image WHERE region=' + '"' + region + '"' + ' and asin=' + '"' + asin + '"'
        return sql

    def product_uploadimage_select_sql_joint(self, region, asin):
        sql = 'select * from amazon_product_image WHERE region=' + '"' + region + '"' + ' and asin=' + '"' + asin + '"' + ' and position = 0'
        return sql

    def product_image_insert_sql_joint(self , region, asin, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == "image" or key == "width" or key == "height"):
                if (key == "image"):
                    key = "url"
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_image(`region`, `asin`, '+ sql_key +') VALUES ('+'"'+region+'", '+'"'+asin+'", '+ sql_value +')'
        # print sql
        return sql

    def product_images_select_sql_joint(self, region, asin, url):
        sql = 'select * from amazon_product_image where region='+ '"' +region+ '"' +' and asin ='+ '"' +asin+ '"' +' and url ='+ '"' +url+ '"'
        return sql

    def product_images_update_sql_joint(self, region, asin, url, position):
        sql = 'update amazon_product_image set position = '+str(position)+' where region ='+ '"' +region+ '"' +' and asin ='+ '"' +asin+ '"' +' and url ='+ '"' +url+ '"'
        return sql

    def product_images_insert_sql_joint(self, region, asin, url, position):
        sql = 'insert into amazon_product_image(`region`, `asin`, `url`, `position`) VALUES ('+'"'+region+'", '+'"'+asin+'", '+'"'+url+'", '+'"'+str(position)+'"'+')'
        return sql

    '''
    关键词信息sql语句拼接
    '''
    # 广告信息sql插入语句拼接
    def keywords_ad_insert_sql_joint(self, region, keywords, node_id, ad_position, ad_position_type, position, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == "asin" or key == "page_id" or key == "page_position" or key == "last_updated_time"):
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_keywords_ad(`region`, `keywords`, `node_id`, `ad_position`, `ad_position_type`, `position`, '+ sql_key +') VALUES ('+'"'+region+'", '+'"'+keywords+'", '+'"'+str(node_id)+'", '+'"'+str(ad_position)+'", '+'"'+str(ad_position_type)+'", '+'"'+str(position)+'", '+ sql_value +')'
        return sql

    # 广告信息sql删除语句拼接
    def keywords_ad_delete_sql_joint(self, region, keywords, node_id):
        sql = 'delete from amazon_product_keywords_ad WHERE region='+'"'+region+'"'+ " and keywords ="+'"'+keywords+'"' + "and node_id ="+ '"'+node_id+'"'
        return sql

    # 自然排名信息sql插入语句拼接
    def keywords_rank_insert_sql_joint(self, region, keywords, node_id, rank, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == "asin" or key == "page_id" or key == "page_position" or key == "last_updated_time"):
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_keywords_rank(`region`, `keywords`, `node_id`, `rank`, ' + sql_key + ') VALUES (' + '"' + region + '", ' + '"' + keywords + '", ' + '"' + str(node_id) + '", ' + '"' + str(rank) + '", ' + sql_value + ')'
        return sql

    # 自然排名信息sql删除语句拼接
    def keywords_rank_delete_sql_joint(self, region, keywords, node_id):
        sql = 'delete from amazon_product_keywords_rank WHERE region=' + '"' + region + '"' + " and keywords =" + '"' + keywords + '"' + "and node_id ="+ '"'+node_id+'"'
        return sql

    '''
    存储关键词数据
    '''
    # 存储关键词查询sql语句拼接
    def keywordsObject_select_sql_joint(self, region, keywords):
        sql = 'select * from keywords WHERE region='+'"'+region+'"'+' and name='+'"'+keywords+'"'
        return sql

    # 存储关键词插入sql语句拼接
    def keywordsObject_insert_sql_joint(self, region, keywords, data):
        sql = 'insert into keywords(`region`, `name`, `amazon_product_search_count`) VALUES ('+'"'+region+'", '+'"'+keywords+'", '+'"'+data+'"'+')'
        return sql

    def mobilekeywordsObject_insert_sql_joint(self, region, keywords, data):
        sql = 'insert into mobile_keywords(`region`, `name`, `amazon_product_search_count`) VALUES ('+'"'+region+'", '+'"'+keywords+'", '+'"'+data+'"'+')'
        return sql

    # 存储关键词更新sql语句拼接
    def keywordsObject_update_sql_joint(self, region, keywords, data):
        sql = 'update keywords set amazon_product_search_count =' + '"' + data + '"' + ' WHERE region =' + '"'+region+'"' + ' and name='+ '"'+keywords+'"'
        return sql

    def mobilekeywordsObject_update_sql_joint(self, region, keywords, data):
        sql = 'update mobile_keywords set amazon_product_search_count =' + '"' + data + '"' + ' WHERE region =' + '"'+region+'"' + ' and name='+ '"'+keywords+'"'
        return sql

    '''
    上传队列sql语句拼接
    '''
    # 上传队列查询sql语句拼接
    def getUploadQueue_select_sql_joint(self, region, type, asin):
        sql = 'select * from upload_queue where region ='+ '"' +str(region)+ '"' +' and type ='+ '"' +str(type)+ '"' +' and value ='+ '"' +asin+ '"'
        return sql

    # 上传队列插入sql语句拼接
    def getUploadQueue_insert_sql_joint(self, region, type, asin, time):
        sql = 'insert into upload_queue (`region`, `type`, `value`, `time`) VALUES ('+ '"' +str(region)+ '", ' + '"' +str(type)+ '", ' + '"' +asin+ '", ' + '"' +str(time)+ '"' +')'
        return sql

    def getMobileUploadQueue_insert_sql_joint(self, region, type, asin):
        sql = 'insert into mobile_upload_queue (`region`, `type`, `value`) VALUES ('+ '"' +str(region)+ '", ' + '"' +str(type)+ '", ' + '"' +asin+ '"' +')'
        return sql

    # 上传队列更新sql语句拼接
    def getUploadQueue_update_sql_joint(self, region, type, asin):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        # import time
        # # 格式化成2016-03-20 11:45:39形式
        # uploadtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'update upload_queue SET time ='+'"'+str(last_updated_time)+'"'+' WHERE region='+ '"' +str(region)+ '"' +' and type ='+ '"' +str(type)+ '"' +' and value ='+ '"' +asin+ '"'
        return sql

    def getMobileUploadQueue_update_sql_joint(self, region, type, asin):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        # import time
        # # 格式化成2016-03-20 11:45:39形式
        # uploadtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'update mobile_upload_queue SET time ='+'"'+str(last_updated_time)+'"'+' WHERE region='+ '"' +str(region)+ '"' +' and type ='+ '"' +str(type)+ '"' +' and value ='+ '"' +asin+ '"'
        return sql

    def getAmazonProductKeywordsRank_select_sql_joint(self, region, keywords):
        sql = 'select * from amazon_product_keywords_rank WHERE region ='+'"'+region+'"'+' and keywords ='+'"'+keywords+'"'
        return sql

    def getAmazonProductKeywordsAd_select_sql_joint(self, region, keywords):
        sql = 'select * from amazon_product_keywords_ad WHERE region ='+'"'+region+'"'+' and keywords ='+'"'+keywords+'"'
        return sql

    def getKeywords(self, region, keywords):
        sql = 'select * from keywords WHERE region ='+'"'+region+'"'+' and name ='+'"'+keywords+'"'
        return sql

    # 获取sellerProduct产品
    def SellerProduct_upload_select_sql_joint(self, region, asin):
        sql = 'select * from amazon_seller_product WHERE region ='+'"'+region+'"'+' and asin ='+'"'+asin+'"'
        return sql

    # 获取sellerProduct_offer
    def SellerProductOffer_upload_select_sql_joint(self, region, asin):
        sql = 'select * from amazon_seller_product_offer WHERE region ='+'"'+region+'"'+' and asin ='+'"'+asin+'"'
        return sql

    # 获取topreviewer
    def TopReviewerUpload_select_sql_joint(self, region, begin, end):
        sql = 'select * from amazon_top_reviewer WHERE region ='+'"'+region+'"'+' and rank >='+'"'+str(begin)+'"'+' and rank <='+'"'+str(end)+'"'
        return sql

    '''
    评论信息sql语句拼接
    '''
    def review_sql_joint(self, region, asin, data):
        pass

    '''
    offer与库存信息sql语句拼接
    '''
    # 查找sql语句拼接
    def offer_select_sql_joint(self, region, asin, data):
        sql = 'select * from amazon_seller_product_offer WHERE region ='+'"'+region+'"'+' and asin ='+'"'+asin+'"'+' and item_id ='+'"'+data['item_id']+'"'
        return sql
    # 更新sql语句拼接
    def offer_update_sql_joint(self, region, asin, data):  # 保留region和asin字段，暂未使用
        k = []
        try:
            for key, value in data.items():
                if (key == 'seller_id' or key == 'price' or key == 'shipping' or key == 'condition' or key == 'fulfillment' or key == 'inventory'):
                    if (value != ''):
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_seller_product_offer set '+str(v)+' WHERE region ='+'"'+region+'"'+' and asin ='+'"'+asin+'"'+' and item_id ='+'"'+data['item_id']+'"'
        # print (sql)
        return sql

    # 插入sql语句拼接
    def offer_insert_sql_joint(self, region, asin, data):
        k = []
        v = []
        for key, value in data.items():
            if (key != "seller_rating_count" and key != "seller_name" and key != "session_id" and key != "seller_rating" and key != "seller_positive" and key != "offering_id"):
                k.append("`" + key + "`")
                v.append('"' + value + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_seller_product_offer(`region`, `asin`, ' + sql_key + ') VALUES (' + '"'+region+'", ' + '"'+asin +'", ' + sql_value + ')'
        # print (sql)
        return sql

    # amazon_seller表卖家查找sql语句(offer抓取时)
    def seller_select_sql_joint(self, region, seller_id):
        sql = 'select * from amazon_seller WHERE region ='+ '"'+region+'"'+' and seller_id ='+'"'+seller_id+'"'
        return sql

    # seller表卖家信息更新sql语句(offer抓取时)
    def seller_update_sql_joint(self, region, data):
        k = []
        try:
            for key, value in data.items():
                if (key == 'seller_name' or key == 'seller_rating'):
                    if (key == 'seller_name'):
                        key = "name"
                        value = value.replace("\"", "'")
                    if (key == 'seller_rating'):
                        key = "rating"
                        if (value != 0):
                            value = str(int(float(value)*10))
                    if (value != ''):
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_seller set '+str(v)+' WHERE region ='+'"'+region+'" and seller_id ='+'"'+data['seller_id']+'"'
        return sql

    # seller表卖家信息插入sql语句(offer抓取时)
    def seller_insert_sql_joint(self, region, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == "seller_id" or key == "seller_name" or key == "seller_rating"):
                if (key == "seller_name"):
                    key = "name"
                    value = value.replace("\"", "'")
                if (key == "seller_rating"):
                    key = "rating"
                    value = str(int(float(value)*10))
                if (value != ""):
                    k.append("`" + key + "`")
                    v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        # sql = 'insert into amazon_seller (`region`, ' + sql_key + ') VALUES ('+'"'+region+'", '+'"'+data['seller_id']+'", '+'"'+data['seller_name']+'", '+'"'+str(int(float(data['seller_rating'])*10))+'"'+')'
        sql = 'insert into amazon_seller (`region`, ' + sql_key + ') VALUES ('+'"'+region+'", '+ sql_value +')'
        # print (sql)
        return sql

    def product_seller_insert_sql_joint(self, region, merchant_id):
        sql = 'insert into amazon_seller (`region`, `seller_id`) VALUES ('+'"'+region+'", '+'"'+merchant_id+'"'+')'
        return sql

    # seller表卖家信息更新sql语句(seller卖家抓取时)
    def sellerinfo_update_sql_joint(self, region, merchant_id, data):
        k = []
        try:
            for key, value in data.items():
                if (value != ''):
                    if (key == 'feedback_positive_thirty_days'):
                        key = 'last_30_days_positive_feedback_ratio'
                    if (key == 'feedback_positive_ninty_days'):
                        key = 'last_90_days_positive_feedback_ratio'
                    if (key == 'feedback_positive_twelve_months'):
                        key = 'last_12_months_positive_feedback_ratio'
                    if (key == 'feedback_positive_lifetime'):
                        key = 'lifetime_positive_feedback_ratio'
                    if (key == 'feedback_neutral_thirty_days'):
                        key = 'last_30_days_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_ninty_days'):
                        key = 'last_90_days_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_twelve_months'):
                        key = 'last_12_months_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_lifetime'):
                        key = 'lifetime_neutral_feedback_ratio'
                    if (key == 'feedback_negative_thirty_days'):
                        key = 'last_30_days_negative_feedback_ratio'
                    if (key == 'feedback_negative_ninty_days'):
                        key = 'last_90_days_negative_feedback_ratio'
                    if (key == 'feedback_negative_twelve_months'):
                        key = 'last_12_months_negative_feedback_ratio'
                    if (key == 'feedback_negative_lifetime'):
                        key = 'lifetime_negative_feedback_ratio'
                    if (key == 'feedback_count_thirty_days'):
                        key = 'last_30_days_feedback_count'
                    if (key == 'feedback_count_ninty_days'):
                        key = 'last_90_days_feedback_count'
                    if (key == 'feedback_count_twelve_months'):
                        key = 'last_12_months_feedback_count'
                    if (key == 'feedback_count_lifetime'):
                        key = 'lifetime_feedback_count'
                    if (key == 'rating'):
                        value = str(int(float(value) * 10))
                    k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_seller set ' + str(v) + ' WHERE region=' + '"' + region + '"' + ' and seller_id =' + '"' + merchant_id + '"'
        return sql

    def sellerinfo_insert_sql_joint(self, region, merchant_id, data):
        k = []
        v = []
        try:
            for key, value in data.items():
                if (value != ''):
                    if (key == 'feedback_positive_thirty_days'):
                        key = 'last_30_days_positive_feedback_ratio'
                    if (key == 'feedback_positive_ninty_days'):
                        key = 'last_90_days_positive_feedback_ratio'
                    if (key == 'feedback_positive_twelve_months'):
                        key = 'last_12_months_positive_feedback_ratio'
                    if (key == 'feedback_positive_lifetime'):
                        key = 'lifetime_positive_feedback_ratio'
                    if (key == 'feedback_neutral_thirty_days'):
                        key = 'last_30_days_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_ninty_days'):
                        key = 'last_90_days_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_twelve_months'):
                        key = 'last_12_months_neutral_feedback_ratio'
                    if (key == 'feedback_neutral_lifetime'):
                        key = 'lifetime_neutral_feedback_ratio'
                    if (key == 'feedback_negative_thirty_days'):
                        key = 'last_30_days_negative_feedback_ratio'
                    if (key == 'feedback_negative_ninty_days'):
                        key = 'last_90_days_negative_feedback_ratio'
                    if (key == 'feedback_negative_twelve_months'):
                        key = 'last_12_months_negative_feedback_ratio'
                    if (key == 'feedback_negative_lifetime'):
                        key = 'lifetime_negative_feedback_ratio'
                    if (key == 'feedback_count_thirty_days'):
                        key = 'last_30_days_feedback_count'
                    if (key == 'feedback_count_ninty_days'):
                        key = 'last_90_days_feedback_count'
                    if (key == 'feedback_count_twelve_months'):
                        key = 'last_12_months_feedback_count'
                    if (key == 'feedback_count_lifetime'):
                        key = 'lifetime_feedback_count'
                    if (key == 'rating'):
                        value = str(int(float(value) * 10))
                    k.append("`" + key + "`")
                    v.append('"' + value + '"')
            sql_key = ", ".join(k)
            sql_value = ", ".join(v)
            sql = 'insert into amazon_seller(`region`, `seller_id`, '+ sql_key +') VALUES('+'"'+region+'", '+'"'+merchant_id+'", '+sql_value+')'
            return sql
        except Exception as err:
            print (err)

    # sellerproduct表卖家产品信息查询sql语句(offer抓起时)
    def sellerproduct_select_sql_joint(self, region, asin, seller_id):
        sql = 'select * from amazon_seller_product WHERE region = '+'"'+region+'"'+' and asin='+'"'+asin+'"'+' and seller_id ='+'"'+seller_id+'"'
        return sql

    # sellerproducts 上传卖家产品信息查询sql语句(上传时)
    def sellerproducts_select_sql_joint(self, region, merchant_id):
        sql = 'select * from amazon_seller_product WHERE region = ' + '"' + region + '"' + ' and seller_id =' + '"' + merchant_id + '"'
        return sql

    # sellerproduct表卖家产品信息更新sql语句(offer抓起时)
    def sellerproduct_update_sql_joint(self, region, asin, data):
        k = []
        try:
            for key, value in data.items():
                if (key == 'seller_rating_count' or key == 'seller_name' or key == 'price' or key == 'seller_rating' or key == 'seller_positive'):
                    if (value != ''):
                        if (key == 'seller_rating_count'):
                            key = 'seller_lifetime_feedback_count'
                        if (key == 'seller_positive'):
                            key = 'seller_last_12_months_positive_feedback_ratio'
                        if (key == 'seller_rating'):
                            value = str(int(float(value)*10))
                        if (key == 'seller_name'):
                            value = value.replace("\"", "'")
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except:
            pass
        v = " , ".join(k)
        sql = 'update amazon_seller_product set '+str(v)+' WHERE region='+'"'+region+'"'+' and asin='+'"'+asin+'"'+' and seller_id ='+'"'+data['seller_id']+'"'
        return sql

    # sellerproduct表卖家产品信息插入sql语句(offer抓起时)
    def sellerproduct_insert_sql_joint(self, region, asin, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == 'seller_rating_count' or key == 'seller_id' or key == 'seller_name' or key == 'price' or key == 'list_price' or key == 'seller_rating' or key == 'seller_positive'):
                if (key == 'seller_rating_count'):
                    key = 'seller_lifetime_feedback_count'
                if (key == 'seller_positive'):
                    key = 'seller_last_12_months_positive_feedback_ratio'
                if (key == 'seller_rating'):
                    value = str(int(float(value) * 10))
                if (key == 'seller_name'):
                    value = value.replace("\"", "'")
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_seller_product (`region`, `asin`, ' + sql_key + ') VALUES ('+ '"'+region+'", '+'"'+asin+'", '+ sql_value + ')'
        return sql

    # sellerproduct表产品rank清空sql语句(抓取sellerproduct时)
    def sellerproducts_rankupdate_sql_joint(self, region, merchant_id):
        sql = 'update amazon_seller_product set rank = NULL WHERE region ='+'"'+region+'"'+' and seller_id ='+'"'+merchant_id+'"'
        return sql

    # sellerproduct表产品信息更新sql语句(抓取sellerproduct时)
    def sellerproducts_update_sql_joint(self, region, asin, merchant_id, rank, data):
        k = []
        try:
            for key, value in data.items():
                if (key == 'price' or key == 'list_price' or key == 'seller_rating' or key == 'bestseller_search_index' or key == 'bestseller_browse_node_id'):
                    if (value != ''):
                        if (key == 'bestseller_search_index'):
                            key = 'search_index'
                        if (key == 'bestseller_browse_node_id'):
                            key = 'bestseller_node_id'
                        if (key == 'seller_rating'):
                            value = str(int(float(value) * 10))
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except:
            pass
        v = " , ".join(k)
        sql = 'update amazon_seller_product set rank = '+'"'+str(rank)+'"'+', ' + str(v) + ' WHERE region=' + '"' + region + '"' + ' and asin=' + '"' + asin + '"' + ' and seller_id =' + '"' + merchant_id + '"'
        return sql

    # amazon_product_review表更新语句
    def productReview_update_sql_joint(self, region, asin, review_id, data):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        k = []
        try:
            for key, value in data.items():
                if (key != 'region' and key != 'asin' and key != 'review_id'):
                    if (value != ''):
                        if (key == 'title' or key == 'description'):
                            value = value.replace("\"", "").replace("\'", "")
                        if (key == 'rating'):
                            value = str(int(float(value) * 10))
                        k.append('`' + key + '`' + '=' + '"' + str(value).encode("utf-8") + '"')
            k.append('`' + "last_updated_time" + '`' + '=' + '"' + str(last_updated_time) + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update amazon_product_review set ' + str(v) + ' WHERE region=' + '"' + region + '"' + ' and asin=' + '"' + asin + '"' + ' and review_id =' + '"' + review_id + '"'
        print (sql)
        return sql

    # amazon_product_review_image表更新语句
    def productReviewImage_update_sql_joint(self, region, review_id, url, data):
        k = []
        try:
            for key, value in data.items():
                if (key != 'region' and key != 'review_id' and key != 'url'):
                    if (value != ''):
                        if (key == 'key'):
                            key = "position"
                            value = str(value)
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except:
            pass
        v = " , ".join(k)
        sql = 'update amazon_product_review_image set ' + str(v) + ' WHERE region=' + '"' + region + '"' + ' and review_id =' + '"' + review_id + '"' + ' and url =' + '"' + url + '"'
        return sql

    # amazon_product_review_video表更新语句
    def productReviewVideo_update_sql_joint(self, region, review_id, data):
        k = []
        try:
            for key, value in data.items():
                if (key != 'region' and key != 'review_id'):
                    if (value != ''):
                        k.append('`' + key + '`' + '=' + '"' + value.encode("utf-8") + '"')
        except:
            pass
        v = " , ".join(k)
        sql = 'update amazon_product_review_video set ' + str(v) + ' WHERE region=' + '"' + region + '"' + ' and review_id =' + '"' + review_id + '"'
        return sql

    # sellerproduct表产品信息插入sql语句(抓取sellerproduct时)
    def sellerproducts_insert_sql_joint(self, region, merchant_id, rank, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == 'asin' or key == 'price' or key == 'list_price' or key == 'seller_rating' or key == 'bestseller_search_index' or key == 'bestseller_browse_node_id'):
                if (key == 'bestseller_search_index'):
                    key = 'search_index'
                if (key == 'bestseller_browse_node_id'):
                    key = 'bestseller_node_id'
                if (key == 'seller_rating'):
                    value = str(int(float(value) * 10))
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_seller_product (`region`, `seller_id`, `rank`, ' + sql_key + ') VALUES (' + '"' + region + '", ' + '"' + merchant_id + '", ' + '"' + str(rank) + '", ' + sql_value + ')'
        return sql

    # 数据库表scrape插入语句
    def insert_scrape(self, data):
        k = []
        v = []
        for key, value in data.items():
            k.append("`" + key + "`")
            v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into scrape (' + sql_key + ') VALUES ('+ sql_value + ')'
        # print (sql)
        return sql

    # amazon_product_review表插入语句
    def productReview_insert_sql_joint(self, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == 'title' or key == 'description'):
                value = value.replace("\"", "'")
            if (key == 'rating'):
                value = str(int(float(value) * 10))
            k.append("`" + key + "`")
            v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_review (' + sql_key + ') VALUES (' + sql_value + ')'
        return sql

    # amazon_product_review_image表插入语句
    def productReviewImage_insert_sql_joint(self, data):
        k = []
        v = []
        for key, value in data.items():
            if (key == 'key'):
                key = "position"
            k.append("`" + key + "`")
            v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_review_image (' + sql_key + ') VALUES (' + sql_value + ')'
        return sql

    # amazon_product_review_video表插入语句
    def productReviewVideo_insert_sql_joint(self, data):
        k = []
        v = []
        for key, value in data.items():
            k.append("`" + key + "`")
            v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_product_review_video (' + sql_key + ') VALUES (' + sql_value + ')'
        return sql

    def getDownloadQueue_sql_joint(self, region, t, count):
        types = ",".join(t)
        sql = 'select * from download_queue where type in ('+types+') and upload_status = 0 and status != 0 and region = '+'"'+region[0]+'"'+' order by time asc limit '+str(count)+' offset 0'
        return sql

    # processUploadQueue时查询下载队列
    def DownloadQueue_select_sql_joint(self, downloadQueue_id):
        sql = 'select * from download_queue where id ='+'"'+str(downloadQueue_id)+'"'
        return sql

    def DownloadQueue_update_sql_joint(self, status, count, id):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        sql = 'update download_queue SET upload_status ='+'"'+str(status)+'"'+', upload_count ='+'"'+str(count)+'"'+', last_updated_time ='+'"'+last_updated_time+'"'+' WHERE id ='+'"'+str(id)+'"'
        # print (sql)
        return sql

    # processUploadQueue 根据upload_queue_id查询upload_queue
    def UploadQueue_select_sql_joint(self, upload_queue_id):
        sql = 'select * from upload_queue WHERE id ='+'"'+upload_queue_id+'"'
        return sql

    def MobileUploadQueue_select_sql_joint(self, upload_queue_id):
        sql = 'select * from mobile_upload_queue WHERE id ='+'"'+upload_queue_id+'"'
        return sql

    # processUploadQueue 上传成功后根据upload_queue_id删除相应数据
    def UploadQueue_delete_sql_joint(self, upload_queue_id):
        sql = 'delete from upload_queue WHERE id ='+'"'+upload_queue_id+'"'
        return sql

    def MobileUploadQueue_delete_sql_joint(self, upload_queue_id):
        sql = 'delete from mobile_upload_queue WHERE id ='+'"'+upload_queue_id+'"'
        return sql

    def getUploadQueue_sql_joint(self, region):
        sql = 'select * from upload_queue WHERE region ='+'"'+region+'"'+' order by time limit 1000 offset 0'
        return sql

    def getMobileUploadQueue_sql_joint(self, region):
        sql = 'select * from mobile_upload_queue WHERE region ='+'"'+region+'"'+' order by time limit 1000 offset 0'
        return sql

    # TopReviewer表根据rank删除信息sql语句(抓取TopReviewer表时)
    def TopReviewer_delete_sql_joint(self, region, begin, end):
        sql = 'delete from amazon_top_reviewer WHERE region ='+'"'+region+'"'+' and rank >='+'"'+str(begin)+'"'+' and rank <='+'"'+str(end)+'"'
        return sql

    # TopReviewer表插入信息sql语句(抓取TopReveiwer表时)
    def TopReviewer_insert_sql_joint(self, region, data):
        k = []
        v = []
        for key, value in data.items():
            if (key != 'profile_image_url'):
                if (key == 'name'):
                    value = value.replace("🎭", "")
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        sql = 'insert into amazon_top_reviewer (`region`, ' + sql_key + ') VALUES (' + '"' + region + '", ' + sql_value + ')'
        return sql

    # TopReviewer表插入信息sql语句
    # def TopReviewer_insert_sql_joint(self, region, ):

    '''
    其他数据库sql语句拼接
    '''
    # 此函数与之前的函数无关
    # 添加数据库数据
    def select_products(self, region, status):
        sql = 'select asin from asin_list WHERE region = '+'"'+region+'"'+ ' and status = '+'"'+status+'"'+' limit 1000 offset 0'
        # print (sql)
        return sql

    def insert_products(self, ac_download_queue_id, region, t, value):
        sql = 'insert into download_queue (`ac_download_queue_id`, `region`, `type`, `value`) VALUES ('+'"'+ac_download_queue_id+'", '+'"'+region+'", '+'"'+t+'", '+'"'+value+'"'+')'
        # print (sql)
        return sql

    def select_keywords(self, region, status):
        sql = 'select keywords from keywords_list limit 1000 offset 100'
        # print (sql)
        return sql

    def update_download_queue(self, id, data):
        # 'update amazon_seller_product_offer set inventory ='+'"'+data['inventory']+'"'+' WHERE item_id ='+'"'+data['item_id']+'"'
        k = []
        try:
            for key, value in data.items():
                if (key != 'id'):
                    if (value != ''):
                        k.append('`' + key + '`' + '=' + '"' + str(value) + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update download_queue set ' + str(v) + ' WHERE id = ' + '"' + str(id) + '"'
        # print (sql)
        return sql

    # 更新产品评论时download_queue表value值更新
    def update_download_queue_review(self, id, data):
        k = []
        try:
            for key, value in data.items():
                if (key != 'id'):
                    if (value != ''):
                        k.append('`' + key + '`' + '=' + '"' + str(value) + '"')
        except Exception as err:
            print (err)
        v = " , ".join(k)
        sql = 'update download_queue set ' + str(v) + ' WHERE id = ' + '"' + str(id) + '"'
        # print (sql)
        return sql

    def update_mobile_download_queue(self, region, type, value, status, scrape_count):
        # 'update amazon_seller_product_offer set inventory ='+'"'+data['inventory']+'"'+' WHERE item_id ='+'"'+data['item_id']+'"'
        sql = 'update mobile_download_queue set status ='+status+', scrape_count ='+scrape_count+' WHERE region ='+'"'+region+'"'+' and type ='+'"'+type+'"'+' and value ='+'"'+value+'"'
        return sql

    def delete_learn_app_person(self, region, type, value):
        sql = 'delete from learn_app_person WHERE region ='+'"'+region+'"'+' and type ='+'"'+type+'"'+' and value ='+'"'+value+'"'
        return sql