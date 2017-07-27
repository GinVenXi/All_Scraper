#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17:12
'''
from Models.DbTable.Abstract import Model_DbTable_Abstract

class Model_DbTable_DownloadQueue(Model_DbTable_Abstract):
    def __init__(self):
        name = 'download_queue'

