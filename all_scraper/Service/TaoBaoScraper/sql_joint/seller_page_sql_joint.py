#-*-coding:utf-8*-

# sql语句插入拼接
def sellerpage_insert_sql_joint(data):
    k = []
    v = []
    #以下为插入taobao_seller_page的字段
    try:
        for key, value in data.items():
            if (value != "" and key!="seller_id"):
                if(key=='seller_name' or key=='seller_location' or key=='last_update_time' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif (key == 'seller_page_link' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'seller_credit' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("卖家信用：", "").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'seller_conform' or key == 'seller_service' or key == 'seller_logistics' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'favorable_rate' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("好评率：", "").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'csspeed' or key == 'csrate' or key == 'dispute_rate' or key == 'penalty_num' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("天", "").replace("次", "").replace("\n", "").strip()
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
        sql = "insert into All_Scraper.taobao_seller_page(" + sql_key + ")VALUES(" + sql_value + ")"
        return sql
    except Exception as err:
        print err