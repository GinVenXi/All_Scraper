#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Service.Cronjob.ProcessPendingJingdongDownloadQueue import Service_Cronjob_ProcessPendingJingdongDownloadQueue
import fcntl, sys, os
pidfile = 0

class all_start():
    def process_start(self):
        process = Service_Cronjob_ProcessPendingJingdongDownloadQueue()
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

    ApplicationInstance()
    test()
