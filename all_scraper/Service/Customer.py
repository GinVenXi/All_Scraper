#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-23'
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

from Models.Keys import Model_Keys
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Mapper.Scrape import Model_Mapper_Scrape
from Models.Scraper.TopReviewer import Model_Scraper_TopReviewer
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Models.Static.Region import Model_Static_Region
from Service.Abstract import Service_Abstract

class Service_Customer(Service_Abstract):
    def __init__(self):
        pass

    def scrapeTopReviewer(self, downloadQueue):
        try:
            value = downloadQueue[4]
            try:
                value = value.split(":")
            except Exception as err:
                print (err)
            if (len(value) == 2):
                begin = int(value[0])
                end = int(value[1])
            else:
                begin = 1
                end = int(value[0])
            region = Model_Static_Region().getText(downloadQueue[2])
            self.scraper = Model_Scraper_TopReviewer(region)
            if (begin < 1):
                begin = 1
            if (end > 1000):
                end = 1000
            data = self.scraper.scrape(begin, end+1)

            # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
            amazon = Model_Mapper_Amazon()
            # 连接数据库
            db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
            conn = db.connects()
            mapper = Model_Mapper_Mysql(conn)

            if (data):
                rankBegin = begin * 10 - 9
                rankEnd = end * 10
                sql = amazon.TopReviewer_delete_sql_joint(region, rankBegin, rankEnd)
                mapper.delete(sql)
                for items in data:
                    for item in items:
                        # print (item)
                        sql = amazon.TopReviewer_insert_sql_joint(region, item)
                        mapper.insert(sql)
                return Model_Static_DownloadQueue_Status.SCRAPED
            elif (data == ""):
                return Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA
            else:
                return Model_Static_DownloadQueue_Status.FAILED
        except Exception as err:
            print (err)

    def getAmazonTopReviewerUploadData(self, region, begin, end):
        # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
        amazon = Model_Mapper_Amazon()
        # 连接数据库
        db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        conn = db.connects()
        mapper = Model_Mapper_Mysql(conn)
        rankBegin = begin * 10 - 9
        rankEnd = end * 10
        sql = amazon.TopReviewerUpload_select_sql_joint(region, rankBegin, rankEnd)
        TopReveiwerData = mapper.select(sql)
        # print (TopReveiwerData)
        topreviewer_key = Model_Keys.topreviewer_key
        TopReivew_list = []
        for topreveiwerdata in TopReveiwerData:
            TopReivew_list.append(dict(zip(topreviewer_key, topreveiwerdata)))
        if (TopReivew_list):
            return TopReivew_list
        return False