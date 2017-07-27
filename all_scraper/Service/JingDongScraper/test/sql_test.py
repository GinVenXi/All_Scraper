#-*-coding:utf-8*-

from db_operation.db_connection import DB_connection
from db_operation.db_operation import DB_operation

def main():
    db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
    conn = db.connects()
    mapper = DB_operation(conn)
    sql_select_sku_shop_id = 'SELECT sku,shop_id FROM All_Scraper.jd_products;'
    result = mapper.select(sql_select_sku_shop_id)
    for item in result:
        sku=item[0]
        shop_id=item[1]
        print sku
        print shop_id
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()