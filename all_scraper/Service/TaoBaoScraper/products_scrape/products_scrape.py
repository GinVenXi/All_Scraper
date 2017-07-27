#-*-coding:utf-8*-
import time
from Service.TaoBaoScraper.get_url_or_id_keywords.get_products_url import get_Products_Url
from Service.TaoBaoScraper.get_text.get_text import login_taobao
from Service.TaoBaoScraper.get_text.get_text import get_text
from Service.TaoBaoScraper.analysis.products_analysis import products_analysis
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation
from Service.TaoBaoScraper.sql_joint.product_sql_joint import product_insert_sql_joint
from Service.TaoBaoScraper.get_text.get_text import crack_verification_code
from Service.TaoBaoScraper.sql_joint.product_sql_joint import product_image_insert_sql_joint

# def main():
#     try:
#         start_time = time.clock()
#         #获取product页面的product_id
#         item_sql_Product_id = get_Products_Url()
#         item_sql_Product_id_1=item_sql_Product_id.get_Product_url()
#         #登录淘宝
#         # login=login_taobao()
#         # login.login_taobao()
#         for Product_id in item_sql_Product_id_1:
#             print (Product_id[0])
#             url='https://detail.tmall.com/item.htm?id='+str(Product_id[0])+'&abbucket=0'
#             # 获取到产品页的网页源代码
#             html=get_text()
#             html_1= html.get_html_text(url)
#             html_1_1=html_1.encode("utf-8")
#             #判断是否出现图片验证码
#             if(html_1_1.find("SecurityMatrix") != -1 or html_1_1.find("验证码：") != -1):
#                 print ("出现图片验证码！")
#                 time.sleep(5)
#                 crack=crack_verification_code()
#                 crack.crack_Verification_Code(html_1)
#                 cracked_html=crack.crack_Verification_Code(html_1)
#                 time.sleep(3)
#                 try:
#                     if (cracked_html):
#                         processor = products_analysis()
#                         data2 = processor.process(cracked_html,Product_id[0])
#                         if (data2):
#                             # 连接数据库
#                             db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                             conn = db.connects()
#                             mapper = DB_operation(conn)
#                             for taobao_product in data2:
#                                 sql_taobao_products = product_insert_sql_joint(taobao_product)
#                                 if (taobao_product['image_url']):
#                                     for url in taobao_product['image_url']:
#                                         url = "https:" + url
#                                         sql_taobao_product_image = product_image_insert_sql_joint(url,taobao_product)
#                                         mapper.insert(sql_taobao_product_image)
#                                 mapper.insert(sql_taobao_products)
#                             conn.commit()
#                             conn.close()
#                 except Exception as err:
#                     print err
#             else:
#                 if(html_1):
#                     processor = products_analysis()
#                     data2 = processor.process(html_1,Product_id[0])
#                     if (data2):
#
#                         # 连接数据库
#                         db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                         conn = db.connects()
#                         mapper = DB_operation(conn)
#                         for taobao_product in data2:
#                             sql_taobao_products=product_insert_sql_joint(taobao_product)
#                             if(taobao_product['image_url']):
#                                 for url in taobao_product['image_url']:
#                                     url="https:"+url
#                                     sql_taobao_product_image=product_image_insert_sql_joint(url,taobao_product)
#                                     mapper.insert(sql_taobao_product_image)
#                             mapper.insert(sql_taobao_products)
#                             # (sql_taobao_products,sql_taobao_product_image) = product_insert_sql_joint(i)
#                         conn.commit()
#                         conn.close()
#         all_time = (time.clock() - start_time)
#         print ("total time is:", all_time)
#     except Exception as err:
#         print err
#
# if __name__ == '__main__':
#     main()

class products_scrape():
    def PRODUCTS_SCRAPE(self):
        try:
            start_time = time.clock()
            # 获取product页面的product_id
            item_sql_Product_id = get_Products_Url()
            item_sql_Product_id_1 = item_sql_Product_id.get_Product_url()
            # 登录淘宝
            # login=login_taobao()
            # login.login_taobao()
            for Product_id in item_sql_Product_id_1:
                print (Product_id[0])
                url = 'https://detail.tmall.com/item.htm?id=' + str(Product_id[0]) + '&abbucket=0'
                # 获取到产品页的网页源代码
                html = get_text()
                html_1 = html.get_html_text(url)
                html_1_1 = html_1.encode("utf-8")
                # 判断是否出现图片验证码
                if (html_1_1.find("SecurityMatrix") != -1 or html_1_1.find("验证码：") != -1):
                    print ("出现图片验证码！")
                    time.sleep(5)
                    crack = crack_verification_code()
                    crack.crack_Verification_Code(html_1)
                    cracked_html = crack.crack_Verification_Code(html_1)
                    time.sleep(3)
                    try:
                        if (cracked_html):
                            processor = products_analysis()
                            data2 = processor.process(cracked_html, Product_id[0])
                            if (data2):
                                # 连接数据库
                                db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                                conn = db.connects()
                                mapper = DB_operation(conn)
                                for taobao_product in data2:
                                    sql_taobao_products = product_insert_sql_joint(taobao_product)
                                    if (taobao_product['image_url']):
                                        for url in taobao_product['image_url']:
                                            url = "https:" + url
                                            sql_taobao_product_image = product_image_insert_sql_joint(url,
                                                                                                      taobao_product)
                                            mapper.insert(sql_taobao_product_image)
                                    mapper.insert(sql_taobao_products)
                                conn.commit()
                                conn.close()
                    except Exception as err:
                        print err
                else:
                    if (html_1):
                        processor = products_analysis()
                        data2 = processor.process(html_1, Product_id[0])
                        if (data2):

                            # 连接数据库
                            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                            conn = db.connects()
                            mapper = DB_operation(conn)
                            for taobao_product in data2:
                                sql_taobao_products = product_insert_sql_joint(taobao_product)
                                if (taobao_product['image_url']):
                                    for url in taobao_product['image_url']:
                                        url = "https:" + url
                                        sql_taobao_product_image = product_image_insert_sql_joint(url, taobao_product)
                                        mapper.insert(sql_taobao_product_image)
                                mapper.insert(sql_taobao_products)
                                # (sql_taobao_products,sql_taobao_product_image) = product_insert_sql_joint(i)
                            conn.commit()
                            conn.close()
            all_time = (time.clock() - start_time)
            print ("total time is:", all_time)
        except Exception as err:
            print err