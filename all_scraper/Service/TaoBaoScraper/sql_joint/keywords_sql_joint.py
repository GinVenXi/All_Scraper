#-*-coding:utf-8*-

# sql语句拼接
def keywords_insert_sql_joint(data):
    k = []
    v = []
    # m = []
    # n = []
    # s = []
    # t = []
    # b = []
    # c = []
    #以下字段为插入到taobao_keywords数据表的字段
    try:
        for key, value in data.items():
            if (value != "" and key!="title" and key!="current_price" and key!="sell_count" and key!="shipping" and key!="shop_name" and key!="shop_location" and key!="shop_link" ):

                if (key=='keyword' or key=='seller_id' or key=='last_update_time' and value != ""):
                    try:
                        value = value.decode("utf-8").encode("utf-8").strip()
                    except Exception as err:
                        print err
                if(key=='productpage_url' and value!=""):
                    try:
                        value=value.decode("utf-8").encode("utf-8").replace("\n","").strip()
                    except Exception as err:
                        print err
                if(key=='page_id' or key=='page_position' and value!=""):
                    try:
                        value=value
                    except Exception as err:
                        print err
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
    except Exception as err:
        print err
    sql_key = ", ".join(k)
    sql_value = ", ".join(v)

    # #以下字段为插入到taobao_products数据表中的字段
    # try:
    #     for key,value in data.items():
    #         if(key!="page_id" and key!="page_position" and key!="keyword" and key!="productpage_url" and key!="seller_id" and key!='last_update_time'  and value!=""):
    #             if(key=='current_price' or key=='product_id' and value!=""):
    #                 try:
    #                     value=value.decode("utf-8").encode("utf-8").strip()
    #                 except Exception as err:
    #                     print err
    #             if(key=='title' or key=='shipping' or key=='shop_name' or key=='shop_location' or key=='sell_count' and value !=""):
    #                 try:
    #                     value=value.encode("utf-8").strip()
    #                 except Exception as err:
    #                     print err
    #             if(key=='shop_link' and value!=""):
    #                 try:
    #                     value=value.decode("utf-8").encode("utf-8").strip()
    #                 except Exception as err:
    #                     print err
    #             m.append("`" + key + "`")
    #             n.append('"' + str(value) + '"')
    # except Exception as err:
    #     print err
    # sql_key_1 = ", ".join(m)
    # sql_value_1 = ", ".join(n)
    #
    # #以下字段为插入到taobao_seller_page数据表的字段
    # try:
    #     for key,value in data.items():
    #         if (key != 'product_id' and key != "page_id" and key != "page_position" and key != "keyword" and key != "productpage_url" and key!="last_update_time" and key!="title" and key!="current_price" and key!="sell_count" and key!="shipping" and key!="shop_name" and key!="shop_location" and key!="shop_link" and key!="last_update_time" and value != ""):
    #             if(key=='seller_id' and value!=""):
    #                 try:
    #                     value=value.decode("utf-8").encode("utf-8").strip()
    #                 except Exception as err:
    #                     print err
    #             s.append("`" + key + "`")
    #             t.append('"' + str(value) + '"')
    # except Exception as err:
    #     print err
    # sql_key_2 = ", ".join(s)
    # sql_value_2 = ", ".join(t)
    # #以下字段为插入到taobao_product_image数据表的字段
    # try:
    #     for key,value in data.items():
    #         if(k=='product_id' and value!=''):
    #             try:
    #                 value=value.encode("utf-8").strip()
    #             except Exception as err:
    #                 print err
    #         b.append("`" + key + "`")
    #         c.append('"' + str(value) + '"')
    # except Exception as err:
    #     print err
    # sql_key_3 = ", ".join(b)
    # sql_value_3 = ", ".join(c)

    # 返回拼接的sql语句
    try:
        sql = "insert into All_Scraper.taobao_keywords(" + sql_key + ")VALUES(" + sql_value + ")"
        # sql1="insert into All_Scraper.taobao_products(" + sql_key_1 + ")VALUES(" + sql_value_1 + ")"
        # sql2="insert into All_Scraper.taobao_seller_page(" + sql_key_2 + ")VALUES(" + sql_value_2 + ")"
        # sql3="insert into All_Scraper.taobao_product_image(" + sql_key_3 + ")VALUES(" + sql_value_3 + ")"
        # return (sql,sql1,sql2)
        return sql
    except Exception as err:
        print err