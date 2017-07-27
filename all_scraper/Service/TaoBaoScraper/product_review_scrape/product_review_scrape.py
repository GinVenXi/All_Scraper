#-*-coding:utf-8*-
from Service.TaoBaoScraper.get_url_or_id_keywords.get_reviews_userid_itemid import get_reviews
from Service.TaoBaoScraper.get_text.get_text import get_text
from Service.TaoBaoScraper.analysis.reviews_analysis import reviews_analysis
from Service.TaoBaoScraper.sql_joint.product_review_sql_joint import product_review_insert_sql_joint
from Service.TaoBaoScraper.db_operation.db_connection import DB_connection
from Service.TaoBaoScraper.db_operation.db_operation import DB_operation
from Service.TaoBaoScraper.sql_joint.product_sql_joint import product_image_insert_sql_joint

def main():
    try:
        # for i in range(20):
        User_id1 = []
        itemId1 = []
        reviews_id=get_reviews()
        (User_id1, itemId1) = reviews_id.get_reviews_userid_itemid()
        for User_id1dom in User_id1:
            for itemId1dom in itemId1:
                for page in range(20):

                    start_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + itemId1dom[0] + '&sellerId=' +User_id1dom[0] + '&currentPage=' + str(page)
                    json_text = get_text()
                    json_text_1=json_text.get_json_text(start_url)
                    # print json_text
                    try:
                        if (json_text_1):
                            processor = reviews_analysis()
                            data3 = processor.process(json_text_1, start_url)
                            if(data3):

                                for i in range(len(data3)):
                                    lastdata = data3[i]
                                    # print lastdata
                                    if (lastdata):
                                        db = DB_connection('localhost', 3306, 'root', 'bwx0605', 'All_Scraper', 'utf8')
                                        conn = db.connects()
                                        mapper = DB_operation(conn)
                                        sql_taobao_product_review= product_review_insert_sql_joint(lastdata)
                                        for img in lastdata['image_url']:
                                            sql_taobao_product_review_image=product_image_insert_sql_joint()
                                        print sql_taobao_product_review
                                        print sql_taobao_product_review_image
                                        mapper.insert(sql_taobao_product_review)
                                        mapper.insert(sql_taobao_product_review_image)
                                    conn.commit()
                                    conn.close()
                    except Exception as err:
                        print err
    except Exception as err:
        print err

if __name__ == '__main__':
    main()

class products_review_scrape():

    def PRODUCT_REVIEW_SCRAPE(self):
        try:
            # for i in range(20):
            User_id1 = []
            itemId1 = []
            reviews_id = get_reviews()
            (User_id1, itemId1) = reviews_id.get_reviews_userid_itemid()
            for User_id1dom in User_id1:
                for itemId1dom in itemId1:
                    for page in range(20):

                        start_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + itemId1dom[
                            0] + '&sellerId=' + User_id1dom[0] + '&currentPage=' + str(page)
                        json_text = get_text()
                        json_text_1 = json_text.get_json_text(start_url)
                        # print json_text
                        try:
                            if (json_text_1):
                                processor = reviews_analysis()
                                data3 = processor.process(json_text_1, start_url)
                                if (data3):

                                    for i in range(len(data3)):
                                        lastdata = data3[i]
                                        # print lastdata
                                        if (lastdata):
                                            db = DB_connection('localhost', 3306, 'root', '123123', 'All_Scraper',
                                                               'utf8')
                                            conn = db.connects()
                                            mapper = DB_operation(conn)
                                            sql_taobao_product_review = product_review_insert_sql_joint(lastdata)
                                            for img in lastdata['image_url']:
                                                sql_taobao_product_review_image = product_image_insert_sql_joint(img, lastdata)
                                            print sql_taobao_product_review
                                            print sql_taobao_product_review_image
                                            mapper.insert(sql_taobao_product_review)
                                            mapper.insert(sql_taobao_product_review_image)
                                        conn.commit()
                                        conn.close()
                        except Exception as err:
                            print err
        except Exception as err:
            print err