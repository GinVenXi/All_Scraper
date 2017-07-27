#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-16'
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
#mysql 映射类
class Model_Mapper_Mysql():
    def __init__(self,object):
        self.conn = object

    def cur(self):
        cur = self.conn.cursor()
        return cur

    '''
    插入数据
    '''
    def insert(self, sql):
        try:
            cur = self.cur()
            cur.execute(sql)
            # insert_id = int(cur.insert_id())
            self.conn.commit()
            # self.conn.close()
            # return self.conn
            cur.close()
            return True
        except Exception as e:
            print (e)
            self.conn.rollback()

    '''
    删除
    '''
    def delete(self, sql):
        try:
            cur = self.cur()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return True
        except Exception as e:
            print (e)
            self.conn.rollback()

    '''
    更新操作
    '''
    def update(self, sql):
        try:
            cur = self.cur()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return True
        except Exception as e:
            print e
            self.conn.rollback()

    '''
    查找
    '''
    def select(self, sql):
       try:
           cur = self.cur()
           cur.execute(sql)
           result = cur.fetchall()
           cur.close()
           return result
       except:
           print ('mysql error')


