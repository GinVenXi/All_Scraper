#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17:08
'''
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Mysql import Model_Mapper_Mysql

class Model_DbTable_Abstract(object):
    def __init__(self):

        # 数据库初始化，判断数据有效性，然后对数据进行后续操作
        # 连接数据库
        self.db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
        conn = self.db.connects()
        self.mapper = Model_Mapper_Mysql(conn)
        self.amazon = Model_Mapper_Amazon()
