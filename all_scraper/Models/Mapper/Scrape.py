#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-18'
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
from Models.Mapper.Abstract import Model_Mapper_Abstract
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql

class Model_Mapper_Scrape(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_Scrape, self).__init__()
        # # 数据库初始化，判断数据有效性，然后对数据进行后续操作
        # self.amazon = Model_Mapper_Amazon()
        # # 连接数据库
        # self.db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        # self.conn = self.db.connects()
        # self.mapper = Model_Mapper_Mysql(self.conn)

    def save(self, scrape):
        if(scrape['download_queue_id']):
            # print scrape['download_queue_id']
            self.insert("scrape", scrape)
