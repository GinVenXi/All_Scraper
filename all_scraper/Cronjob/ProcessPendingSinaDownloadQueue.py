#coding: utf-8
'''
创建人：Javen
创建时间：
'''
# 新浪新闻
from Service.Cronjob.ProcessPendingSinaDownloadQueue import Service_Cronjob_ProcessPendingSinaDownloadQueue
import fcntl, sys, os
import multiprocessing
pidfile = 0

class all_start():
    def process_start(self):
        process = Service_Cronjob_ProcessPendingSinaDownloadQueue()
        process.start()

def test():
    start = all_start()
    start.process_start()

def ApplicationInstance():
    global pidfile
    pidfile = open(os.path.realpath(__file__), "r")
    try:
        fcntl.flock(pidfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except:
        print ("another instance is running...")
        sys.exit(1)

if __name__=="__main__":
    # 控制同一时间段只有一个进程在执行，即不使用多进程
    # ApplicationInstance()
    test()