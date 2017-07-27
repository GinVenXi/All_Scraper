#-*-coding:utf-8*-
import time
from Service.JingDongScraper.get_keywords_url_id.get_product_url import get_product_url
from Service.JingDongScraper.get_text.get_text import login_jd
from Service.JingDongScraper.get_text.get_text import get_text
from Service.JingDongScraper.analysis.products_analysis import products_analysis
from Service.JingDongScraper.db_operation.db_connection import DB_connection
from Service.JingDongScraper.db_operation.db_operation import DB_operation
from Service.JingDongScraper.sql_joint.product_sql_joint import products_insert_sql_joint
from Service.JingDongScraper.sql_joint.product_sql_joint import products_image_insert_sql_joint

# def main():
#     try:
#         start_time=time.clock()
#         #从jd_keywords表里面获取需要的sku拼接url
#         item_product_sku = get_product_url()
#         item_product_sku_1 = item_product_sku.get_Product_Url()
#         #登录京东操作
#         login=login_jd()
#         login.login_JD()
#         for product_sku in item_product_sku_1:
#             print ('##############################################')
#             print (product_sku[0])
#             url="https://item.jd.com/"+str(product_sku[0])+".html"
#             #根据url获取网页源码
#             html = get_text()
#             html_1 = html.get_html_text_1(url)
#             try:
#                 # if(html_1):
#                 #     #解析操作
#                 #     processor=products_analysis()
#                 #     data_1=processor.process(html_1)
#                 #     if(data_1):
#                 #         for data in data_1:
#                 #             for key,value in data.items():
#                 #                 # 如果解析里有shop_id
#                 #                 if (key == 'shop_id' and value != ""):
#                 #                     # 找到数据库中看有没有这一条记录
#                 #                     shopid_value = value
#                 #                     result = products_update_select(shopid_value)
#                 #                     # 有的话
#                 #                     if (result):
#                 #                         # 更新操作
#                 #                         products_update_operation(data, shopid_value)
#                 #                     else:
#                 #                         # 插入操作
#                 #                         products_insert_operation(data)
#                 if(html_1):
#                     #解析操作
#                     processor=products_analysis()
#                     data=processor.process(html_1,product_sku[0])
#                     # 连接数据库
#                     db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
#                     conn = db.connects()
#                     mapper = DB_operation(conn)
#                     if(data):
#                         for data_1 in data:
#                             #插入到jd_products数据表中的数据
#                             sql_jd_products=products_insert_sql_joint(data_1)
#                             for img in data_1['image_url']:
#                                 img_url="https:"+img
#                                 sql_jd_product_image=products_image_insert_sql_joint(data_1,img_url)
#                                 # mapper.insert(sql_jd_product_image)
#                             # mapper.insert(sql_jd_products)
#                             print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#                             print sql_jd_products
#                             print sql_jd_product_image
#                             print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#                             mapper.insert(sql_jd_products)
#                             mapper.insert(sql_jd_product_image)
#                         conn.commit()
#                         conn.close()
#             except Exception as err:
#                 print err
#     except Exception as err:
#             print err
#     all_time = (time.clock() - start_time)
#     print ("total time is:", all_time)
#         # #以下代码为单个网页测试代码
#         # url='https://item.jd.com/11378358411.html'
#         # html=getHtmlText(url)
#         # if(html):
#         #     processor=Model_Processor_Jd_Product_Base()
#         #     data=processor.process(html)
#         #     if(data):
#         #         # print data
#         #         db=sqlConnect('localhost', 3306, 'root', 'bwx0605', 'JD_scraper', 'utf8')
#         #         conn=db.connects()
#         #         mapper=Mysql(conn)
#         #         sql_products_insert=products_insert_sql_joint(data[0])
#         #         print sql_products_insert
#         #         mapper.insert(sql_products_insert)
#         #         conn.commit()
#         #         conn.close()
#     # except Exception as err:
#     #     print err
#
# if __name__ == '__main__':
#     main()

class products_scrape():
    def PRODUCTS_SCRAPE(self):
        try:
            start_time = time.clock()
            # 从jd_keywords表里面获取需要的sku拼接url
            item_product_sku = get_product_url()
            item_product_sku_1 = item_product_sku.get_Product_Url()
            # 登录京东操作
            login = login_jd()
            login.login_JD()
            for product_sku in item_product_sku_1:
                print (product_sku[0])
                url = "https://item.jd.com/" + str(product_sku[0]) + ".html"
                # 根据url获取网页源码
                html = get_text()
                html_1 = html.get_html_text_1(url)
                try:
                    # if(html_1):
                    #     #解析操作
                    #     processor=products_analysis()
                    #     data_1=processor.process(html_1)
                    #     if(data_1):
                    #         for data in data_1:
                    #             for key,value in data.items():
                    #                 # 如果解析里有shop_id
                    #                 if (key == 'shop_id' and value != ""):
                    #                     # 找到数据库中看有没有这一条记录
                    #                     shopid_value = value
                    #                     result = products_update_select(shopid_value)
                    #                     # 有的话
                    #                     if (result):
                    #                         # 更新操作
                    #                         products_update_operation(data, shopid_value)
                    #                     else:
                    #                         # 插入操作
                    #                         products_insert_operation(data)
                    if (html_1):
                        # 解析操作
                        processor = products_analysis()
                        data = processor.process(html_1, product_sku[0])
                        # 连接数据库
                        db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper', 'utf8')
                        conn = db.connects()
                        mapper = DB_operation(conn)
                        if (data):
                            for data_1 in data:
                                # 插入到jd_products数据表中的数据
                                sql_jd_products = products_insert_sql_joint(data_1)
                                for img in data_1['image_url']:
                                    img_url = "https:" + img
                                    sql_jd_product_image = products_image_insert_sql_joint(data_1, img_url)
                                    # mapper.insert(sql_jd_product_image)
                                # mapper.insert(sql_jd_products)
                                print sql_jd_products
                                print sql_jd_product_image
                                mapper.insert(sql_jd_products)
                                mapper.insert(sql_jd_product_image)
                            conn.commit()
                            conn.close()
                except Exception as err:
                    print err
        except Exception as err:
            print err
        all_time = (time.clock() - start_time)
        print ("total time is:", all_time)