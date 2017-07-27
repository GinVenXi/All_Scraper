#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Service.Abstract import Service_Abstract
import urllib

class Service_Functions(Service_Abstract):

    def getProcessor(self , scraper = 'Product_Base', region = 'com'):
        region = ''.join(region.split('.')).lower()
        region = region[0].upper() + region[1:]
        if(region=='Com' and scraper == 'Product_Base'):
            # modulePath是模块文件的路径 + 模块的文件名。
            module = 'Models.Processor.' + '.'.join(scraper.split('_')) + '.' + region
            # print module
            aMod = __import__(module, fromlist= True)
            obj = getattr(aMod, 'Model_Processor_' + scraper + '_' + region)()
            return obj
        else:
            module = 'Models.Processor.' + '.'.join(scraper.split('_')) + '.' + region
            aMod = __import__(module, fromlist= True)
            obj = getattr(aMod, 'Model_Processor_' + scraper + '_' + region)()
            return obj

    # 新浪新闻
    def getSinaProcessor(self, scraper = 'Sina_Base'):
        if (scraper  == 'Sina_Base'):
            # modulePath是模块文件的路径 + 模块的文件名。
            module = 'Models.Processor.' + '.'.join(scraper.split('_'))
            # print module
            aMod = __import__(module, fromlist=True)
            obj = getattr(aMod, 'Model_Processor_' + scraper)()
            return obj
        else:
            module = 'Models.Processor.' + '.'.join(scraper.split('_'))
            aMod = __import__(module, fromlist=True)
            obj = getattr(aMod, 'Model_Processor_' + scraper)()
            return obj

    # 腾讯新闻
    def getTencentProcessor(self, scraper = 'Tencent_Base'):
        if (scraper  == 'Tencent_Base'):
            # modulePath是模块文件的路径 + 模块的文件名。
            module = 'Models.Processor.' + '.'.join(scraper.split('_'))
            # print module
            aMod = __import__(module, fromlist=True)
            obj = getattr(aMod, 'Model_Processor_' + scraper)()
            return obj
        else:
            module = 'Models.Processor.' + '.'.join(scraper.split('_'))
            aMod = __import__(module, fromlist=True)
            obj = getattr(aMod, 'Model_Processor_' + scraper)()
            return obj


    def formatNumber(self, number, region="com"):
        if(region == "com"):
            self.number = number.replace(".", "").replace("$", "").replace("#", "").replace(",", "")
        elif(region == "co.uk"):
            pass
        elif(region == "de"):
            pass
        elif(region == "co.jp"):
            pass
        elif(region == "fr" or region == "es" or region == "it"):
            pass
        else:
            pass

        return self.number

    def formatRating(self, rating, region="com"):
        if (region == "com"):
            self.rating = rating.replace(" out of 5 stars" , "")
        elif (region == "co.uk"):
            pass
        elif (region == "de"):
            pass
        elif (region == "co.jp"):
            pass
        elif (region == "fr"):
            pass
        elif (region == "es"):
            pass
        elif (region == "it"):
            pass

        return self.rating

    def formatDate(self, date, region="com"):
        if (region == "com" or region == "co.uk"):
            pass
        elif (region == "de"):
            pass
        elif (region == "co.jp"):
            pass
        elif (region == "fr"):
            pass
        elif (region == "es"):
            pass
        elif (region == "it"):
            pass

        return date

    # 合并offerlist信息和库存信息
    def mergeDict(self, data, inventroy):

        for i in range(len(data)):
            # inventory字典  生成key
            # try:
            #     print (urllib.unquote(data[i]['offering_id']))
            # except Exception as err:
            #     print (err)
            # 将库存信息添加至offerlist信息中
            # try:
            #     print (inventroy)
            #     print (inventroy[urllib.unquote(data[i]['offering_id'])])
            # except Exception as err:
            #     print (err)
            # item_id
            # try:
            #     print (inventroy[urllib.unquote(data[i]['offering_id'])].split(".")[0])
            # except Exception as err:
            #     print (err)
            try:
                if (inventroy[urllib.unquote(data[i]['offering_id'])].split(".")[1] != ''):
                    data[i].setdefault("inventory", inventroy[urllib.unquote(data[i]['offering_id'])].split(".")[1])
                else:
                    pass
            except:
                continue
            try:
                if (inventroy[urllib.unquote(data[i]['offering_id'])].split(".")[0] != ''):
                    data[i].setdefault("item_id", inventroy[urllib.unquote(data[i]['offering_id'])].split(".")[0])
                else:
                    pass
            except:
                continue

        return data

    def mergeItem_idDict(self, data, item_id):
        for i in range(len(item_id)):
            data[i].setdefault("item_id", item_id[i])

        return data