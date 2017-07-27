#-*-coding:utf-8*-
import time
from Service.JingDongScraper.get_keywords_url_id.get_sellerpage_url import get_Seller_Page_Url
from Service.JingDongScraper.get_text.get_text import get_text
from Service.JingDongScraper.analysis.seller_page_analysis import seller_page_analysis
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation
from Service.JingDongScraper.sql_joint.seller_page_sql_joint import sellerpage_insert_sql_joint
from Service.JingDongScraper.get_text.get_text import login_jd

# def main():
#     try:
#         start_time = time.clock()
#         #获取拼接url的shop_id(https://mall.jd.com/shopLevel-shop_id.html)
#         item_sellerpage = get_Seller_Page_Url()
#         item_sellerpage_1=item_sellerpage.get_sellerpage_Url()
#         #登录京东
#         login=login_jd()
#         login.login_JD()
#         if (len(item_sellerpage_1) > 0):
#             for sellerpage in item_sellerpage_1:
#                 try:
#                     print (sellerpage[0])
#                     if (sellerpage[0] == None):
#                         continue
#                 except:
#                     continue
#                 #拼接sellerpage页面的url
#                 sellerpage_url="https:"+"//mall.jd.com/shopLevel-"+sellerpage[0]+".html"
#                 #获取页面的网页源代码
#                 html = get_text()
#                 html_1=html.get_html_text_1(sellerpage_url)
#                 if (html_1):
#                     #对源代码进行解析,提取
#                     processor = seller_page_analysis()
#                     sellerpage_text = processor.process(html_1,sellerpage_url,sellerpage[0])
#                     if (sellerpage_text):
#                         # 连接数据库
#                         db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                         conn = db.connects()
#                         mapper = DB_operation(conn)
#                         for i in sellerpage_text:
#                             #将数据插入jd_seller_page数据表中
#                             sql_sellerpage_insert_1=sellerpage_insert_sql_joint(i)
#                             print sql_sellerpage_insert_1
#                             mapper.insert(sql_sellerpage_insert_1)
#                         #关闭数据库连接
#                         conn.commit()
#                         conn.close()
#     except Exception as err:
#         print err
#
#
#
#         # 以下为针对单个网址的代码
#         # try:
#         #     url = 'https://mall.jd.com/shopLevel-643810.html'
#         #     html = getHtmlText(url)
#         #     if (html):
#         #         processor = Model_Processor_Jd_Seller_Base()
#         #         data = processor.process(html)
#         #         if (data):
#         #             print data
#         #             db = sqlConnect('localhost', 3306, 'root', 'bwx0605', 'JD_scraper', 'utf8')
#         #             conn = db.connects()
#         #             mapper = Mysql(conn)
#         #             sql_sellerpage_insert = sellerpage_insert_sql_joint(data[0])
#         #             print sql_sellerpage_insert
#         #             mapper.insert(sql_sellerpage_insert)
#         #             conn.commit()
#         #             conn.close()
#         # except Exception as err:
#         #     print err
#
# if __name__ == '__main__':
#     main()

class seller_page_scrape():
    def SELLER_PAGE_SCRAPE(self):
        try:
            start_time = time.clock()
            # 获取拼接url的shop_id(https://mall.jd.com/shopLevel-shop_id.html)
            item_sellerpage = get_Seller_Page_Url()
            item_sellerpage_1 = item_sellerpage.get_sellerpage_Url()
            # 登录京东
            login = login_jd()
            login.login_JD()
            if (len(item_sellerpage_1) > 0):
                for sellerpage in item_sellerpage_1:
                    try:
                        print (sellerpage[0])
                        if (sellerpage[0] == None):
                            continue
                    except:
                        continue
                    # 拼接sellerpage页面的url
                    sellerpage_url = "https:" + "//mall.jd.com/shopLevel-" + sellerpage[0] + ".html"
                    # 获取页面的网页源代码
                    html = get_text()
                    html_1 = html.get_html_text_1(sellerpage_url)
                    if (html_1):
                        # 对源代码进行解析,提取
                        processor = seller_page_analysis()
                        sellerpage_text = processor.process(html_1, sellerpage_url, sellerpage[0])
                        if (sellerpage_text):
                            # 连接数据库
                            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                            conn = db.connects()
                            mapper = DB_operation(conn)
                            for i in sellerpage_text:
                                # 将数据插入jd_seller_page数据表中
                                sql_sellerpage_insert_1 = sellerpage_insert_sql_joint(i)
                                print sql_sellerpage_insert_1
                                mapper.insert(sql_sellerpage_insert_1)
                            # 关闭数据库连接
                            conn.commit()
                            conn.close()
        except Exception as err:
            print err