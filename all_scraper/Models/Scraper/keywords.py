#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Scraper.Standard import Model_Scraper_Standard
from Service.Functions import Service_Functions
from pyvirtualdisplay import Display

class Model_Scraper_Keywords(Model_Scraper_Standard):
    def __init__(self, region):
        super(Model_Scraper_Keywords, self).__init__(region)
        self.region = region
        self.processor = Service_Functions().getProcessor('Keywords', region)

    def scraper(self, keywords):
        self.process = Model_Scraper_Standard(self.region)
        url = "https://www.amazon."+self.region+"/gp/search?keywords="+keywords+"&page=1"
        # 不显示浏览器
        # with Display(backend="xvfb", size=(1440, 900)):
        print (url)
        try:
            content = self.process.processkeywords(url)
        except Exception as err:
            print (err)
        try:
            if (content):
                # 这边写解析代码
                data = []
                result = self.processor.process(content.encode('utf-8'), 1)
                if (result):
                    # print (result)
                    data.append(result)
                    pagecount = int(self.processor.getPageCount(content))
                    if (pagecount > 5):
                        pagecount = 5
                    # pagecount = 1
                    if (pagecount > 1):
                        for i in range(2, pagecount + 1):
                            pageurl = "https://www.amazon." + self.region + "/gp/search?keywords=" + keywords + "&page=" + str(i)
                            print (pageurl)
                            pagecontent = self.process.processkeywords(pageurl)
                            if (pagecontent):
                                pageresult = self.processor.process(pagecontent.encode('utf-8'), i)
                                # print (pageresult)
                                data.append(pageresult)
                    return data
            elif (content == None):
                return None
            else:
                return False
        except:
            return False

        # # 保存文件
        # #
        # def save_detail(self, asin, html):
        #     if os.path.exists('/home/javen/PycharmProjects/AMAZON_SCRAPY/Downloader/Amazon_Data/'):
        #         os.chdir('/home/javen/PycharmProjects/AMAZON_SCRAPY/Downloader/Amazon_Data/')
        #     else:
        #         os.mkdir('/home/javen/PycharmProjects/AMAZON_SCRAPY/Downloader/Amazon_Data/')
        #         os.chdir('/home/javen/PycharmProjects/AMAZON_SCRAPY/Downloader/Amazon_Data/')
        #     try:
        #         if (os.path.exists(asin + '.html')):
        #             print(str(asin) + " has existed")
        #             return True
        #         else:
        #             html_content = open(asin + '.html', 'w')
        #             # html_content.encoding('utf-8')
        #             html_content.write(html)
        #             html_content.close()
        #             return True
        #     except Exception as err:
        #         print('Save_detail exception happened:' + str(err))
