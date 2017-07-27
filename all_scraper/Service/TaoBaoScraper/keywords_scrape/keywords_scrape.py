#-*-coding:utf-8*-
from Service.TaoBaoScraper.get_text.get_text import login_taobao
from Service.TaoBaoScraper.get_text.get_text import get_text
from Service.TaoBaoScraper.analysis.keywords_analysis import keywords_analysis
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation
from Service.TaoBaoScraper.sql_joint.keywords_sql_joint import keywords_insert_sql_joint
from Service.TaoBaoScraper.get_url_or_id_keywords.get_keywords import get_keywords
import time
import urllib
import re
import sys
from selenium import webdriver

# def main():
#     try:
#         start_time = time.clock()
#         #获取keywords
#         item_keywords=get_keywords()
#         item_keywords_1=item_keywords.get_keywords()
#         # # #登录淘宝
#         # login=login_taobao()
#         # login.login_taobao()
#
#         #抓取淘宝的页数
#         depth=20
#         for keyword in item_keywords_1:
#             #利用正则表达式对keyword进行处理，将英文字母进行处理
#             keyword=keyword[0].encode("utf-8")
#             J = re.sub('[A-Za-z0-9\[\`\~\!\@\-\.\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]', '',keyword)
#             S = urllib.quote(J.decode(sys.stdin.encoding).encode('utf8'))
#             for page in range(depth):
#                 #拼接url
#                 url='https://s.taobao.com/search?q='+str(S)+'&s='+str(44*page)
#                 print url
#                 #获取网页源码
#                 get_keywords_text=get_text()
#                 keywords_text=get_keywords_text.get_html_text(url)
#                 if(keywords_text):
#                     #解析
#                     processor=keywords_analysis()
#                     data=processor.process(keywords_text,page,J)
#                     if(data):
#                         # 连接数据库
#                         db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                         conn = db.connects()
#                         mapper = DB_operation(conn)
#                         for taobao_keywords in data:
#                             sql_joint=keywords_insert_sql_joint(taobao_keywords)
#                             print sql_joint
#                             mapper.insert(sql_joint)
#                         conn.close()
#         all_time = (time.clock() - start_time)
#         print ("total time is:", all_time)
#     except Exception as err:
#         print err
#
#         #以下代码为针对单一商品iphone的代码
#         # # 商品相关
#         # goods = "iphone"
#         # depth = 20
#         # start_url = "https://s.taobao.com/search?q=" + goods
#         # for i in range(depth):
#         #     try:
#         #         url = start_url + '&s=' + str(44 * i)
#         #         print ("###################################################################")
#         #         print url
#         #         get_keywords_text=get_text()
#         #         keywords_text=get_keywords_text.get_html_text(url)
#         #         # html = getHtmlText(url)
#         #         # print html
#         #         if (keywords_text):
#         #             processor = keywords_analysis()
#         #             data= processor.process(keywords_text)
#         #             if (data):
#         #                 # 连接数据库
#         #                 db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'scraper1', 'utf8')
#         #                 conn = db.connects()
#         #                 mapper = DB_operation(conn)
#         #                 for taobao_keywords in data:
#         #                     sql_joint=keywords_insert_sql_joint(taobao_keywords)
#         #                     mapper.insert(sql_joint)
#         #                 # taobao_keywords =mapper.insert(sql)
#         #                 conn.commit()
#         #                 conn.close()
#         #     except:
#         #         continue
# if __name__ == '__main__':
#     main()

class keywords_scrape():
    def KEYWORDS_SCRAPE(self):
        try:
            start_time = time.clock()
            # 获取keywords
            item_keywords = get_keywords()
            item_keywords_1 = item_keywords.get_keywords()
            # # #登录淘宝
            # login=login_taobao()
            # login.login_taobao()

            # 抓取淘宝的页数
            depth = 20
            for keyword in item_keywords_1:
                # 利用正则表达式对keyword进行处理，将英文字母进行处理
                keyword = keyword[0].encode("utf-8")
                J = re.sub('[A-Za-z0-9\[\`\~\!\@\-\.\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]',
                           '', keyword)
                S = urllib.quote(J.decode(sys.stdin.encoding).encode('utf8'))
                get_keywords_text = get_text()
                for page in range(depth):
                    # 拼接url
                    url = 'https://s.taobao.com/search?q=' + str(S) + '&s=' + str(44 * page)
                    print url
                    # 获取网页源码

                    keywords_text = get_keywords_text.get_html_text(url)
                    if (keywords_text):
                        # 解析
                        processor = keywords_analysis()
                        data = processor.process(keywords_text, page, J)
                        if (data):
                            # 连接数据库
                            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                            conn = db.connects()
                            mapper = DB_operation(conn)
                            for taobao_keywords in data:
                                sql_joint = keywords_insert_sql_joint(taobao_keywords)
                                print sql_joint
                                mapper.insert(sql_joint)
                            conn.close()
                get_keywords_text.quit()
            all_time = (time.clock() - start_time)
            print ("total time is:", all_time)
        except Exception as err:
            print err



