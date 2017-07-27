#-*-coding:utf-8*-

# 插入数据库语句拼接
def product_review_insert_sql_joint(data):
    # print (data)
    k = []
    v = []
    m = []
    n = []

    #以下为插入到taobao_product_review表的字段
    try:
        for key, value in data.items():
            if (value != "" and key!="image_url"):
                if (key == 'product_information' or key == 'reviewer_name' or key == 'review_content' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\"", "").replace("<b>", "").replace("</b>", "").strip()
                    except:
                        value = value.strip()
                if (key == 'image_count' or key == 'review_time' or key == 'seller_id' or key == 'reviewer_id' or key=='review_count' and value != ""):
                    try:
                        value = value.encode("utf-8").strip()
                    except:
                        # print ("key1 error")
                        pass
                if (key == 'review_json_link' or key=='last_update_time' and value != ""):
                    try:
                        value = value.encode("utf-8").strip()
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
        #插入到taobao_product_review表的字段
        sql = "insert into All_Scraper.taobao_product_review(" + sql_key + ")VALUES(" + sql_value + ")"
        return sql
    except Exception as err:
        print err



def product_review_image_sql_joint(data,imgurl):
    m = []
    n = []
    # 以下为插入到taobao_product_review_image数据表中的字段
    try:
        for key, value in data.items():
            if (key == 'reviewer_name' or key == 'reviewer_id' or key == 'last_update_time' or key=='image_url' and value != ""):
                try:
                    value = value.encode("utf-8").strip()
                except Exception as err:
                    print err
                m.append("`" + key + "`")
                n.append('"' + str(value) + '"')
    except Exception as err:
        print err
    sql_key_1 = ", ".join(m)
    sql_value_1 = ", ".join(n)

    sql = "insert into All_Scraper.taobao_product_review_image(`image_url`," + sql_key_1 + ") values(" + "'" + str(imgurl) + "'" + "," + str(sql_value_1) + ")"
    return sql

