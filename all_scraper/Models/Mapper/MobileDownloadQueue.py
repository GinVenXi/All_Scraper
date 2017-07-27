#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17：04
'''
from Models.DbTable.DownloadQueue import Model_DbTable_DownloadQueue
from Models.Mapper.Abstract import Model_Mapper_Abstract

class Model_Mapper_MobileDownloadQueue(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_MobileDownloadQueue, self).__init__()
        # self.dbTable = Model_DbTable_DownloadQueue()

    # 用来存储download_queue表的sql语句
    def save(self, mobiledownloadQueue):
        if (mobiledownloadQueue['id']):
            searchData = {'id' : mobiledownloadQueue['id']}
            result = self.findData("all", "mobile_download_queue", searchData)
            if (result):
                import time
                last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                mobiledownloadQueue['last_updated_time'] = last_updated_time
                self.update("mobile_download_queue", mobiledownloadQueue)
                return mobiledownloadQueue
            else:
                return False
        else:
            result = self.insert("mobile_download_queue", mobiledownloadQueue)
            if (result):
                mobiledownloadQueue['id'] = result
            return mobiledownloadQueue


