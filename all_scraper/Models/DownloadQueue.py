#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17:34
'''
from Models.Abstract import Model_Abstract
class Model_DownloadQueue(Model_Abstract):

    keys = ['id','ac_download_queue_id','region','type','value','status','priority','scrape_count','upload_status','upload_count','last_updated_time','time']