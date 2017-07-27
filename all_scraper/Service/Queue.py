#coding: utf-8
'''
创建人：Javen
创建时间： 2017/2/10  16:57
'''

from Models.Keys import Model_Keys
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.MobileDownloadQueue import Model_Mapper_MobileDownloadQueue
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Mapper.Scrape import Model_Mapper_Scrape
from Models.Mapper.UploadQueue import Model_Mapper_UploadQueue
from Models.Static.DownloadQueue.UploadStatus import Model_Static_DownloadQueue_UploadStatus
from Models.Static.Region import Model_Static_Region
from Service.Abstract import Service_Abstract
from Models.Mapper.DownloadQueue import Model_Mapper_DownloadQueue
from Models.DownloadQueue import Model_DownloadQueue
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Customer import Service_Customer
from Service.Product import Service_Product
from Service.Keywords import Service_Keywords
from Service.Offer import Service_Offer
from Models.Static.DownloadQueue.Type import Model_Static_DownloadQueue_Type
from Service.Review import Service_Review
from Service.Seller import Service_Seller
from Service.Upload import Service_Upload


class Service_Queue(Service_Abstract):

    def __init__(self):
        # 亚马逊
        self.downloadQueueMapper = Model_Mapper_DownloadQueue()
        self.mobiledownloadQueueMapper = Model_Mapper_MobileDownloadQueue()
        self.uploadQueueMapper = Model_Mapper_UploadQueue()

        self.productService = Service_Product()
        self.reviewService = Service_Review()
        self.keywordsService = Service_Keywords()
        self.offerService = Service_Offer()
        self.customerService = Service_Customer()
        self.sellerService = Service_Seller()

    def getDownloadQueueMapper(self):
        return self.downloadQueueMapper

    def getMobileDownloadQueueMapper(self):
        return self.mobiledownloadQueueMapper

    def getUploadQueueMapper(self):
        return self.uploadQueueMapper

    def getProductService(self):
        return self.productService

    def getReviewService(self):
        return self.reviewService

    def getKeywordsService(self):
        return self.keywordsService

    def getCustomerService(self):
        return self.customerService

    def getOfferService(self):
        return self.offerService

    def getSellerService(self):
        return self.sellerService

    def processPendingDownloadQueue(self, downloadQueue):
        status = downloadQueue[5]
        scrape_count = downloadQueue[7]
        if (status != Model_Static_DownloadQueue_Status.PENDING):
            return False
        # 获得下载队列，开始执行
        try:
            result = Model_Static_DownloadQueue_Status.PENDING
            type = downloadQueue[3]
            # 产品页 0
            if (type == Model_Static_DownloadQueue_Type.PRODUCT or type == Model_Static_DownloadQueue_Type.PRODUCT_INFO):
                result = self.getProductService().scrape(downloadQueue)
            # 前5页关键词 3
            elif (type == Model_Static_DownloadQueue_Type.KEYWORDS):
                result = self.getKeywordsService().scrape(downloadQueue)
            # 首页关键词 4
            elif (type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
                result = self.getKeywordsService().scrapeFirst(downloadQueue)
            # offer页面计算库存 1
            elif (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
                result = self.getOfferService().scrape(downloadQueue)
                # print (result)
                if (result == Model_Static_DownloadQueue_Status.SCRAPED):
                    result = self.getProductService().scrape(downloadQueue)
            # 产品评论抓取
            elif (type == Model_Static_DownloadQueue_Type.PRODUCT_REVIEW):
                result = self.getReviewService().scrape(downloadQueue)
            # seller 卖家页面 11
            elif (type == Model_Static_DownloadQueue_Type.SELLER):
                result = self.getSellerService().scrape(downloadQueue)
            # seller_product 卖家产品页 12
            elif (type == Model_Static_DownloadQueue_Type.SELLER_PRODUCT):
                result = self.getSellerService().scrapeProduct(downloadQueue)
            # top_reviewer 顶级评论页 10
            elif (type == Model_Static_DownloadQueue_Type.TOP_REVIEWER):
                result = self.getCustomerService().scrapeTopReviewer(downloadQueue)
            # 淘宝 产品页抓取
            # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_TaoBao):
            #     result = self.getProductTaoBaoService().scrapeProduct(downloadQueue)
            #     pass
        except Exception as err:
            print (err)

        if(result == Model_Static_DownloadQueue_Status.SCRAPED or result == Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA):
            status = result
            scrape_count += 1
            if (result == Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA):
                if (scrape_count >= 3 and status != 1):
                    status = 3
        elif (result == Model_Static_DownloadQueue_Status.FAILED or result == Model_Static_DownloadQueue_Status.SCRAPED_WRONG):
            scrape_count += 1
            if (scrape_count >= 3 and status != 1):
                status = 3

        # print (result)
        if (result != Model_Static_DownloadQueue_Status.SCRAPED_WRONG):
            try:
                # 写入本地日志
                # 当前日期
                # import datetime
                # now = datetime.datetime.now()
                # now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                import pytz
                import datetime
                tz = pytz.timezone('Asia/Shanghai')
                # tz = pytz.timezone('America/New_York')
                now_date = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                with open("./log.log", "a") as f:
                    f.write(str(now_date) + "---" + str(downloadQueue[0]) + "-- region:" + str(
                        downloadQueue[2]) + "-- type:" + str(downloadQueue[3]) + "--value:" + str(
                        downloadQueue[4]) + "-- status:" + Model_Static_DownloadQueue_Status().getText(result) + "\n")
                # 写入数据库日志
                downloadQueue_key = Model_Keys().downloadqueue_key
                downloadQueue = dict(zip(downloadQueue_key, downloadQueue))
                downloadQueue["status"] = str(status)
                downloadQueue["scrape_count"] = str(scrape_count)
            except Exception as err:
                print (err)
            try:
                # 更新download_queue表
                self.getDownloadQueueMapper().save(downloadQueue)
            except Exception as err:
                print (err)
        return True
        # sql = self.amazon.update_download_queue(str(region), str(type), value, str(status), str(scrape_count))
        # self.mapper.update(sql)

    def processPendingMobileDownloadQueue(self, mobiledownloadQueue):
        # region =downloadQueue[2]
        status = mobiledownloadQueue[5]
        # value = downloadQueue[4]
        scrape_count = mobiledownloadQueue[7]
        if (status != Model_Static_DownloadQueue_Status.PENDING):
            return False
        # 获得下载队列，开始执行
        try:
            result = Model_Static_DownloadQueue_Status.PENDING
            type = mobiledownloadQueue[3]
            # 产品页 0
            if (type == Model_Static_DownloadQueue_Type.KEYWORDS or type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
                result = self.getProductService().mobile_scrape(mobiledownloadQueue)
                # print (mobiledownloadQueue)
            # # 前5页关键词 3
            # elif (type == Model_Static_DownloadQueue_Type.KEYWORDS):
            #     result = self.getKeywordsService().scrape(mobiledownloadQueue)
            # # 首页关键词 4
            # elif (type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
            #     result = self.getKeywordsService().scrapeFirst(mobiledownloadQueue)
            # # offer页面计算库存 1
            # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
            #     result = self.getOfferService().scrape(mobiledownloadQueue)
            #     # print (result)
            #     if (result == Model_Static_DownloadQueue_Status.SCRAPED):
            #         result = self.getProductService().scrape(mobiledownloadQueue)
            # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_REVIEW):
            #     pass
            # # seller 卖家页面 11
            # elif (type == Model_Static_DownloadQueue_Type.SELLER):
            #     result = self.getSellerService().scrape(mobiledownloadQueue)
            # # seller_product 卖家产品页 12
            # elif (type == Model_Static_DownloadQueue_Type.SELLER_PRODUCT):
            #     result = self.getSellerService().scrapeProduct(mobiledownloadQueue)
            # # top_reviewer 顶级评论页 10
            # elif (type == Model_Static_DownloadQueue_Type.TOP_REVIEWER):
            #     result = self.getCustomerService().scrapeTopReviewer(mobiledownloadQueue)
            else:
                pass
            scrape_count += 1
            if(result == Model_Static_DownloadQueue_Status.SCRAPED or result == Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA):
                status = result
            elif (result == Model_Static_DownloadQueue_Status.FAILED):
                if (scrape_count > 3 and status != 1):
                    status = 3
            mobiledownloadQueue_key = Model_Keys().mobiledownloadqueue_key
            mobiledownloadQueue = dict(zip(mobiledownloadQueue_key, mobiledownloadQueue))
            mobiledownloadQueue["status"] = str(status)
            mobiledownloadQueue["scrape_count"] = str(scrape_count)
            try:
                self.getMobileDownloadQueueMapper().save(mobiledownloadQueue)
            except Exception as err:
                print (err)
        except Exception as err:
            print (err)

    def uploadDownloadQueues(self, downloadQueues, region):
        data = {'region': region}
        # 开始更改下载队列中的上传状态和上传次数
        amazon = Model_Mapper_Amazon()
        # 连接数据库
        db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        conn = db.connects()
        mapper = Model_Mapper_Mysql(conn)
        for downloadQueue in downloadQueues:
            queueRegion = Model_Static_Region().getText(downloadQueue[2])
            queueValue = downloadQueue[4]
            result = False
            if (downloadQueue[5] == Model_Static_DownloadQueue_Status.SCRAPED):
                type = downloadQueue[3]
                # 产品页 0
                if (type == Model_Static_DownloadQueue_Type.PRODUCT or type == Model_Static_DownloadQueue_Type.PRODUCT_INFO):
                    result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, None)
                # # 前5页关键词 3 或首页关键词
                elif (type == Model_Static_DownloadQueue_Type.KEYWORDS or type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
                    value = queueValue
                    keywords = value
                    result = self.getKeywordsService().getAmazonKeywordsUploadData(queueRegion, keywords)
                # offer页面计算库存 1
                elif (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
                    result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, "OFFER")
                elif (type == Model_Static_DownloadQueue_Type.PRODUCT_REVIEW):
                    pass
                elif (type == Model_Static_DownloadQueue_Type.SELLER):
                    merchant_id = queueValue
                    result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id)
                elif (type == Model_Static_DownloadQueue_Type.SELLER_PRODUCT):
                    merchant_id = queueValue
                    result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id, True)
                elif (type == Model_Static_DownloadQueue_Type.TOP_REVIEWER):
                    value = queueValue
                    value = value.split(":")
                    if (len(value) == 2):
                        begin = value[0]
                        end = value[1]
                    else:
                        begin = 1
                        end = value[0]
                    result = self.getCustomerService().getAmazonTopReviewerUploadData(queueRegion, begin, end)
                else:
                    pass

            # 整合数据
            data['region_data'] = {
                downloadQueue[0]: {
                    "data" : result,
                    'region' : str(downloadQueue[2]),
                    'type' : str(downloadQueue[3]),
                    'value' : downloadQueue[4],
                    "ac_download_queue_id" : str(downloadQueue[1]),
                    "status" : str(downloadQueue[5])
                }
            }
            # print data
            uploadService = Service_Upload()
            result = uploadService.upload(data)
            # print (result)
            if (result):
                # 根据云服务器返回数据进行判断，这里还要改进
                for download_queue_id, subresult in result.items():
                # download_queue_id = downloadQueue[0]
                #     subresult = 1
                    sql = amazon.DownloadQueue_select_sql_joint(download_queue_id)
                    downloadQueue = mapper.select(sql)
                    if (len(downloadQueue)>0):
                        id = downloadQueue[0][0]
                        count = downloadQueue[0][9]
                        count += 1
                        status = Model_Static_DownloadQueue_UploadStatus().PENDING
                        if (subresult):
                            status = Model_Static_DownloadQueue_UploadStatus().UPLOADED
                        else:
                            if (count > 2):
                                status = Model_Static_DownloadQueue_UploadStatus().FAILED
                        sql = amazon.DownloadQueue_update_sql_joint(status, count, id)
                        mapper.update(sql)
        conn.close()

    def processUploadQueues(self, uploadQueues, region):
        # 开始更改下载队列中的上传状态和上传次数
        amazon = Model_Mapper_Amazon()
        # 连接数据库
        db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        conn = db.connects()
        mapper = Model_Mapper_Mysql(conn)
        data = {'region': region}
        for uploadQueue in uploadQueues:
            queueRegion = Model_Static_Region().getText(uploadQueue[1])
            queueValue = uploadQueue[3]
            result = False
            if (str(uploadQueue[2]).isdigit()):
                type = uploadQueue[2]
                # 产品页 0
                if (type == Model_Static_DownloadQueue_Type.PRODUCT):
                    result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, None)
                # 前5页关键词 3
                elif (type == Model_Static_DownloadQueue_Type.KEYWORDS):
                    value = queueValue
                    keywords = value
                    result = self.getKeywordsService().getAmazonKeywordsRankUploadData(queueRegion, keywords)
                # 首页关键词 4
                elif (type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
                    value = queueValue
                    keywords = value
                    result = self.getKeywordsService().getAmazonKeywordsInfoUploadData(queueRegion, keywords)
                # offer页面计算库存 1
                elif (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
                    result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, 'OFFER')
                # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_REVIEW):
                #     pass
                elif (type == Model_Static_DownloadQueue_Type.SELLER):
                    merchant_id = queueValue
                    result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id)
                elif (type == Model_Static_DownloadQueue_Type.SELLER_PRODUCT):
                    merchant_id = queueValue
                    result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id, True)
                elif (type == Model_Static_DownloadQueue_Type.TOP_REVIEWER):
                    value = queueValue
                    value = value.split(":")
                    if (len(value) == 2):
                        begin = value[0]
                        end = value[1]
                    else:
                        begin = 1
                        end = value[0]
                    result = self.getCustomerService().getAmazonTopReviewerUploadData(queueRegion, begin, end)
                else:
                    pass

            # 整合数据
            data['region_data'] = {uploadQueue[0]: {
                "data": result,
                'region': uploadQueue[1],
                'type': uploadQueue[2],
                'value': uploadQueue[3],
            }}
            # print data
            uploadService = Service_Upload()
            result = uploadService.upload(data, 'UploadQueue')
            # print (result)

            if (result):
                # 根据云服务器返回数据进行判断，这里还要改进
                for upload_queue_id, subresult in result.items():
                    # subresult = 1
                    if (subresult == True):
                        sql = amazon.UploadQueue_select_sql_joint(str(upload_queue_id))
                        uploadQueue = mapper.select(sql)
                        if (uploadQueue):
                            sql = amazon.UploadQueue_delete_sql_joint(str(upload_queue_id))
                            mapper.delete(sql)
        conn.close()

    def processMobileUploadQueues(self, mobileuploadQueues, region):

        data = {'region': region}
        for mobileuploadQueue in mobileuploadQueues:
            queueRegion = Model_Static_Region().getText(mobileuploadQueue[1])
            queueValue = mobileuploadQueue[3]
            result = False
            if (str(mobileuploadQueue[2]).isdigit()):
                type = mobileuploadQueue[2]
                # 产品页 0
                if (type == Model_Static_DownloadQueue_Type.PRODUCT):
                    result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, None)
                # # 前5页关键词 3
                # elif (type == Model_Static_DownloadQueue_Type.KEYWORDS):
                #     value = queueValue
                #     keywords = value
                #     result = self.getKeywordsService().getAmazonKeywordsRankUploadData(queueRegion, keywords)
                # # 首页关键词 4
                # elif (type == Model_Static_DownloadQueue_Type.KEYWORDS_INFO):
                #     value = queueValue
                #     keywords = value
                #     result = self.getKeywordsService().getAmazonKeywordsInfoUploadData(queueRegion, keywords)
                # # offer页面计算库存 1
                # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_OFFER):
                #     result = self.getProductService().getAmazonProductUploadData(queueRegion, queueValue, 'OFFER')
                # # elif (type == Model_Static_DownloadQueue_Type.PRODUCT_REVIEW):
                # #     pass
                # elif (type == Model_Static_DownloadQueue_Type.SELLER):
                #     merchant_id = queueValue
                #     result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id)
                # elif (type == Model_Static_DownloadQueue_Type.SELLER_PRODUCT):
                #     merchant_id = queueValue
                #     result = self.getSellerService().getAmazonSellerUploadData(queueRegion, merchant_id, True)
                # elif (type == Model_Static_DownloadQueue_Type.TOP_REVIEWER):
                #     value = queueValue
                #     value = value.split(":")
                #     if (len(value) == 2):
                #         begin = value[0]
                #         end = value[1]
                #     else:
                #         begin = 1
                #         end = value[0]
                #     result = self.getCustomerService().getAmazonTopReviewerUploadData(queueRegion, begin, end)
                else:
                    pass

            # 整合数据
            data['region_data'] = {mobileuploadQueue[0]: {
                "data": result,
                'region': mobileuploadQueue[1],
                'type': mobileuploadQueue[2],
                'value': mobileuploadQueue[3],
            }}
            # print data
            uploadService = Service_Upload()
            result = uploadService.upload(data, 'UploadQueue')
            # print (result)
            if (result):
                # 开始更改下载队列中的上传状态和上传次数
                amazon = Model_Mapper_Amazon()
                # 连接数据库
                db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
                conn = db.connects()
                mapper = Model_Mapper_Mysql(conn)
                # 根据云服务器返回数据进行判断，这里还要改进
                for upload_queue_id, subresult in result.items():
                    # subresult = 1
                    if (subresult == True):
                        sql = amazon.MobileUploadQueue_select_sql_joint(str(upload_queue_id))
                        uploadQueue = mapper.select(sql)
                        if (uploadQueue):
                            sql = amazon.MobileUploadQueue_delete_sql_joint(str(upload_queue_id))
                            mapper.delete(sql)
                conn.close()