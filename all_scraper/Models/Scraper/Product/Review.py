#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from math import floor

from Models.Static.Scrape.Status import Model_Static_Scrape_Status
from Service.Functions import Service_Functions
from Models.Scraper.Standard import Model_Scraper_Standard
class Model_Scraper_Product_Review(Model_Scraper_Standard):

    def __init__(self, region):
        self.region = region
        self.processor = Service_Functions().getProcessor('Product_Review', region)

    def scrape(self, asin, scrapedCount):
        self.process = Model_Scraper_Standard(self.region)
        url = "https://www.amazon."+self.region+"/gp/product-reviews/"+asin+"?sortBy=recent&pageNumber=1"
        print (url)
        content = self.process.processReview(url)
        if (content):
            data = {}
            items = []
            summary = self.processor.getSummary(content.encode('utf-8'))
            if (summary):
                # print (summary)
                data['summary'] = summary
            # 处理首页数据
            result = self.processor.process(content.encode('utf-8'))
            if (result):
                # print (result)
                items.append(result)

            newScrapedCount = 10
            if (data['summary']['page_count'] and data['summary']['page_count'] > 0):
                # print (data['summary']['page_count'])
                pageCount = data['summary']['page_count']
                # 已经抓取的页面
                scrapedPageCount = int(floor(int(scrapedCount) / 10))
                # print (scrapedPageCount)
                # 实际需要抓取的页面
                pageCount = pageCount - scrapedPageCount
                # print (pageCount)
                if (pageCount > 20):
                    pageCount = 2
                if (pageCount >= 2):
                    newScrapedCount = pageCount * 10
                    for i in range(2, pageCount+1):
                        pageUrl = "https://www.amazon."+self.region+"/gp/product-reviews/"+asin+"?sortBy=recent&pageNumber="+str(i)
                        print (pageUrl)
                        pageContent = self.process.processReview(pageUrl)
                        if not pageContent:
                            continue
                        # 处理page数据
                        pageResult = self.processor.process(pageContent.encode("utf-8"))
                        if (pageResult):
                            # print (pageResult)
                            # items = []
                            items.append(pageResult)
                            # print (items[0])
                            # print (items[1])
            data['list'] = items
            if (len(data) > 0):
                data['new_scraped_count'] = newScrapedCount
                # print (data)
                return data
            else:
                return Model_Static_Scrape_Status.SUCCESS_NO_DATA
        elif (content == None):
            return None
        else:
            return False
