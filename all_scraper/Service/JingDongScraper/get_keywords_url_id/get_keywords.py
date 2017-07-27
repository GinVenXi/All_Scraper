#-*-coding:utf-8*-
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation


class get_keywords():
    def get_keywords(self):
        try:
            keywords = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_keywords = "SELECT keyword FROM All_Scraper.search_keywords limit 100;"
            keywords = mapper.select(sql_get_keywords)
            conn.commit()
            conn.close()
            return keywords
        except Exception as err:
            print err