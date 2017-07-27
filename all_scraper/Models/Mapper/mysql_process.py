#coding: utf-8
import pymysql

from Models.Mapper.Abstract import Model_Mapper_Abstract


class db_mysql(Model_Mapper_Abstract):
    def __init__(self):
        pass

    def insert(self, ASIN):
        try:
            #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn=pymysql.connect(host='localhost', user='root', passwd='123123', db='python_test', port=3306, charset='utf8')
            # 获取一个游标
            cur=conn.cursor()
            #执行插入语句
            cur.execute('insert into asin_list(region, asin, status) VALUES ("com", %s, "0")', ASIN)
            #提交
            conn.commit()
            #关闭游标
            cur.close()
            # 释放数据库资源
            conn.close()
        except Exception as err:
            print(err)

    def delete(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', passwd='123123', db='python_test', port=3306, charset='utf8')
            cur = conn.cursor()
            cur.execute('delete from asin_list where status = 2')
            conn.commit()
            cur.close()
            conn.close()
        except Exception as err:
            print(err)

    def update(self, ASIN):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='localhost', user='root', passwd='123123', db='python_test', port=3306,
                                   charset='utf8')
            # 获取一个游标
            cur = conn.cursor()
            # 执行插入语句
            cur.execute('update asin_list set status = 0 where asin = %s', ASIN)
            # 提交
            conn.commit()
            # 关闭游标
            cur.close()
            # 释放数据库资源
            conn.close()
        except Exception as err:
            print(err)

    def update_error(self, ASIN):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='localhost', user='root', passwd='123123', db='python_test', port=3306,
                                   charset='utf8')
            # 获取一个游标
            cur = conn.cursor()
            # 执行插入语句
            cur.execute('update asin_list set status = 2 where asin = %s', ASIN)
            # 提交
            conn.commit()
            # 关闭游标
            cur.close()
            # 释放数据库资源
            conn.close()
        except Exception as err:
            print(err)

    def query(self):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='localhost', user='root', passwd='123123', db='python_test', port=3306,
                                   charset='utf8')
            # 获取一个游标
            cur = conn.cursor()
            # 执行查询语句
            cur.execute('select asin from asin_list where status = 1')
            # 返回数据
            data = cur.fetchall()
            # return data
            ASIN = []
            for d in data:
                # #注意int类型需要使用str函数转义
                ASIN.append(str(d[0]))
            return ASIN
            #     # print("ASIN: " + ASIN)
            # # 关闭游标
            cur.close()
            # 释放数据库资源
            conn.close()
        except Exception as err:
            print(err)

# # 读取文件中ASIN并插入到数据库中
# asin_file = open('/home/javen/data/sqlresult_1101830.csv', 'r')
# asin = asin_file.read()
# data = []
# data.append(asin.split('\n'))
# for i in range(len(data[0])):
#     ASIN = data[0][i]
#     print(ASIN)
#     try:
#         insert(str(ASIN))
#     except Exception as err:
#         print(err)