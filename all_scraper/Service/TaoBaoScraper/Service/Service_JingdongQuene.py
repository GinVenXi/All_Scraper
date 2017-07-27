# -*-coding:utf-8*-


class Service_JDQuene():

    def __init__(self):
        pass

    def processPendingTaobaoDownloadQuene(self,downloadQuene):
        try:
            if(downloadQuene[3]==1):
                #taobao_keyword
                JD_keyword=keywords_scrape()
                result = JD_keyword.KEYWORDS_SCRAPE()
            elif(downloadQuene[3]==2):
                #taobao_product
                JD_product=products_scrape()
                JD_product.PRODUCTS_SCRAPE()
            elif(downloadQuene[3]==3):
                #taobao_product_review
                JD_product_review=products_review_scrape()
                JD_product_review.PRODUCT_REVIEW_SCRAPE()
            elif(downloadQuene[3]==4):
                #taobao_sellerpage
                JD_sellerpage=seller_page_scrape()
                JD_sellerpage.SELLER_PAGE_SCRAPE()
        except Exception as err:
            print err
        # if (result):
        #     # 修改数据库状态

