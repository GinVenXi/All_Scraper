#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-2-17'
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
class Model_Static_Region():
    COM = 0
    CO_UK = 1
    CA = 2
    COM_MX = 3
    CN = 4
    FR = 5
    DE = 6
    IN = 7
    IT = 8
    ES = 9
    CO_JP = 10
    COM_BR = 11

    def __init__(self):
        self.COM = 'com',
        self.CO_UK = 'co.uk',
        self.CA = 'ca',
        self.COM_MX = 'com.mx',
        self.CN = 'cn',
        self.FR = 'fr',
        self.DE = 'de',
        self.IN = 'in',
        self.IT = 'it',
        self.ES = 'es',
        self.CO_JP = 'co.jp',
        self.COM_BR = 'com.br',

    def getAvailableRegions(self):
        return ["0", "1", "6", "10", "5", "9", "8", "2"]#, self.CO_UK, self.DE, self.CO_JP, self.FR, self.ES, self.IT]

    def getText(self, region):
        if(region == 0):
            return 'com'
        elif(region == 1):
            return 'co.uk'
        elif (region == 2):
            return 'ca'
        elif (region == 3):
            return 'com.mx'
        elif (region == 4):
            return 'cn'
        elif (region == 5):
            return 'fr'
        elif (region == 6):
            return 'de'
        elif (region == 7):
            return 'in'
        elif (region == 8):
            return 'it'
        elif (region == 9):
            return 'es'
        elif (region == 10):
            return 'co.jp'
        elif (region == 11):
            return 'com.br'