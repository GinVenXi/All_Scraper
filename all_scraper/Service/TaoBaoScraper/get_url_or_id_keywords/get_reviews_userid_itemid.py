#-*-coding:utf-8*-
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation

class get_reviews():
    def get_reviews_userid_itemid(self):
        try:
            User_id = []
            itemId = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将seller_id提取出来
            sql_get_User_id = "SELECT seller_id FROM taobao_keywords;"
            # 将product_id提取出来
            sql_get_itemId = "select product_id from taobao_keywords;"
            User_id = mapper.select(sql_get_User_id)
            itemId = mapper.select(sql_get_itemId)
            conn.commit()
            conn.close()
            return User_id, itemId
        except Exception as err:
            print err