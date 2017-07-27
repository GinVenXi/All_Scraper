#-*-coding:utf-8*-
from db_operation.db_connection import DB_connection
from db_operation.db_operation import DB_operation
from sql_joint.product_update_sql_joint import products_update_sql_joint
from sql_joint.product_update_sql_joint import products_update_sql_joint_1
from sql_joint.product_sql_joint import products_insert_sql_joint

#根据shop_id来确定唯一一条记录
def products_update_select(shop_id):
    # 从jd_products表中选出sku和shop_id两个字段所对应的值
    # 因为jd_products表中的一部分字段的数据是从jd_keywords解析之后插入到jd_products表中
    # 所以我们要对jd_products中的数据进行更新操作（由shop_name,shop_id,shop_name即可确认唯一一条记录）
    # 如果存在则直接更新剩余空闲字段,如果不存在则插入新的一条记录
    # 数据库连接及更新操作
    try:
        db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        sql_select_shop_id = 'SELECT shop_id FROM All_Scraper.jd_products where `shop_id`=' + shop_id
        result = mapper.select(sql_select_shop_id)
        return result
    except Exception as err:
        print err

#根据shop_name来确定唯一一条记录
def products_update_select_1(shop_name):
        # 从jd_products表中选出sku和shop_id两个字段所对应的值
        # 因为jd_products表中的一部分字段的数据是从jd_keywords解析之后插入到jd_products表中
        # 所以我们要对jd_products中的数据进行更新操作（由shop_name,shop_id,shop_name即可确认唯一一条记录）
        # 如果存在则直接更新剩余空闲字段,如果不存在则插入新的一条记录
        # 数据库连接及更新操作
        try:
            db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            sql_select_shop_id = 'SELECT shop_id FROM All_Scraper.jd_products where `shop_name`=' + shop_name
            result = mapper.select(sql_select_shop_id)
            return result
        except Exception as err:
            print err

#产品页根据shop_id更新数据
def products_update_operation(data,shop_id):
    try:
        db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        sql_update_joint = products_update_sql_joint(data, shop_id)
        print ("##################################################")
        print sql_update_joint
        mapper.update(sql_update_joint)
        conn.commit()
        conn.close()
    except Exception as err:
        print err

#产品页根据shop_name更新数据
def products_update_operation_1(data, shop_name):
        try:
            db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
            conn = db.connects()
            mapper = DB_operation(conn)
            sql_update_joint = products_update_sql_joint_1(data, shop_name)
            print ("##################################################")
            print sql_update_joint
            mapper.update(sql_update_joint)
            conn.commit()
            conn.close()
        except Exception as err:
            print err


#产品页插入数据库总操作
def products_insert_operation(data):
    try:
        db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
        conn = db.connects()
        mapper = DB_operation(conn)
        (sql_insert_joint,sql_insert_joint_iamge)=products_insert_sql_joint(data)
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print sql_insert_joint
        print sql_insert_joint_iamge
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        mapper.insert(sql_insert_joint)
        mapper.insert(sql_insert_joint_iamge)
        conn.commit()
        conn.close()
    except Exception as err:
        print err