#coding: utf-8
'''
创建人：Javen
创建时间：
'''

class Model_Static_DownloadQueue_Status(object):
    PENDING = 0
    SCRAPED = 1
    SCRAPED_NO_DATA = 2
    FAILED = 3
    SCRAPED_WRONG = 4

    def getText(self, num):
        if (num == 1):
            return "SUCCESS"
        elif (num == 2):
            return "SUCCESS NO DATA"
        elif (num == 3):
            return "FAILED"
        else:
            return "SCRAPED_WRONG"