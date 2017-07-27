#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time
from Service.TaobaoQueue import Service_TaobaoQuene
from Service.get_downloadquene import get_TaoBao_download_Quene
from pyvirtualdisplay import Display


class Service_Cronjob_ProcessPendingTaobaoDownloadQueue():

    def  __init__(self):
        pass

    def start(self):
        bt = time.time()
        print("Parent Begin:" + str(bt) + "\n")
        with Display(backend="xvfb", size=(1440, 900)):
            try:
                # 从downloadquene中取出数据库中数据
                type_list = get_TaoBao_download_Quene()
                downloadQuenes = type_list
            except Exception as err:
                print err
            if (downloadQuenes):
                queneService = Service_TaobaoQuene()
                for downloadQuene in downloadQuenes:
                    queneService.processPendingTaobaoDownloadQuene(downloadQuene)
            else:
                print ("no downloadquenes")

        # self.downloadQueueMapper.conn.close()
        tt = time.time()
        tseconds = tt - bt
        print ("Process Time:" + str(tseconds) + "\n")
        et = time.time()
        print ("Parent End:" + str(et) + "\n")
        print ("Parent" + str(et - bt) + "seconds\n")