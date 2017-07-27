#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-18'
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
# 实时记录Message的功能
# 在流程执行时记录下有关信息
from Models.Abstract import Model_Abstract
class Model_Message(Model_Abstract):
    def __init__(self):
        self.message = []

    def hasMessage(self):
        if(len(self.message)>0):
            return True
        return False

    def getMessage(self):
        return self.message

    def getMessageString(self):
        if(self.hasMessage()):
            return '\n'.join(self.message)
        return False

    def clearMessage(self):
        self.message = []

    def addMessage(self, message):
        if(message != None):
            self.message.append(message)
