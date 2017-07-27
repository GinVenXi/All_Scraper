#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.processor import Model_Processor
from lxml import etree
import sys
'''
#############################################################
解析函数(主要针对产品单个评论页)
#############################################################
'''
class Model_Processor_Product_Review_Base_Cojp(Model_Processor):

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.co.jp"
            sys.exit()
        tree = etree.HTML(html)
        data = {}

        crDom = tree.xpath("//*[@class='crReviewHeader']")
        if (crDom):
            detailDom = tree.xpath("//*[contains(@class, 'hReview')]")
            if (detailDom):
                # asin 1
                try:
                    asinDom = detailDom[0].xpath(".//span[@class='item']//*[@class='asin']/text()")
                    if (asinDom):
                        data['asin'] = asinDom[0]
                        # print (asinDom[0])
                except:
                    pass
                # title 2
                try:
                    titleDom = detailDom[0].xpath(".//span[@class='summary']/text()")
                    if (titleDom):
                        data['title'] = titleDom[0].strip()
                        # print (titleDom[0].strip())
                except:
                    pass
                # description 3
                try:
                    reviewTextDom = detailDom[0].xpath(".//span[@class='description']/text()")
                    if (reviewTextDom):
                        if (reviewTextDom[0].strip() != ""):
                            data['text'] = reviewTextDom[0].strip()
                            # print (data['text'])
                        else:
                            reviewTextDom = tree.xpath("//div[@class='reviewText']/text()")
                            if (reviewTextDom):
                                if (reviewTextDom[0].strip() != ""):
                                    data['text'] = reviewTextDom[0].strip()
                                    # print (data['text'])
                except:
                    pass
                # author_name 4
                try:
                    authorDom = detailDom[0].xpath(".//span[contains(@class, 'reviewer')]/a")
                    if (authorDom):
                        data['author_name'] = authorDom[0].xpath("text()")[0]
                        # print (data['author_name'])
                        authorLink = authorDom[0].xpath("@href")
                        if ("profile" in authorLink[0]):
                            # print (authorLink[0])
                            # author_id 5
                            data['author_id'] = authorLink[0].split("/")[4]
                            # print (data['author_id'])
                            if (data['author_id']):
                                # author_url 6
                                data['author_url'] = "http://www.amazon.co.jp/gp/pdp/profile/"+data['author_id']
                                # print (data['author_url'])
                except:
                    pass
                # review_date 7
                try:
                    reviewDateDom = detailDom[0].xpath(".//span[contains(@class, 'reviewer')]//*[@class='dtreviewed']/text()")
                    if (reviewDateDom):
                        data['date'] = self.formatReviewDate(reviewDateDom[0], "co.jp")
                        # print (data['date'])
                except:
                    pass
                # rating 8
                try:
                    ratingDom = detailDom[0].xpath(".//*[@class='rating']//*[@class='value']/@title")
                    if (ratingDom):
                        data['rating'] = ratingDom[0]
                        # print (data['rating'])
                except:
                    pass
            # verified 9
            try:
                verifiedDom = tree.xpath("//*[@class='crVerifiedStripe']/b/text()")
                if (verifiedDom):
                    if (verifiedDom[0].strip() == "Amazonã§è³¼å¥"):
                        data['verified'] = 1
                        # print (data['verified'])
            except:
                pass
            # images 10
            try:
                imagesDom = tree.xpath("//img[@class='review-image-thumbnail']/@src")
                if (imagesDom):
                    images = []
                    for imageDom in imagesDom:
                        images.append(self.formatImage(imageDom))
                    data['images'] = images
            except:
                pass
            # vedio_url 11  /html/body/table/tbody/tr/td[1]/div[1]/div[6]/div/script[2]/text()
            try:
                vedioDom = tree.xpath("//*[@class='reviewText']//script[2]/text()")
                if (vedioDom):
                    if ("streamingUrls" in vedioDom[0]):
                        # print (vedioDom[0])
                        sStr1 = vedioDom[0]
                        sStr2 = "streamingUrls"
                        sStr3 = ".mp4"
                        nPos = sStr1.index(sStr2)
                        # print (nPos)
                        nPos1 = sStr1.index(sStr3)
                        # print (nPos1)
                        data['vedio_url'] = sStr1[nPos+16:nPos1+4]
                        # print (data['vedio_url'])
            except:
                pass
        if (len(data) > 0):
            return data
        else:
            return False