#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import time
from Service.NewsQueue import Service_NewsQueue


class Service_Cronjob_ProcessPendingSinaDownloadQueue():

    def start(self):
        bt = time.time()
        print("Parent Begin:" + str(bt) + "\n")
        try:
            # 新浪各种页面
            urls = {
                "base": "http://www.sina.com.cn/",
                "news": "http://news.sina.com.cn/",
                "finance": "http://finance.sina.com.cn/",
                "tech": "http://tech.sina.com.cn/",
                "sports": "http://sports.sina.com.cn/",
                "ent": "http://ent.sina.com.cn/",
                # 汽车页面需要进行点击更多操作，可以用phantomjs+selenium进行操作(ok)
                "auto": "http://auto.sina.com.cn/",
                # 博客页面需要进行翻页，可以用phantomjs+selenium进行操作(ok)
                "blog": "http://blog.sina.com.cn/",
                "video": "http://video.sina.com.cn/",
                "fashion": "http://fashion.sina.com.cn/",
                # 教育页面需要进行翻页，可以用phantomjs+selenium进行操作(ok)
                # "edu": "http://edu.sina.com.cn/",
                "city": "http://city.sina.com.cn/",
                # 旅游页面需要进行翻页，可以用phantomjs+selenium进行操作(ok)
                "travel": "http://travel.sina.com.cn/",
                "games": "http://games.sina.com.cn/",

            }
            queueService = Service_NewsQueue()
            for key, value in urls.items():
                print (key)
                print (value)
                queueService.processPendingSinaDownloadQueue(key, value)
                time.sleep(2)

        except Exception as err:
            print (err)

        tt = time.time()
        tseconds = tt - bt
        print ("Process Time:" + str(tseconds) + "\n")
        et = time.time()
        print ("Parent End:" + str(et) + "\n")
        print ("Parent" + str(et-bt) + "seconds\n")