#-*-coding:utf-8*-
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation

# 从关键词页抓取到的数据库表中提取产品页的url
class get_Products_Url():

    def get_Product_url(self):
        try:
            Product_url = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_Product_url = "SELECT product_id FROM taobao_keywords;"
            Product_url = mapper.select(sql_get_Product_url)
            conn.commit()
            conn.close()
            return Product_url
        except Exception as err:
            print err