#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.DbTable.Tencent.Abstract import Model_DbTable_Tencent_Abstract

class Model_Mapper_Tencent_Abstract(object):
    def __init__(self):
        self.dbTable = Model_DbTable_Tencent_Abstract()
        self.mapper = self.dbTable.mapper
        self.tencent = self.dbTable.tencent
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
        if (table == "tencent_download_queue"):
            sql = self.tencent.downloadQueue_update(data)
            result = self.mapper.update(sql)
        elif (table == "tencent_pages"):
            sql = self.tencent.tencentPages_update(data)
            result = self.mapper.update(sql)
        return result

    def insert(self, table=None, data=None, searchData=None):
        if (table == "tencent_download_queue"):
            sql = self.tencent.downloadQueue_insert(data)
            result = self.mapper.insert(sql)
        elif (table == "tencent_pages"):
            sql = self.tencent.tencentPages_insert(data)
            result = self.mapper.insert(sql)

        return result

    def delete(self, table=None, searchData=None):
        pass
