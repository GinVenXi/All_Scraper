#-*-coding:utf-8*-

# sql语句拼接函数
def product_insert_sql_joint(data):
    k = []
    v = []

    #以下字段插入到taobao_products数据表
    try:
        for key, value in data.items():
            if (value != ""  and key!='in_stock' and key!='image_url' ):

                if (key == 'review_count' or key == 'discription' or key == 'service' or key == 'logistics' or key == 'before_price' or key=='current_price' or key=='sell_count' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'collect_count' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("(", "").replace(")", "").replace("人气", "").strip()
                    except Exception as err:
                        print err
                elif (key=='product_id' or key=='last_update_time' and value != ""):
                    try:
                        value = value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif(key=='title'and value!=""):
                    try:
                        value=value.encode("utf-8").replace("\n","").strip()
                    except Exception as err:
                        print err
                elif(key=='shop_link' or key=='sellerpage_url' and value!=""):
                    try:
                        value=value.encode("utf-8").replace("\n","").strip()
                    except Exception as err:
                        print err
                elif(key == 'shipping' or key=='shop_location' or key=='shop_name' and value!=""):
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
        #插入taobao_products表中的sql语句
        sql = "insert into All_Scraper.taobao_products(" + sql_key + ")VALUES(" + str(sql_value) + ")"
        print (sql)
        return sql
    except Exception as err:
        print err


# 以下字段插入到taobao_product_image数据表
def product_image_insert_sql_joint(singleurl,data):
    k = []
    v = []
    try:
        for key,value in data.items():
                if(key=='last_update_time' or key=='product_id' and value!=""):
                    value=value.strip()
                    k.append("`" + key + "`")
                    v.append('"' + str(value) + '"')
                else:
                    pass

    except Exception as err:
        print err
    sql_key = ", ".join(k)
    sql_value = ", ".join(v)
    # url=singleurl.encode("utf-8")
    # url="".join(singleurl.encode("utf-8"))
    sql = "insert into All_Scraper.taobao_product_image(`image_url`,"+sql_key +") values(" +"'"+str(singleurl)+"'"+","+str(sql_value)+")"
    # print (sql)
    return sql


#注明：此处并没有把product_id和last_update_time两个字段插入到taobao_products数据表中
#没有把product_id插入到taobao_product_image里面
#product_id需要从downloadquene里取出,last_update_time稍后处理