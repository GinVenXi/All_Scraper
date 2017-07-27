# -*-coding:utf-8-*-
# -*- coding:utf-8 -*-

import time
import re
import sys
import urllib
from Service.JingDongScraper.get_keywords_url_id.get_keywords import get_keywords
from Service.JingDongScraper.get_text.get_text import get_text
from Service.JingDongScraper.get_text.get_text import login_jd
from Service.JingDongScraper.analysis.keywords_analysis import keywords_analysis
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation
from Service.JingDongScraper.sql_joint.keyword_sql_joint import keywords_insert_sql_joint

class keywords_scrape():
    def KEYWORDS_SCRAPE(self):
        try:
            start_time = time.clock()
            # 初始化
            item_keywords = get_keywords()
            # 调用类中函数
            item_keywords_1 = item_keywords.get_keywords()
            # 初始化
            login = login_jd()
            login.login_JD()
            depth = 21

            for keyword in item_keywords_1:
                keyword = keyword[0].encode("utf-8")
                # 利用正则表达式将keyword中的英文字母去掉，只留汉字
                J = re.sub('[A-Za-z0-9\[\`\~\!\@\-\.\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]',
                           '', keyword)
                # 解码成utf-8形式，防止在网页中输入url产生乱码
                S = urllib.quote(J.decode(sys.stdin.encoding).encode('utf8'))
                # print S
                for i in range(depth):
                    if (i % 2 != 0):
                        url = 'https://search.jd.com/Search?keyword=' + str(S) + '&page=' + str(i) + '&enc=utf-8'
                        # print url
                        # 初始化
                        html = get_text()
                        # 调用函数
                        html_1 = html.get_html_text(url)
                        if (html_1):
                            # 初始化
                            processor = keywords_analysis()
                            data = processor.process(html_1, i / 2, J)
                            if (data):
                                # 连接数据库
                                db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                                conn = db.connects()
                                mapper = DB_operation(conn)
                                for jd in data:
                                    # sql=keyword_sql_joint()
                                    (sql_1) = keywords_insert_sql_joint(jd)
                                    print sql_1
                                    mapper.insert(sql_1)
                                conn.commit()
                                conn.close()
            all_time = (time.clock() - start_time)
            print ("total time is:", all_time)
        except Exception as err:
            print err