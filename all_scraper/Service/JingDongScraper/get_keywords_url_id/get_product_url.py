#-*-coding:utf-8*-
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation

class get_product_url():
    # 从keywords页面抓取下来的数据库中提取有用信息拼接产品页url
    def get_Product_Url(self):
        try:
            Product_url = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_Product_url = "SELECT sku FROM jd_keywords;"
            Product_url = mapper.select(sql_get_Product_url)
            conn.commit()
            conn.close()
            return Product_url
        except Exception as err:
            print err
