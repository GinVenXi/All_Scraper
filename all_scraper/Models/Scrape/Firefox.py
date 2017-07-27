#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Scrape.Abstract import Model_Scrape_Abstract
from Models.Static.Scrape.Method import Model_Static_Scrape_Method
from Models.Downloader_Method import Model_Downloader_Method
from Models.Static.Scrape.Status import Model_Static_Scrape_Status
from Models.Time import Model_Time
import time

class Model_Scrape_Firefox(Model_Scrape_Abstract):
    def __init__(self , region):
        super(Model_Scrape_Firefox, self).__init__(region)
        self.region = region
        self.downloader = Model_Downloader_Method("all")

    def getDownloader(self):
        return self.downloader

    def getContent(self):
        return self.downloader.getContent()

    # def print_ts(self , message):
    #     print "[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)

    def process(self , url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.downloader(self.url)
            if(downloadResult == Model_Static_Scrape_Status.FAILED):
                print("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif(downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif(downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    def process_review(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.review_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    def process_keywords(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.keywords_downloader(self.url)
            if(downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif(downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif(downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    def process_offer(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.offer_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                # self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    # 抓取卖家库存SellerInventory_Downloader
    def process_inventory(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.inventory_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    # 抓取顶级评论人TopReviewer_Downloader
    def process_TopReviewer(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.topreviewer_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    # 抓取卖家Seller_Downloader
    def process_seller(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.seller_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break

    # 抓取卖家产品SellerProduct_Downloader
    def process_sellerproduct(self, url):
        self.url = url
        self.scrape = {}
        self.scrape['url'] = url
        self.scrape['method'] = Model_Static_Scrape_Method().FIREFOX
        self.scrape['begin_time'] = Model_Time().getCurrentDatetime()
        for i in range(3):
            downloadResult = self.downloader.sellerproduct_downloader(self.url)
            if (downloadResult == Model_Static_Scrape_Status.FAILED):
                print ("Download Error: failed")
                self.downloader.refresh_again()
                self.scrape['status'] = Model_Static_Scrape_Status.FAILED
                self.scrape['comment'] = "Download Error: failed"
                continue
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
                print ("Download Success: no data")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS_NO_DATA
                self.scrape['comment'] = "Download Success: no data"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break
            elif (downloadResult == Model_Static_Scrape_Status.ROBOT_CHECK):
                print ("Download Error: robot check")
                self.scrape['status'] = Model_Static_Scrape_Status.ROBOT_CHECK
                self.scrape['comment'] = "Download Error: robot check"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                return "Robot Check"
            elif (downloadResult == Model_Static_Scrape_Status.SUCCESS):
                print ("Download Success: success")
                self.scrape['status'] = Model_Static_Scrape_Status.SUCCESS
                self.scrape['comment'] = "Download Success: success"
                self.scrape['end_time'] = Model_Time().getCurrentDatetime()
                break