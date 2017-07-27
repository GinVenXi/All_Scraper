#coding: utf-8
'''
创建人:Javen
创建时间:2017/2/8
修改时间:2017/2/8
'''
from Service.Cronjob.ProcessPendingDownloadQueue import Service_Cronjob_ProcessPendingDownloadQueue
import fcntl, sys, os
pidfile = 0

class all_start():
    def process_start(self):
        process = Service_Cronjob_ProcessPendingDownloadQueue()
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
