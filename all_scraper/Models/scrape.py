#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Abstract import Model_Abstract
class Model_Scrape(Model_Abstract):
    keys = ['id', 'download_queue_id', 'method', 'url', 'proxy_id', 'begin_time', 'end_time', 'status', 'comment', 'time']