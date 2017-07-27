# -*-coding:utf-8*-
from keywords_scrape.keywords_scrape import keywords_scrape
from products_scrape.products_scrape import products_scrape
from product_review_scrape.product_review_scrape import product_review_scrape
from seller_page_scrape.seller_page_scrape import seller_page_scrape


class Service_JDQuene():

    def __init__(self):
        pass

    def processPendingTaobaoDownloadQuene(self,downloadQuene):
        try:
            if(downloadQuene[3]==1):
                #JD_keyword
                JD_keyword=keywords_scrape()
                result = JD_keyword.KEYWORDS_SCRAPE()
            elif(downloadQuene[3]==2):
                #JD_product
                JD_product=products_scrape()
                JD_product.PRODUCTS_SCRAPE()
            elif(downloadQuene[3]==3):
                #JD_product_review
                JD_product_review=product_review_scrape()
                JD_product_review.PRODUCT_REVIEW_SCRAPE()
            elif(downloadQuene[3]==4):
                #JD_sellerpage
                JD_sellerpage=seller_page_scrape()
                JD_sellerpage.SELLER_PAGE_SCRAPE()
        except Exception as err:
            print err

