#-*-coding:utf-8*-
import pytz
import datetime


def product_update_sql_joint(data,product_id):
    tz = pytz.timezone('Asia/Shanghai')
    last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    k=[]
    v=[]
    try:
        for key,value in data.items():
            if (key != 'product_id' and key != 'title' and key != 'shop_name' and key != 'shop_location' and key != 'current_price' and key != 'sell_count' and key != 'shop_link' and value != ''):
                if (key == 'before_price' or key == ' discription' or key == 'service' or key == 'logistics' or key == 'collect_count' or key == 'review_count' and value != ""):
                    try:
                        value = value.encode("utf-8").strip()
                    except Exception as err:
                        print err
                if (key == 'sellerpage_url' and value != ""):
                    try:
                        value = value.encode("utf-8").replace("\n", "").strip()
                    except Exception as err:
                        print err
            k.append('`' + key + '`' + '=' + '"' + str(value).encode('utf-8') + '"')
    except Exception as err:
        print err
    v=",".join(k)
    # 返回拼接的sql语句
    try:
        if (len(v) > 0):
            sql = 'update All_Scraper.taobao_products set last_update_time=' + '"' + last_update_time + '"' + ',' + str(v) + 'WHERE product_id=' + '"' + product_id + '"'
            return sql
    except Exception as err:
        print err
