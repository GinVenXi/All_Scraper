#-*-coding:utf-8*-
from keywords_scrape.keywords_scrape import keywords_scrape
from products_scrape.products_scrape import products_scrape
from product_review_scrape.product_review_scrape import products_review_scrape
from seller_page_scrape.seller_page_scrape import seller_page_scrape


class Service_TaobaoQuene():

    def __init__(self):
        pass

    def processPendingTaobaoDownloadQuene(self,downloadQuene):
        try:
            if(downloadQuene[3]==1):
                #taobao_keyword
                taobao_keyword=keywords_scrape()
                result = taobao_keyword.KEYWORDS_SCRAPE()
            elif(downloadQuene[3]==2):
                #taobao_product
                taobao_product=products_scrape()
                taobao_product.PRODUCTS_SCRAPE()
            elif(downloadQuene[3]==3):
                #taobao_product_review
                taobao_product_review=products_review_scrape()
                taobao_product_review.PRODUCT_REVIEW_SCRAPE()
            elif(downloadQuene[3]==4):
                #taobao_sellerpage
                taobao_sellerpage=seller_page_scrape()
                taobao_sellerpage.SELLER_PAGE_SCRAPE()
        except Exception as err:
            print err
        # if (result):
        #     # 修改数据库状态
