#-*-coding:utf-8*-
import pymysql

#数据库连接操作
class DB_connection():
    def __init__(self,host,port,user,passwd,db,charset='utf8'):
        self.conn = pymysql.connect(host = host , port = port , user = user , passwd = passwd , db = db , charset = charset)
    def connects(self):
        return self.conn
    #关闭mysql连接
    def close(self):
        self.conn.close()
