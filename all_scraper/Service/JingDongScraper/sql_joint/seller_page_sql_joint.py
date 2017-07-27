#-*-coding:utf-8*-

# 插入数据库语句拼接
def sellerpage_insert_sql_joint(data):
    k = []
    v = []
    try:
        for key, value in data.items():
            if (key != 'id' and key != 'seller_page_link' and value != ""):
                if (key == 'seller_quality' or key == 'seller_total' or key == 'seller_speed' or key == 'seller_processtime' or key == 'seller_attitude' or key == 'seller_hegui' or key == 'seller_discription' or key == 'seller_dispute' or key == 'seller_rework' or key == 'seller_return' or key=='seller_id' and value != ""):
                    try:
                        value = value.decode("utf-8").encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif (key == 'seller_logo_url' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'seller_name' or key == 'seller_location' and value != ""):
                    try:
                        value = value.decode("utf-8").encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif (key=='last_update_time' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
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
        sql = "insert into All_Scraper.jd_seller_page(" + sql_key + ")VALUES(" + sql_value + ")"
        return sql
    except Exception as err:
        print err
