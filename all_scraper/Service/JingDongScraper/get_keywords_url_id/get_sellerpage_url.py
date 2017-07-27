#-*-coding:utf-8*-
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation

class get_Seller_Page_Url():
    def get_sellerpage_Url(self):
        try:
            sellerpage_Url = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_sellerpage_Url = "SELECT shop_id FROM All_Scraper.jd_products;"
            sellerpage_Url = mapper.select(sql_get_sellerpage_Url)
            conn.commit()
            conn.close()
            return sellerpage_Url
        except Exception as err:
            print err