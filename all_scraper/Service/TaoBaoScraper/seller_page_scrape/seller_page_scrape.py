#-*-coding:utf-8*-
import time

from Service.TaoBaoScraper.analysis.seller_page_analysis import seller_page_analysis
# from crack_code import crack_verification_code
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation
from Service.TaoBaoScraper.get_text.get_text import get_text
from Service.TaoBaoScraper.get_text.get_text import login_taobao
from Service.TaoBaoScraper.get_url_or_id_keywords.get_sellerpage_url import get_seller_page_url
from Service.TaoBaoScraper.sql_joint.seller_page_sql_joint import sellerpage_insert_sql_joint
from Service.TaoBaoScraper.get_text.get_text import crack_verification_code

#
# def main():
#     start_time = time.clock()
#     try:
#         #从products数据库中取出所需url
#         item_sellerpage_url = get_seller_page_url()
#         item_sellerpage_url_1=item_sellerpage_url.get_seller_page_url()
#         # url='https://rate.taobao.com/user-rate-35f0d4bbc2cee87d3f17c85317b48901.htm'
#         #登录淘宝
#         # login=login_taobao()
#         # login.login_taobao()
#
#         for sellerpage_url in item_sellerpage_url_1:
#             if sellerpage_url[0] == None:
#                 continue
#             print sellerpage_url[0]
#             if (len(sellerpage_url) > 0):
#                #获取网页源代码
#                 html = get_text()
#                 html_1=html.get_html_text(sellerpage_url[0])
#                 lasthtml = html_1.encode("utf-8")
#                 #判断是否出现图片验证码,如果出现,破解验证码,并对用户提示
#                 #然后再进行后续工作
#                 if (lasthtml.find("SecurityMatrix") != -1 or lasthtml.find("验证码：") != -1):
#                     print ("出现图片验证码！")
#                     time.sleep(5)
#                     crack= crack_verification_code()
#                     cracked_html=crack.crack_Verification_Code(html_1)
#                     time.sleep(3)
#                     if(cracked_html):
#                         processor = seller_page_analysis()
#                         data = processor.process(cracked_html, sellerpage_url[0])
#                         if (data):
#                             # 连接数据库
#                             db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                             conn = db.connects()
#                             mapper = DB_operation(conn)
#                             for i in data:
#                                 sql_insert = sellerpage_insert_sql_joint(i)
#                                 print sql_insert
#                                 mapper.insert(sql_insert)
#                             conn.commit()
#                             conn.close()
#                 else:
#                     #如果没有验证码
#                     if (html_1):
#                         #解析
#                         processor = seller_page_analysis()
#                         data = processor.process(html_1, sellerpage_url[0])
#                         if (data):
#                             # 连接数据库
#                             db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                             conn = db.connects()
#                             mapper = DB_operation(conn)
#                             for i in data:
#                                 #将数据插入数据库
#                                 sql_insert=sellerpage_insert_sql_joint(i)
#                                 print sql_insert
#                                 mapper.insert(sql_insert)
#                             conn.commit()
#                             conn.close()
#     except Exception as err:
#         print err
#     all_time = (time.clock() - start_time)
#     print ("total time is:", all_time)
#
# if __name__ == '__main__':
#     main()

class seller_page_scrape():
    def SELLER_PAGE_SCRAPE(self):
        start_time = time.clock()
        try:
            # 从products数据库中取出所需url
            item_sellerpage_url = get_seller_page_url()
            item_sellerpage_url_1 = item_sellerpage_url.get_seller_page_url()
            # url='https://rate.taobao.com/user-rate-35f0d4bbc2cee87d3f17c85317b48901.htm'
            # 登录淘宝
            # login=login_taobao()
            # login.login_taobao()

            for sellerpage_url in item_sellerpage_url_1:
                if sellerpage_url[0] == None:
                    continue
                print sellerpage_url[0]
                if (len(sellerpage_url) > 0):
                    # 获取网页源代码
                    html = get_text()
                    html_1 = html.get_html_text(sellerpage_url[0])
                    lasthtml = html_1.encode("utf-8")
                    # 判断是否出现图片验证码,如果出现,破解验证码,并对用户提示
                    # 然后再进行后续工作
                    if (lasthtml.find("SecurityMatrix") != -1 or lasthtml.find("验证码：") != -1):
                        print ("出现图片验证码！")
                        time.sleep(5)
                        crack = crack_verification_code()
                        cracked_html = crack.crack_Verification_Code(html_1)
                        time.sleep(3)
                        if (cracked_html):
                            processor = seller_page_analysis()
                            data = processor.process(cracked_html, sellerpage_url[0])
                            if (data):
                                # 连接数据库
                                db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                                conn = db.connects()
                                mapper = DB_operation(conn)
                                for i in data:
                                    sql_insert = sellerpage_insert_sql_joint(i)
                                    print sql_insert
                                    mapper.insert(sql_insert)
                                conn.commit()
                                conn.close()
                    else:
                        # 如果没有验证码
                        if (html_1):
                            # 解析
                            processor = seller_page_analysis()
                            data = processor.process(html_1, sellerpage_url[0])
                            if (data):
                                # 连接数据库
                                db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                                conn = db.connects()
                                mapper = DB_operation(conn)
                                for i in data:
                                    # 将数据插入数据库
                                    sql_insert = sellerpage_insert_sql_joint(i)
                                    print sql_insert
                                    mapper.insert(sql_insert)
                                conn.commit()
                                conn.close()
        except Exception as err:
            print err
        all_time = (time.clock() - start_time)
        print ("total time is:", all_time)
