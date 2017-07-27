#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Keys import Model_Keys
from Models.Mapper.AmazonProduct import Model_Mapper_AmazonProduct
from Models.Mapper.AmazonProductReview import Model_Mapper_AmazonProductReview
from Models.Mapper.AmazonProductReviewImage import Model_Mapper_AmazonProductReviewImage
from Models.Mapper.AmazonProductReviewVideo import Model_Mapper_AmazonProductReviewVideo
from Models.Scraper.Product.Review import Model_Scraper_Product_Review
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Models.Static.Region import Model_Static_Region
from Service.Abstract import Service_Abstract
class Service_Review(Service_Abstract):
    def __init__(self):
        super(Service_Review, self).__init__()
        self.amazonProductMapper = Model_Mapper_AmazonProduct()
        self.amazonProductReviewMapper = Model_Mapper_AmazonProductReview()
        self.amazonProductReviewImageMapper = Model_Mapper_AmazonProductReviewImage()
        self.amazonProductReviewVideoMapper = Model_Mapper_AmazonProductReviewVideo()

    def getAmazonProductMapper(self):
        return self.amazonProductMapper

    def getAmazonProductReviewMapper(self):
        return self.amazonProductReviewMapper

    def getAmazonProductReviewImageMapper(self):
        return self.amazonProductReviewImageMapper

    def getAmazonProductReviewVideoMapper(self):
        return self.amazonProductReviewVideoMapper

    def scrape(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            self.type = downloadQueue[3]
            self.value = downloadQueue[4].encode("utf-8")
            region = Model_Static_Region()
            reg = region.getText(self.region)
            scrapedCount = 0
            if ("/" in self.value):
                asin = self.value.split("/")[0]
                scrapedCount = self.value.split("/")[1]
            else:
                asin = self.value
            self.scraper = Model_Scraper_Product_Review(reg)
            data = self.scraper.scrape(asin, scrapedCount)

            # 操作scrape表，写入抓取日志
            if (self.scraper.hasScrapes()):
                # 执行写入操作
                self.saveScrapes(self.scraper.getScrapes(), downloadQueue)
            scrapeSuccess = False
            if (data):
                if (data['list'] and isinstance(data['list'], list)):
                    scrapeSuccess = True
                    for items in data['list']:
                        for item in items:
                            # print (item)
                            if (item):
                                amazonProductReview = {}
                                amazonProductReview['region'] = reg
                                amazonProductReview['review_id'] = item['id']
                                amazonProductReview['asin'] = asin
                                try:
                                    amazonProductReview['customer_id'] = item['author_id']
                                except:
                                    pass
                                try:
                                    amazonProductReview['customer_name'] = item['author_name']
                                except:
                                    pass
                                try:
                                    amazonProductReview['title'] = item['title']
                                except:
                                    pass
                                try:
                                    amazonProductReview['description'] = item['text']
                                except:
                                    pass
                                try:
                                    amazonProductReview['rating'] = item['rating']
                                except:
                                    pass
                                try:
                                    amazonProductReview['date'] = item['date']
                                except:
                                    pass
                                try:
                                    amazonProductReview['helpful_yes'] = item['helpful_yes']
                                except:
                                    pass
                                try:
                                    amazonProductReview['is_verified'] = item['verified']
                                except:
                                    pass
                                try:
                                    if (item['images'] and isinstance(item['images'], list) and len(item['images']) > 0):
                                        amazonProductReview['is_image_included'] = 1
                                    else:
                                        amazonProductReview['is_image_included'] = 0
                                except:
                                    pass
                                try:
                                    if (item['video_url']):
                                        amazonProductReview['is_video_included'] = 1
                                    else:
                                        amazonProductReview['is_video_included'] = 0
                                except:
                                    pass
                                if (self.getAmazonProductReviewMapper().save(amazonProductReview)):
                                    try:
                                        if (amazonProductReview['is_image_included']):
                                            for index, image_url in enumerate(item['images']):
                                                amazonProductReviewImage = {}
                                                amazonProductReviewImage['region'] = reg
                                                amazonProductReviewImage['review_id'] = item['id']
                                                amazonProductReviewImage['url'] = image_url
                                                amazonProductReviewImage['key'] = index
                                                self.getAmazonProductReviewImageMapper().save(amazonProductReviewImage)
                                    except:
                                        pass
                                    try:
                                        if (amazonProductReview['is_video_included']):
                                            amazonProductReviewVideo = {}
                                            amazonProductReviewVideo['region'] = reg
                                            amazonProductReviewVideo['revier_id'] = item['id']
                                            amazonProductReviewVideo['url'] = item['video_url']
                                            amazonProductReviewVideo['image_url'] = item['video_image_url']
                                            self.getAmazonProductReviewVideoMapper().save(amazonProductReviewVideo)
                                    except:
                                        pass
                    if (data['new_scraped_count']):
                        downloadQueue = list(downloadQueue)
                        downloadQueue[4] = downloadQueue[4]+":"+str(data['new_scraped_count'])
                        downloadQueueKey = Model_Keys.downloadqueue_key
                        downloadQueue = dict(zip(downloadQueueKey, downloadQueue))
                        # print (downloadQueue)
                        self.getDownloadQueueMapper().saveReview(downloadQueue)
                    if (scrapeSuccess):
                        return Model_Static_DownloadQueue_Status.SCRAPED
            elif (data == False):
                return Model_Static_DownloadQueue_Status.SCRAPED_WRONG
            else:
                # 若未抓出数据，进行相应操作
                return Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA
        except Exception as err:
            print (err)
