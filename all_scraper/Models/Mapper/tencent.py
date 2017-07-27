#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import pytz

import datetime


class Model_Mapper_Tencent():
    def __init__(self):
        pass

    def downloadQueue_insert(self, data):
        k = []
        v = []
        try:
            for key, value in data.items():
                if (key == "title"):
                    value = str(value).encode("utf-8").replace("\"", "\'")
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        except Exception as err:
            print ("wrong11")
            print (err)
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        try:
            sql = 'insert into tencent_download_queue(' + sql_key + ') VALUES (' + sql_value + ')'
            print (sql)
            return sql
        except Exception as err:
            print ("wrong12")
            print (err)

    def tencentPages_insert(self, data):
        k = []
        v = []
        try:
            for key, value in data.items():
                if (key == "title" or key == "summary" or key == "keywords"):
                    value = str(value).encode("utf-8").replace("\"", "\'")
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
        except Exception as err:
            print ("wrong21")
            print (err)
        sql_key = ", ".join(k)
        sql_value = ", ".join(v)
        try:
            sql = 'insert into tencent_pages(' + sql_key + ') VALUES (' + sql_value + ')'
            print (sql)
            return sql
        except Exception as err:
            print ("wrong22")
            print (err)

    def downloadQueue_update(self, data):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        k = []
        try:
            for key, value in data.items():
                if (key != "url_id" and key != "id" and key != "last_updated_time" and value != ''):
                    if (key == "title"):
                        value = str(value).encode("utf-8").replace("\"", "\'")
                    k.append('`' + key + '`' + '=' + '"' + str(value) + '"')
        except Exception as err:
            print ("wrong31")
            print (err)
        v = " , ".join(k)
        try:
            sql = 'update tencent_download_queue set last_updated_time = ' + '"' + str(last_updated_time) + '"' + ', ' + v + ' WHERE id =' + '"' + str(data['id']) + '"'
            print (sql)
            return sql
        except Exception as err:
            print ("wrong32")
            print (err)

    def tencentPages_update(self, data):
        tz = pytz.timezone('Asia/Shanghai')
        last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        k = []
        try:
            for key, value in data.items():
                if (key != "url_id" and value != ''):
                    if (key == "title" or key == "summary" or key == "keywords"):
                        value = str(value).encode("utf-8").replace("\"", "\'")
                    k.append('`' + key + '`' + '=' + '"' + str(value) + '"')
        except Exception as err:
            print ("wrong41")
            print (err)
        v = " , ".join(k)
        try:
            sql = 'update tencent_pages set last_updated_time = ' + '"' + str(last_updated_time) + '"' + ', ' + v + ' WHERE url_id =' + '"' + str(data['url_id']) + '"'
            print (sql)
            return sql
        except Exception as err:
            print ("wrong42")
            print (err)