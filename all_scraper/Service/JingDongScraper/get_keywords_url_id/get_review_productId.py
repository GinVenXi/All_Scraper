#-*-coding:utf-8*-
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation


class get_review_productId():
    # 这里获取的是productId
    # 评论(json)页的url拼接为https://sclub.jd.com/comment/productPageComments.action?productId=4265472&score=0&sortType=5&page=1&pageSize=10
    def get_review_ProductId(self):
        try:
            Product_Id = []
            # 连接数据库
            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            # 将url提取出来
            sql_get_ProductId_url = "SELECT sku FROM All_Scraper.jd_keywords;"
            Product_Id = mapper.select(sql_get_ProductId_url)
            conn.commit()
            conn.close()
            return Product_Id
        except Exception as err:
            print err