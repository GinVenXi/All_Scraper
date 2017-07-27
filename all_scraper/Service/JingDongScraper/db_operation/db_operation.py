#-*-coding:utf-8*-
import pymysql

#数据库查删增改操作
class DB_operation():

    def __init__(self, object):
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
            self.conn.commit()
            result = cur.fetchall()
            cur.close()
            return result
        except Exception as err:
            print err
            # print ('mysql error')