#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Keys import Model_Keys
from Models.Mapper.Sina.Base import Model_Mapper_Sina_Base
from Models.Mapper.Tencent.Base import Model_Mapper_Tencent_Base

from Service.Sina.Auto import Service_Sina_Auto
from Service.Sina.Base import Service_Sina_Base
from Service.Sina.Blog import Service_Sina_Blog
from Service.Sina.City import Service_Sina_City
from Service.Sina.Edu import Service_Sina_Edu
from Service.Sina.Travel import Service_Sina_Travel
from Service.Sina.Video import Service_Sina_Video
from Service.Tencent.Auto import Service_Tencent_Auto
from Service.Tencent.Base import Service_Tencent_Base
from Service.Tencent.Gongyi import Service_Tencent_Gongyi
from Service.Tencent.Sports import Service_Tencent_Sports


class Service_NewsQueue():

    def __init__(self):
        self.downloadQueueMapper = Model_Mapper_Sina_Base()
        self.tencentDownloadQueueMapper = Model_Mapper_Tencent_Base()
        self.sinaBaseService = Service_Sina_Base()
        self.sinaAutoService = Service_Sina_Auto()
        self.sinaBlogService = Service_Sina_Blog()
        self.sinaEduService = Service_Sina_Edu()
        self.sinaTravelService = Service_Sina_Travel()
        self.sinaCityService = Service_Sina_City()
        self.sinaVideoService = Service_Sina_Video()

        self.tencentBaseService = Service_Tencent_Base()
        self.tencentSportsService = Service_Tencent_Sports()
        self.tencentAutoService = Service_Tencent_Auto()
        self.tencentGongyiService = Service_Tencent_Gongyi()

    def getDownloadQueueMapper(self):
        return self.downloadQueueMapper

    def getTencentDownloadQueueMapper(self):
        return self.tencentDownloadQueueMapper

    def getSinaBaseService(self):
        return self.sinaBaseService

    def getTencentBaseService(self):
        return self.tencentBaseService

    def getSinaAutoService(self):
        return self.sinaAutoService

    def getSinaBlogService(self):
        return self.sinaBlogService

    def getSinaEduService(self):
        return self.sinaEduService

    def getSinaTravelService(self):
        return self.sinaTravelService

    def getSinaCityService(self):
        return self.sinaCityService

    def getSinaVideoService(self):
        return self.sinaVideoService

    def getTencentSportsService(self):
        return self.tencentSportsService

    def getTencentAutoService(self):
        return self.tencentAutoService

    def getTencentGongyiService(self):
        return self.tencentGongyiService

    def processPendingAmazonDownloadQueue(self, key, value):
        pass

    def processPendingSinaDownloadQueue(self, key, value):

        if (key == "auto"):
            result = self.getSinaAutoService().scrape(value)
        elif (key == "blog"):
            result = self.getSinaBlogService().scrape(value)
        elif (key == "edu"):
            result = self.getSinaEduService().scrape(value)
        elif (key == "travel"):
            result = self.getSinaTravelService().scrape(value)
        elif (key == "city"):
            result = self.getSinaCityService().scrape(value)
        elif (key == "video"):
            result = self.getSinaVideoService().scrape(value)
        else:
            result = self.getSinaBaseService().scrape(value)
        # print (result)
        if (result):
            download_queues = self.getSinaBaseService().getDownloadQueueContent()
            if (download_queues):
                if (len(download_queues)>0):
                    print len(download_queues)
                    for download_queue in download_queues:
                        try:
                            result = self.getSinaBaseService().scrape_content(download_queue)

                            # 对download_queue进行修改
                            downloadQueue_key = Model_Keys().news_downloadqueue_key
                            downloadQueue = dict(zip(downloadQueue_key, download_queue))
                            if (result == True):
                                downloadQueue["status"] = str(1)
                                print ("yes")
                            else:
                                downloadQueue["status"] = str(2)
                                print ("no")
                            self.getDownloadQueueMapper().save_status(downloadQueue)
                        except Exception as err:
                            print (err)

    def processPendingTencentDownloadQueue(self, key, value):
        # 下面还要修改，只是照搬了新浪的
        if (key == "sports"):
            result = self.getTencentSportsService().scrape(value)
        elif (key == "auto"):
            result = self.getTencentAutoService().scrape(value)
        elif (key == "gongyi"):
            result = self.getTencentGongyiService().scrape(value)
        else:
            result = self.getTencentBaseService().scrape(value)
        print (result)
        if (result):
            download_queues = self.getTencentBaseService().getDownloadQueueContent()
            if (download_queues):
                if (len(download_queues)>0):
                    print len(download_queues)
                    for download_queue in download_queues:
                        try:
                            # print (download_queue)
                            result = self.getTencentBaseService().scrape_content(download_queue)
        #
        #                     # 对download_queue进行修改
                            downloadQueue_key = Model_Keys().news_downloadqueue_key
                            downloadQueue = dict(zip(downloadQueue_key, download_queue))
                            if (result == True):
                                downloadQueue["status"] = str(1)
                                print ("yes")
                            else:
                                downloadQueue["status"] = str(2)
                                print ("no")
                            self.getTencentDownloadQueueMapper().save_status(downloadQueue)
                        except Exception as err:
                            print (err)