#-*-coding:utf-8*-
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation

class get_seller_page_url():
    def get_seller_page_url(self):
        try:
            Product_url = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_sellerpage_url = "SELECT sellerpage_url FROM All_Scraper.taobao_products;"
            Product_url = mapper.select(sql_get_sellerpage_url)
            conn.commit()
            conn.close()
            return Product_url
        except Exception as err:
            print err