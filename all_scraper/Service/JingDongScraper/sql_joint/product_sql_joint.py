#-*-coding:utf-8*-
import pytz
# 插入数据库sql语句拼接
def products_insert_sql_joint(data):
    k = []
    v = []
    #以下为插入到jd_products数据表的字段
    try:
        for key, value in data.items():
            if(key!="image_url" and value!=""):
                if(key=='sku' or key=='last_update_time' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif(key=='shop_id' or key=='price' or key=='review_count' or key=='shop_score' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif (key == 'shipping' and value != ""):
                    try:
                        value = value.replace("\n", "").strip()
                    except Exception as  err:
                        print err
                elif(key=='sellerpage_url' or key=='shop_link' and value!=""):
                    try:
                        value=value.encode("utf-8").replace("\n","").strip()
                    except Exception as err:
                        print err

                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
    except Exception as err:
        print err
    sql_key = ", ".join(k)
    sql_value = ", ".join(v)
    # 返回拼接的sql语句
    try:
        sql = "insert into All_Scraper.jd_products(" + sql_key + ")VALUES(" + sql_value + ")"
        return sql
    except Exception as err:
        print err


#以下为插入到jd_product_image数据表的字段（image_url）
def products_image_insert_sql_joint(data,image_url):
    m = []
    n = []
    try:
        for key,value in data.items():
            if(key=='sku' or key=='last_update_time' and value!=""):
                value=value.encode("utf-8").strip()
                m.append("`" + key + "`")
                n.append('"' + str(value) + '"')
    except Exception as err:
        print err
    sql_key_1 = ", ".join(m)
    sql_value_1 = ", ".join(n)
    try:
        # sql_1 = "insert into All_Scraper.jd_product_iamge(" + sql_key_1 + ")VALUES(" + sql_value_1 + ")"
        sql_1="insert into All_Scraper.jd_product_image(`image_url`,"+sql_key_1 +") values(" +"'"+str(image_url)+"'"+","+str(sql_value_1)+")"
        return sql_1
    except Exception as err:
        print err