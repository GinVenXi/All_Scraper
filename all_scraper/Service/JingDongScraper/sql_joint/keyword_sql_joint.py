#-*-coding:utf-8*-

# class keyword_sql_joint():
#     # sql语句拼接
def keywords_insert_sql_joint(data):
    k = []
    v = []
    # m = []
    # n = []
    # s = []
    # t = []
    #将下列字段插入到jd_keywords数据表里
    try:
        for key, value in data.items():
            if(key!="title" and key!="shop_name" and key!="shop_id" and key!="price" and key!="review_count" and key!="shop_link" and key!="image_url" and value!=""):
                if (key == "keyword" or key=='sku' and value != ""):
                    # value = value.replace("\"", "\'")
                    value=value.decode("utf-8").encode("utf-8").strip()
                if (key == "productpage_url" or key=='last_update_time' and value != ""):
                    value=value.encode("utf-8").replace("\n","").strip()
                if(key=='page_id' or key=='page_position' and value!=""):
                    value=value
                k.append("`" + key + "`")
                v.append('"' + str(value) + '"')
    except Exception as err:
        print (err)
    sql_key = ", ".join(k)
    sql_value = ", ".join(v)

    # #将下列字段插入到jd_products数据表中
    # try:
    #     for key,value in data.items():
    #         if(key!="keyword"  and key!="productpage_url" and key!="page_id" and key!="page_position" and key!="image_url" and key!="last_update_time" and value!="" ):
    #             if(key=='sku' or key=='title' or key=='shop_name'  and value!=""):
    #                 try:
    #                     value=value.encode("utf-8").strip()
    #                 except Exception as err:
    #                     print err
    #             if(key=='price'  or key=='review_count' or key=='shop_id' and value!=""):
    #                 try:
    #                     value=value.strip()
    #                 except Exception as err:
    #                     print err
                # if (key == 'shop_link' and value != ""):
                #     try:
                #         value=value.encode("utf-8").strip()
                #     except Exception as err:
    #             #         print err
    #             m.append("`" + key + "`")
    #             n.append('"' + str(value) + '"')
    # except Exception as err:
    #     print (err)
    # sql_key1 = ", ".join(m)
    # sql_value1 = ", ".join(n)

    # #将下列字段插入到jd_product_image数据表中
    # try:
    #     for key,value in data.items():
    #         if(key=='sku' and value!=""):
    #             value=value.encode("utf-8").strip()
    #         s.append("`" + key + "`")
    #         t.append('"' + str(value) + '"')
    # except Exception as err:
    #     print err
    # sql_key2 = ", ".join(s)
    # sql_value2 = ", ".join(t)


    try:
        # 插入到jd_keywords中的sql语句
        sql = 'insert into All_Scraper.jd_keywords(' + sql_key + ') VALUES (' + sql_value + ')'
        # #插入到jd_products数据表中的sql语句
        # sql1= 'insert into All_Scraper.jd_products(' + sql_key1 + ') VALUES (' + sql_value1 + ')'
        # #插入到jd_product_image数据表中的语句
        # sql2='insert into All_Scraper.jd_product_image(' + sql_key2 + ') VALUES (' + sql_value2 + ')'
        return sql
    except Exception as err:
        print (err)

