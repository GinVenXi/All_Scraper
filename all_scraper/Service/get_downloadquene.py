# -*-coding:utf-8*-
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation


def get_JD_download_Queue():
    try:
        # 连接数据库
        db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        sql="SELECT * FROM jingdong_downloadqueue ;"
        result=mapper.select(sql)
        conn.commit()
        conn.close()
        return result
    except Exception as err:
        print err


def get_TaoBao_download_Quene():
    try:
        # 连接数据库
        db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        sql="SELECT * FROM taobao_downloadqueue ;"
        result=mapper.select(sql)
        conn.commit()
        conn.close()
        return result
    except Exception as err:
        print err

