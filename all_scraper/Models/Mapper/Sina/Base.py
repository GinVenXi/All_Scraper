#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Mapper.Sina.Abstract import Model_Mapper_Sina_Abstract
class Model_Mapper_Sina_Base(Model_Mapper_Sina_Abstract):
    def __init__(self):
        super(Model_Mapper_Sina_Base, self).__init__()

    def save(self, data):
        searchData = {
            'url_id': data['url_id'],
        }
        result = self.findData("all", "sina_download_queue", searchData)
        if (result):
            result = True
            # result = self.update("download_queue", data)
        else:
            result = self.insert("sina_download_queue", data)
        return result

    def save_status(self, data):
        searchData = {
            'url_id': data['url_id'],
        }
        result = self.findData("all", "sina_download_queue", searchData)
        if (result):
            result = self.update("sina_download_queue", data)
        else:
            result = self.insert("sina_download_queue", data)
        return result

    def save_content(self, data):
        searchData = {
            'url_id': data['url_id'],
        }
        result = self.findData("all", "sina_pages", searchData)
        if (result):
            result = self.update("sina_pages", data)
        else:
            result = self.insert("sina_pages", data)
        return result

    def find(self):
        searchData = {
            'status': "0",
        }
        result = self.findData("all", "sina_download_queue", searchData)
        if (result):
            return result
        else:
            return False