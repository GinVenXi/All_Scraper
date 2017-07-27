#-*-coding:utf-8*-

# 评论插入数据库sql语句拼接操作
def reviews_insert_sql_joint(data):
    k = []
    v = []
    try:
        for key, value in data.items():
            if (key != 'id' and value != ''):
                if (key == 'poor_count' or key == 'general_count' or key == 'good_count' or key == 'review_count' or key == 'reviewer_name' or key == 'review_time' and value != ""):
                    try:
                        value = value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                elif (key == 'review_json_link' and value != ''):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
                elif (key == 'review_content' or key == 'product_information' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
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
        sql = "insert into All_Scraper.jd_product_review(" + sql_key + ")VALUES(" + sql_value + ")"
        return sql
    except Exception as err:
        print err
