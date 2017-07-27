#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time
from Service.NewsQueue import Service_NewsQueue


class Service_Cronjob_ProcessPendingTencentDownloadQueue():

    def start(self):
        bt = time.time()
        print("Parent Begin:" + str(bt) + "\n")
        try:
            # 腾讯各种页面
            urls = {
                # Base
                "base": "http://www.qq.com/",
                # 新闻
                "news": "http://news.qq.com/",
                # 财经
                "finance": "http://finance.qq.com/",
                # 体育
                "sports": "http://sports.qq.com/",
                # 娱乐
                "ent": "http://ent.qq.com/",
                # 时尚
                "fashion": "http://fashion.qq.com/",
                # 汽车
                "auto": "http://auto.qq.com/",
                # 房产
                "house": "http://house.qq.com/",
                # 科技
                "tech": "http://tech.qq.com/",
                # 游戏
                "games": "http://games.qq.com/",
                # 教育
                "edu": "http://edu.qq.com/",
                # 文化
                "cul": "http://cul.qq.com/",
                # 公益
                "gongyi": "http://gongyi.qq.com/"

            }
            queueService = Service_NewsQueue()
            for key, value in urls.items():
                print (key)
                print (value)
                queueService.processPendingTencentDownloadQueue(key, value)
                time.sleep(2)

        except Exception as err:
            print (err)

        tt = time.time()
        tseconds = tt - bt
        print ("Process Time:" + str(tseconds) + "\n")
        et = time.time()
        print ("Parent End:" + str(et) + "\n")
        print ("Parent" + str(et-bt) + "seconds\n")