#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/9
'''
import time
from Models.Downloader_Method import Model_Downloader_Method
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Service.Queue import Service_Queue
from Models.Mapper.DownloadQueue import Model_Mapper_DownloadQueue
from pyvirtualdisplay import Display


class Service_Cronjob_ProcessPendingDownloadQueue():

    def  __init__(self):
        self.downloadQueueMapper = Model_Mapper_DownloadQueue()
        self.method = Model_Downloader_Method("all")

    def getDownloadQueueMapper(self):
        return self.downloadQueueMapper

    def start(self):
        bt = time.time()
        print("Parent Begin:" + str(bt) + "\n")
        try:
            # # 连接数据库
            # db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
            # conn = db.connects()
            # mapper = Model_Mapper_Mysql(conn)
            # sql = "select * from download_queue WHERE status = 0"
            # downloadQueues = mapper.select(sql)
            # conn.close()
            searchData = {"status" : str(Model_Static_DownloadQueue_Status.PENDING)}
            downloadQueues = self.getDownloadQueueMapper().findData("all", "download_queue", searchData, 500)
            # print (downloadQueues)
        except Exception as err:
            print (err)
        if (downloadQueues):
            queueService = Service_Queue()
            # with Display(backend="xvfb", size=(1440, 900)):
            try:
                self.method.downloader_init()
                # 浏览器抓取登录
                # login_success = Model_Downloader_Method("com").downloader_login()
                # if (login_success):
                for downloadQueue in downloadQueues:
                    queueService.processPendingDownloadQueue(downloadQueue)
                self.method.downloader_quit()
                    # else:
                    #     Model_Downloader_Method("com").downloader_quit()
                    #     self.start()
            except Exception as err:
                print (err)
                self.method.downloader_quit()
        else:
            print ("no downloadQueues")
        self.downloadQueueMapper.conn.close()
        tt = time.time()
        tseconds = tt - bt
        print ("Process Time:" + str(tseconds) + "\n")
        et = time.time()
        print ("Parent End:" + str(et) + "\n")
        print ("Parent" + str(et-bt) + "seconds\n")
