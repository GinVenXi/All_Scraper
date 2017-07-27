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
import sys
from Models.Processor.Product.Base.Com import Model_Processor_Product_Base_Com
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Mapper.Amazon import Model_Mapper_Amazon
class Model_Mapper_AmazonMysql():
    def open_file(self, region, asin):
        html_content = open('../../../Downloader/Amazon_Data/'+asin+'.html', 'r')
        html = html_content.read()
        html_content.close()
        com = Model_Processor_Product_Base_Com()
        data = com.process(html)
        # print (data['images'][0])
        # sys.exit()
        amazon = Model_Mapper_Amazon()
        sql = amazon.product_sql_joint(region, asin, data)
        print sql
        sys.exit()
        # 连接数据库
        db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        conn = db.connects()
        mapper = Model_Mapper_Mysql(conn)
        mapper.insert(sql)
        conn.close()

if __name__ == "__main__":
    # asin = 'B01NBE22BH'
    # asin = 'B00WGDFG58'
    # asin = 'B01L6NS7EU'
    # asin = 'B01IQPGTR8'
    # asin = 'B00PGQYEUK'
    asin = 'B01M6DT59I'
    region = 'com'
    of = Model_Mapper_AmazonMysql()
    of.open_file(region, asin)