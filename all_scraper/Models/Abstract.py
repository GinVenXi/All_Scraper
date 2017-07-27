#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 17:35
'''
class Model_Abstract(object):
    data = []
    origData = []
    keys = []
    hasDataChanges = False

    def __init__(self):
        pass