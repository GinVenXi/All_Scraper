#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17：04
'''
import pytz
import datetime
from Models.DbTable.DownloadQueue import Model_DbTable_DownloadQueue
from Models.Mapper.Abstract import Model_Mapper_Abstract

class Model_Mapper_DownloadQueue(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_DownloadQueue, self).__init__()
        # self.dbTable = Model_DbTable_DownloadQueue()

    # 用来存储download_queue表的sql语句
    def save(self, downloadQueue):
        if (downloadQueue['id']):
            searchData = {'id': downloadQueue['id']}
            result = self.findData("all", "download_queue", searchData)
            if (result):
                # import time
                # last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                tz = pytz.timezone('Asia/Shanghai')
                # tz = pytz.timezone('America/New_York')
                last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                downloadQueue['last_updated_time'] = last_updated_time
                self.update("download_queue", downloadQueue, searchData)
                return downloadQueue
            else:
                return False
        else:
            result = self.insert("download_queue", downloadQueue)
            if (result):
                downloadQueue['id'] = result
            return downloadQueue

    # 更新抓取数量
    def saveReview(self, downloadQueue):
        if (downloadQueue['id']):
            searchData = {'id': downloadQueue['id']}
            result = self.findData("all", "download_queue", searchData)
            if (result):
                # import time
                # last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                tz = pytz.timezone('Asia/Shanghai')
                # tz = pytz.timezone('America/New_York')
                last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                downloadQueue['last_updated_time'] = last_updated_time
                self.update("download_queue_review", downloadQueue, searchData)
                return downloadQueue
            else:
                return False
        else:
            result = self.insert("download_queue", downloadQueue)
            if (result):
                downloadQueue['id'] = result
            return downloadQueue