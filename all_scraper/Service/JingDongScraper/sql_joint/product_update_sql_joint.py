#-*-coding:utf-8*-
import pytz
import datetime
# 更新数据库中数据操作
#根据ship_id更新数据库
def products_update_sql_joint(data,shop_id):
    tz=pytz.timezone('Asia/Shanghai')
    last_update_time=datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    k = []
    v = []
    try:
        for key, value in data.items():
            if (key != 'id' and key!='price' and key!='image_url' and key!='title' and key!='shop_name'  and key!="review_count" and key!='shop_link' and key!='shop_id' and value != ""):
                if(key=='shop_score' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                if (key == 'shipping' and value != ""):
                    try:
                        value = value.replace("\n", "").strip()
                    except Exception as  err:
                        print err
                if(key=='sellerpage_url' and value!=""):
                    try:
                        value=value.encode("utf-8").replace("\n","").strip()
                    except  Exception as err:
                        print err
                k.append('`'+key+'`'+'='+'"'+str(value)+'"')
    except Exception as err:
        print err
    # sql_key = ", ".join(k)
    # sql_value = ", ".join(v)
    v=",".join(k)
    # 返回拼接的sql语句
    try:
        if(len(v)>0):
            sql='update All_Scraper.jd_products set last_update_time='+'"'+last_update_time+'"'+','+str(v)+'WHERE shop_id='+'"'+shop_id+'"'
            return sql
    except Exception as err:
        print err


#根据shop_name更新数据库
def products_update_sql_joint_1(data,shop_name):
    tz=pytz.timezone('Asia/Shanghai')
    last_update_time=datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    k = []
    v = []
    try:
        for key, value in data.items():
            if (key != 'id' and key!='price' and key!='image_url' and key!='title' and key!='shop_name'  and key!="review_count" and key!='shop_link' and key!='shop_id' and value != ""):
                if(key=='shop_score' and value!=""):
                    try:
                        value=value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                if (key == 'shipping' and value != ""):
                    try:
                        value = value.replace("\n", "").strip()
                    except Exception as  err:
                        print err
                if(key=='sellerpage_url' and value!=""):
                    try:
                        value=value.encode("utf-8").replace("\n","").strip()
                    except  Exception as err:
                        print err
                k.append('`'+key+'`'+'='+'"'+str(value)+'"')
    except Exception as err:
        print err
    # sql_key = ", ".join(k)
    # sql_value = ", ".join(v)
    v=",".join(k)
    # 返回拼接的sql语句
    try:
        if(len(v)>0):
            sql='update All_Scraper.jd_products set last_update_time='+'"'+last_update_time+'"'+','+str(v)+'WHERE shop_name='+'"'+shop_name+'"'
            return sql
    except Exception as err:
        print err
