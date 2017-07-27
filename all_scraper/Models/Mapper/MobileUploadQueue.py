#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-4-24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from Models.DbTable.DownloadQueue import Model_DbTable_DownloadQueue
from Models.Mapper.Abstract import Model_Mapper_Abstract

class Model_Mapper_MobileUploadQueue(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_MobileUploadQueue, self).__init__()
        # self.dbTable = Model_DbTable_DownloadQueue()

    # 用来存储download_queue表的sql语句
    def save(self, region, type, value):
        data = {
            "region": region,
            "type": type,
            "value": value,
        }
        result = self.findData("all", "mobile_upload_queue", data)
        if (result):
            result = self.update("mobile_upload_queue", data)
        else:
            result = self.insert("mobile_upload_queue", data)
        return result