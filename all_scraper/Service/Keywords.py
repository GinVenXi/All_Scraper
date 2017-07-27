#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Keys import Model_Keys
from Models.Mapper.Amazon import Model_Mapper_Amazon
from Models.Mapper.AmazonProduct import Model_Mapper_AmazonProduct
from Models.Mapper.AmazonProductImage import Model_Mapper_AmazonProductImage
from Models.Mapper.AmazonProductKeywordsAd import Model_Mapper_AmazonProductKeywordsAd
from Models.Mapper.AmazonProductKeywordsRank import Model_Mapper_AmazonProductKeywordsRank
from Models.Mapper.Connect import Model_Mapper_Connect
from Models.Mapper.Keywords import Model_Mapper_Keywords
from Models.Mapper.Mysql import Model_Mapper_Mysql
from Models.Scraper.Keyswords.First import Model_Scraper_Keywords_First
from Models.Static.Amazon.Product.Keywords.Ad.AdPositionType import Model_Static_Amazon_Product_Keywords_Ad_AdPositionType
from Models.Static.DownloadQueue.Status import Model_Static_DownloadQueue_Status
from Models.Static.DownloadQueue.Type import Model_Static_DownloadQueue_Type
from Service.Abstract import Service_Abstract
from Models.Static.Region import Model_Static_Region
from Models.Scraper.keywords import Model_Scraper_Keywords

class Service_Keywords(Service_Abstract):
    def __init__(self):
        super(Service_Keywords, self).__init__()
        self.amazonProductKeywordsRankMapper = Model_Mapper_AmazonProductKeywordsRank()
        self.amazonProductKeywordsAdMapper = Model_Mapper_AmazonProductKeywordsAd()
        self.keywordsMapper = Model_Mapper_Keywords()
        self.amazonProductMapper = Model_Mapper_AmazonProduct()
        self.amazonProductImageMapper = Model_Mapper_AmazonProductImage()

    def getAmazonKeywordsRankMapper(self):
        return self.amazonProductKeywordsRankMapper

    def getAmazonKeywordsAdMapper(self):
        return self.amazonProductKeywordsAdMapper

    def getKeywordsMapper(self):
        return self.keywordsMapper

    def getAmazonProductMapper(self):
        return self.amazonProductMapper

    def getAmazonProductImageMapper(self):
        return self.amazonProductImageMapper

    def getUploadQueueMapper(self):
        return self.uploadQueueMapper

    def scrapeFirst(self, downloadQueue):
        try:
            self.region = downloadQueue[2]
            self.type = downloadQueue[3]
            self.value = downloadQueue[4].encode('utf-8')
            region = Model_Static_Region()
            reg = region.getText(self.region)
            keywords = self.value
            self.scraper = Model_Scraper_Keywords_First(reg)
            data = self.scraper.scraper(keywords)
            # 操作scrape表，写入抓取日志
            if (self.scraper.hasScrapes()):
                # 执行写入操作
                self.saveScrapes(self.scraper.getScrapes(), downloadQueue)
            node_id = 0
            scrapeSuccess = False
            if (data):
                print (len(data))
                # print (data)
                try:
                    # 在插入数据库操作前，先将该广告关键词表中的数据清除
                    self.getAmazonKeywordsAdMapper().clearAdData(reg, keywords, str(node_id))
                except Exception as err:
                    print (err)
                try:
                    # 在插入数据库操作前，先将该普通排名关键词下的数据清除
                    self.getAmazonKeywordsRankMapper().clearRankData(reg, keywords, str(node_id))
                except Exception as err:
                    print (err)
                # 更新新的数据
                # print (data)
                if (data[-1]["total"] > 0):
                    scrapeSuccess = True
                    rank = 1  # 绝对排名
                    position = 1  # 广告绝对位置
                    try:
                        for index in range(len(data) - 1):
                            # 处理广告
                            if (data[index]['sponsor'] == 1):
                                if (data[index]['sponsor_position_type'] == 'right'):
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().RIGHT
                                elif (data[index]['sponsor_position_type'] == 'top'):
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().TOP
                                else:
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().BOTTOM
                                ad_position = data[index]['sponsor_position']
                                try:
                                    result = self.getAmazonKeywordsAdMapper().save(reg, keywords, node_id, ad_position, ad_position_type, position, data[index])
                                except Exception as err:
                                    print (err)
                                if (result):
                                    position += 1
                            # 处理自然排名
                            else:
                                try:
                                    result = self.getAmazonKeywordsRankMapper().save(reg, keywords, node_id, rank, data[index])
                                except Exception as err:
                                    print (err)
                                if (result):
                                    rank += 1
                    except Exception as err:
                        print (err)
                # 若未抓出数据，进行相应操作
                elif (data[-1]["total"] == 0):
                    scrapeSuccess = True
                # 存储产品基本信息
                for index in range(len(data) - 1):
                    try:
                        self.saveAmazonProduct(reg, data[index])
                    except:
                        print ("saveAmazonProduct error")

                # 存储关键词基本信息
                if (data[-1]["total"] > 0):
                    try:
                        self.getKeywordsMapper().save(reg, keywords, str(data[-1]["total"]))
                    except Exception as err:
                        print (err)
                if (scrapeSuccess):
                    return Model_Static_DownloadQueue_Status.SCRAPED
                else:
                    return Model_Static_DownloadQueue_Status.FAILED
            elif (data == False):
                return Model_Static_DownloadQueue_Status.SCRAPED_WRONG
            else:
                # 若未抓出数据，进行相应操作
                return Model_Static_DownloadQueue_Status.SCRAPED_NO_DATA
        except Exception as err:
            print (err)

    def scrape(self, downloadQueue):
        self.region = downloadQueue[2]
        self.type = downloadQueue[3]
        self.value = downloadQueue[4].encode('utf-8')
        region = Model_Static_Region()
        reg = region.getText(self.region)
        keywords = self.value
        self.scraper = Model_Scraper_Keywords(reg)
        results = self.scraper.scraper(keywords)
        # 操作scrape表，写入抓取日志
        if (self.scraper.hasScrapes()):
            # 执行写入操作
            try:
                self.saveScrapes(self.scraper.getScrapes(), downloadQueue)
            except:
                pass
        node_id = 0
        scrapeSuccess = False
        if (results):

            # # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
            # amazon = Model_Mapper_Amazon()
            # # 连接数据库
            # db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
            # conn = db.connects()
            # mapper = Model_Mapper_Mysql(conn)

            try:
                # 在插入数据库操作前，先将该广告关键词表中的数据清除
                # sql = amazon.keywords_ad_delete_sql_joint(reg, keywords, str(node_id))
                # mapper.delete(sql)
                self.getAmazonKeywordsAdMapper().clearAdData(reg, keywords, str(node_id))
            except Exception as err:
                print (err)
            try:
                # 在插入数据库操作前，先将该普通排名关键词下的数据清除
                # sql = amazon.keywords_rank_delete_sql_joint(reg, keywords, str(node_id))
                # mapper.delete(sql)
                self.getAmazonKeywordsRankMapper().clearRankData(reg, keywords, str(node_id))
            except Exception as err:
                print (err)
            # 更新新的数据
            # print (results)
            for data in results:
                # print (data[-1])
                if (data[-1]["total"] > 0):
                    scrapeSuccess = True
                    rank = 1  # 绝对排名
                    position = 1  # 广告绝对位置
                    try:
                        for index in range(len(data) - 1):
                            # 处理广告
                            if (data[index]['sponsor'] == 1):
                                if (data[index]['sponsor_position_type'] == 'right'):
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().RIGHT
                                elif (data[index]['sponsor_position_type'] == 'top'):
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().TOP
                                else:
                                    ad_position_type = Model_Static_Amazon_Product_Keywords_Ad_AdPositionType().BOTTOM
                                ad_position = data[index]['sponsor_position']
                                try:
                                    result = self.getAmazonKeywordsAdMapper().save(reg, keywords, node_id, ad_position, ad_position_type, position, data[index])
                                except Exception as err:
                                    print (err)
                                # sql = amazon.keywords_ad_insert_sql_joint(reg, keywords, node_id, ad_position, ad_position_type, position, data[index])
                                # result = mapper.insert(sql)
                                if (result):
                                    position += 1
                            # 处理自然排名
                            else:
                                try:
                                    result = self.getAmazonKeywordsRankMapper().save(reg, keywords, node_id, rank, data[index])
                                except Exception as err:
                                    print (err)
                                # sql = amazon.keywords_rank_insert_sql_joint(reg, keywords, node_id, rank, data[index])
                                # result = mapper.insert(sql)
                                if (result):
                                    rank += 1
                    except Exception as err:
                        print (err)
                # 若未抓出数据，进行相应操作
                elif (data[-1]["total"] == 0):
                    scrapeSuccess = True
                # 存储产品基本信息
                for index in range(len(data) - 1):
                    # print (data[index])
                    try:
                        self.saveAmazonProduct(reg, data[index])
                    except:
                        print ("saveAmazonProduct error")
                # for index in range(len(data) - 1):
                #     sql = amazon.keywords_product_insert_sql_joint(reg, data[index])
                ################################xiugaiasdsadasdfsadfas###############################
            # 存储关键词基本信息
            if (results[0][-1]["total"] > 0):
                try:
                    self.getKeywordsMapper().save(reg, keywords, str(results[0][-1]["total"]))
                except:
                    print ("Keywords insert error")
            #     sql = amazon.keywordsObject_select_sql_joint(reg, keywords)
            #     result = mapper.select(sql)
            #     if (result):
            #         sql = amazon.keywordsObject_update_sql_joint(reg, keywords, str(results[0][-1]))
            #         result = mapper.update(sql)
            #     else:
            #         sql = amazon.keywordsObject_insert_sql_joint(reg, keywords, str(results[0][-1]))
            #         result = mapper.insert(sql)
            #     if (result):
            #         scrapeSuccess = True
            # conn.close()
            if (scrapeSuccess == True):
                return Model_Static_DownloadQueue_Status.SCRAPED
            else:
                return Model_Static_DownloadQueue_Status.FAILED
        elif (results == False):
            return Model_Static_DownloadQueue_Status.SCRAPED_WRONG
        else:
            return Model_Static_DownloadQueue_Status.FAILED
        # except Exception as err:
        #     print (err)

    def saveAmazonProduct(self, region, item):
        # 必须要封装成类，不然很麻烦###########################
        # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
        # amazon = Model_Mapper_Amazon()
        # # 连接数据库
        # db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        # conn = db.connects()
        # mapper = Model_Mapper_Mysql(conn)
        try:
            asin = item['asin']

            # print (item['rating'])
            # 插入基本产品信息
            # print (asin)
            if (asin):
                try:
                    result = self.getAmazonProductMapper().save(region, asin, item)
                    # sql = amazon.product_select_sql_joint(region, asin)
                    # result = mapper.select(sql)
                    # if (result):
                    #     sql = amazon.product_update_sql_joint(region, asin, item)
                    #     result = mapper.update(sql)
                    #     if (result):
                    #         scrapeSuccess = True
                    # else:
                    #     sql = amazon.product_insert_sql_joint(region, asin, item)
                    #     result = mapper.insert(sql)
                    #     if (result):
                    #         scrapeSuccess = True
                except Exception as err:
                    print (err)
                if (result):
                    # 插入或更新图片信息
                    try:
                        if (item['image']):
                            self.getAmazonProductImageMapper().save_img(region, asin, item)
                            # # print (item['image'])
                            # sql = amazon.product_image_select_sql_joint(region, asin)
                            # result = mapper.select(sql)
                            # if (result):
                            #     pass
                            # else:
                            #     sql = amazon.product_image_insert_sql_joint(region, asin, item)
                            #     result = mapper.insert(sql)
                            #     if (result):
                            #         scrapeSuccess = True
                    except Exception as err:
                        print (err)
                        print ("insert image error")
                    try:
                        self.addUploadQueue(self.region, Model_Static_DownloadQueue_Type.PRODUCT, asin)
                        # sql = amazon.getUploadQueue_select_sql_joint(self.region, Model_Static_DownloadQueue_Type.PRODUCT, asin)
                        # result = mapper.select(sql)
                        # if (result):
                        #     sql = amazon.getUploadQueue_update_sql_joint(self.region, Model_Static_DownloadQueue_Type.PRODUCT, asin)
                        #     result = mapper.update(sql)
                        # else:
                        #     sql = amazon.getUploadQueue_insert_sql_joint(self.region, Model_Static_DownloadQueue_Type.PRODUCT, asin)
                        #     result = mapper.insert(sql)
                        # if (result):
                        #     scrapeSuccess = True
                    except Exception as err:
                        print (err)
                        # print ("getUploadQueue error")
        except Exception as err:
            print (err)

    # 获取指定关键词的amazon_keywords_rank和amazon_keywords_ad数据并上传
    def getAmazonKeywordsUploadData(self, region, keywords):
        data = {}
        # 数据库初始化操作，判断数据有效性，然后对数据进行后续操作
        amazon = Model_Mapper_Amazon()
        # 连接数据库
        db = Model_Mapper_Connect('localhost', 3306, 'root', '123123', 'scraper', 'utf8')
        conn = db.connects()
        mapper = Model_Mapper_Mysql(conn)
        # 获取rank keywords数据
        sql = amazon.getAmazonProductKeywordsRank_select_sql_joint(region, keywords)
        rankData = mapper.select(sql)
        rankData_key = Model_Keys.rankdata_key
        rankData_list = []
        for rankdata in rankData:
            rankData_list.append(dict(zip(rankData_key, rankdata)))
        if (rankData_list):
            data['rank'] = {
                'region': region,
                'keywords': keywords,
                'list': rankData_list,
            }
        # 获取ad keywords数据
        sql = amazon.getAmazonProductKeywordsAd_select_sql_joint(region, keywords)
        adData = mapper.select(sql)
        adData_key = Model_Keys.addata_key
        adData_list = []
        for addata in adData:
            adData_list.append(dict(zip(adData_key, addata)))
        if (adData_list):
            data['ad'] = {
                'region': region,
                'keywords': keywords,
                'list': adData_list,
            }
        # 获取搜索关键词数据
        sql = amazon.getKeywords(region, keywords)
        keywordsData = mapper.select(sql)
        if (keywordsData):
            keywordsData_key = Model_Keys.keywords_key
            keywords_list = []
            for keywordsdata in keywordsData:
                keywords_list.append(dict(zip(keywordsData_key, keywordsdata)))
            data['keywords'] = keywords_list[0]
        # print (data)
        if (len(data) > 0):
            return data
        return False

    def getAmazonKeywordsRankUploadData(self, region, keywords):
        pass

    def getAmazonKeywordsInfoUploadData(self, region, keywords):
        pass