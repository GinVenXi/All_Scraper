#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time

from pyvirtualdisplay import Display

from Service.JingdongQueue import Service_JingdongQueue
from Service.get_downloadquene import get_JD_download_Queue


class Service_Cronjob_ProcessPendingJingdongDownloadQueue():

    def  __init__(self):
        pass

    def start(self):
        bt = time.time()
        print("Parent Begin:" + str(bt) + "\n")
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                # 从downloadquene中取出数据库中数据
                type_list = get_JD_download_Queue()
                downloadQueues = type_list
            except Exception as err:
                print err
            if (downloadQueues):
                queneService = Service_JingdongQueue()
                for downloadQueue in downloadQueues:
                    queneService.processPendingJingdongDownloadQueue(downloadQueue)
            else:
                print ("no downloadquenes")
        # self.downloadQueueMapper.conn.close()
        tt = time.time()
        tseconds = tt - bt
        print ("Process Time:" + str(tseconds) + "\n")
        et = time.time()
        print ("Parent End:" + str(et) + "\n")
        print ("Parent" + str(et - bt) + "seconds\n")
