#-*-coding:utf-8*-
import time
from Service.JingDongScraper.get_keywords_url_id.get_review_productId import get_review_productId
from Service.JingDongScraper.get_text.get_text import get_text
from Service.JingDongScraper.analysis.reviews_analysis import reviews_analysis
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation
from Service.JingDongScraper.sql_joint.review_sql_joint import reviews_insert_sql_joint


# def main():
#     try:
#         start_time = time.clock()
#         item_ProductId = get_review_productId()
#         item_ProductId_1=item_ProductId.get_review_ProductId()
#         for product_id in item_ProductId_1:
#             print product_id[0]
#             for i in range(20):
#                 latestUrl = "https://sclub.jd.com/comment/productPageComments.action?productId=" + product_id[0] + "&score=0&sortType=5&page=" + str(i) + "&pageSize=10"
#                 html = get_text()
#                 html_1=html.get_json_text(latestUrl)
#                 if (html_1):
#                     processor = reviews_analysis()
#                     jsontext = processor.process(html_1, latestUrl)
#                     if (jsontext):
#                         # 连接数据库
#                         db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                         conn = db.connects()
#                         mapper = DB_operation(conn)
#                         for jdreview in jsontext:
#                             # sql_reviews_insert = review_sql_joint()
#                             sql_reviews_insert_1=reviews_insert_sql_joint(jdreview)
#                             print sql_reviews_insert_1
#                             mapper.insert(sql_reviews_insert_1)
#                         conn.commit()
#                         conn.close()
#
#     except Exception as err:
#         print err
#     all_time = (time.clock() - start_time)
#     print ("total time is:", all_time)
#
#     # #以下代码为单个网页的测试代码
#     # try:
#     #      # url='https://sclub.jd.com/comment/productPageComments.action?productId=11598704&score=0&sortType=3&page=3&pageSize=10'
#     #     url='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2327&productId=4265472&score=0&sortType=5&page=1&pageSize=10'
#     #     json_text=getJsonText(url)
#     #     try:
#     #         if(json_text):
#     #             processor=Model_Processor_Jd_Review_Base()
#     #             json_data=processor.process(json_text,url)
#     #             if(json_data):
#     #                 print type(json_data)
#     #     except Exception as err:
#     #         print err
#     # except Exception as err:
#     #     print err
#
# if __name__ == '__main__':
#     main()


class product_review_scrape():

    def PRODUCT_REVIEW_SCRAPE(self):
        try:
            start_time = time.clock()
            item_ProductId = get_review_productId()
            item_ProductId_1 = item_ProductId.get_review_ProductId()
            for product_id in item_ProductId_1:
                print product_id[0]
                for i in range(20):
                    latestUrl = "https://sclub.jd.com/comment/productPageComments.action?productId=" + product_id[
                        0] + "&score=0&sortType=5&page=" + str(i) + "&pageSize=10"
                    html = get_text()
                    html_1 = html.get_json_text(latestUrl)
                    if (html_1):
                        processor = reviews_analysis()
                        jsontext = processor.process(html_1, latestUrl)
                        if (jsontext):
                            # 连接数据库
                            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                            conn = db.connects()
                            mapper = DB_operation(conn)
                            for jdreview in jsontext:
                                # sql_reviews_insert = review_sql_joint()
                                sql_reviews_insert_1 = reviews_insert_sql_joint(jdreview)
                                print sql_reviews_insert_1
                                mapper.insert(sql_reviews_insert_1)
                            conn.commit()
                            conn.close()

        except Exception as err:
            print err
        all_time = (time.clock() - start_time)
        print ("total time is:", all_time)