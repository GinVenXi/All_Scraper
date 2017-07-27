#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import pytz

import datetime
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.DownloadQueue import Model_Mapper_DownloadQueue
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Mapper.Scrape import Model_Mapper_Scrape
from Models.Mapper.UploadQueue import Model_Mapper_UploadQueue

class Service_Abstract(object):
    def __init__(self):
        self.downloadQueueMapper = Model_Mapper_DownloadQueue()
        self.uploadQueueMapper = Model_Mapper_UploadQueue()
        self.scrapeMapper = Model_Mapper_Scrape()
        # self.amazon = Model_Mapper_Amazon()
        # # 连接数据库
        # self.db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        # self.conn = self.db.connects()
        # self.mapper = Model_Mapper_Mysql(self.conn)

    def getDownloadQueueMapper(self):
        return self.downloadQueueMapper

    def getUploadQueueMapper(self):
        return self.uploadQueueMapper

    def addUploadQueue(self, region, type, value):
        return self.getUploadQueueMapper().save(region, type, value)

    def saveScrapes(self, scrapes, downloadQueue):
        if(downloadQueue[0]):
            # 在插入前需要将前面的数据清空，主要删除有download_queue_id的数据
            for scrape in scrapes:
                try:
                    if (scrape['download_queue_id']):
                        continue
                except:
                    pass
                scrape['download_queue_id'] = downloadQueue[0]
                tz = pytz.timezone('Asia/Shanghai')
                last_updated_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                scrape['time'] = last_updated_time
                # print len(scrape['url'])
                if (len(scrape['url']) > 255):
                    continue
                self.scrapeMapper.save(scrape)
