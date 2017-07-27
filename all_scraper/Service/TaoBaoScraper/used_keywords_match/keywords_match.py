#-*-coding:utf-8*-
from db_operation.db_connection import DB_connection
from db_operation.db_operation import DB_operation
import re
import urllib
def keywords_match():
    try:
        # 连接数据库
        db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        sql_select_keywords='SELECT keyword FROM Scraper.search_keywords;'
        all_keywords = mapper.select(sql_select_keywords)
        conn.commit()
        conn.close()
        keywords=[]
        for keyword in all_keywords:
            keyword=keyword[0].encode("utf-8")
            J= re.sub('[A-Za-z0-9\[\`\~\!\@\-\.\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]', '',keyword)
            keywords.append(J)
            # S = urllib.quote(J.decode(sys.stdin.encoding).encode('utf8'))
    except Exception as err:
        print err

if __name__ == '__main__':
    keywords_match()