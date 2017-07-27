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
解析函数(主要针对产品评论页)
#############################################################
'''
class Model_Processor_Product_Review_Couk(Model_Processor):

    def process(self, html):

        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.co.uk"
            sys.exit()
        tree = etree.HTML(html)
        data = []
        listDoms = tree.xpath("//*[@id='cm_cr-review_list']/div[contains(@class, 'review')]")
        if (listDoms):
            for listDom in listDoms:
                item = {}
                # 用户id
                try:
                    idDom = listDom.xpath("@id")
                    if (idDom):
                        item['id'] = idDom[0]
                        # print (item['id'])
                except Exception as err:
                    print (err)
                # rating
                try:
                    ratingDom = listDom.xpath("div//*[contains(@class, 'review-rating')]/span/text()")
                    if (ratingDom):
                        item['rating'] = self.formatRating(ratingDom[0], "co.uk")
                        # print (item['rating'])
                except Exception as err:
                    print (err)
                # title
                try:
                    titleDom = listDom.xpath("div//*[contains(@class, 'review-title')]/text()")
                    if (titleDom):
                        item['title'] = titleDom[0]
                        # print (item['title'])
                except Exception as err:
                    print (err)
                # author_name
                try:
                    author_nameDom = listDom.xpath("div//a[contains(@class, 'author')]/text()")
                    if (author_nameDom):
                        item['author_name'] = author_nameDom[0]
                        # print (item['author_name'])
                except Exception as err:
                    print (err)
                # author_id
                try:
                    author_idDom = listDom.xpath("div//a[contains(@class, 'author')]/@href")
                    if (author_idDom):
                        item['author_id'] = author_idDom[0].split("/")[4]
                        # print (item['author_id'])
                except Exception as err:
                    print (err)
                # author_url
                try:
                    if (item['author_id']):
                        item['author_url'] = "http://www.amazon.co.uk/gp/pdp/profile/"+item['author_id']
                        # print (item['author_url'])
                except Exception as err:
                    print (err)
                # review_date
                try:
                    review_dateDom = listDom.xpath("div//span[contains(@class, 'review-date')]/text()")
                    if (review_dateDom):
                        item['date'] = self.formatReviewDate(review_dateDom[0], "co.uk")
                        # print (item['date'])
                except Exception as err:
                    print (err)
                # verified
                try:
                    verifiedDom = listDom.xpath("div//div[contains(@class, 'review-format-strip')]//span[contains(@class, 'a-color-state')]/text()")
                    if (verifiedDom):
                        if (verifiedDom[0] == "Verified Purchase"):
                            item['verified'] = 1
                            # print (item['verified'])
                except Exception as err:
                    print (err)
                # review-text
                try:
                    textDom = listDom.xpath("div//span[contains(@class, 'review-text')]/text()")
                    if (textDom):
                        item['text'] =textDom[0]
                        # print (item['text'])
                except Exception as err:
                    print (err)
                ##########################未找到现有实例
                # video-url
                try:
                    video_urlDom = listDom.xpath("div//span[contains(@class, 'video-url')]/@value")
                    if (video_urlDom):
                        item['video_url'] = video_urlDom[0]
                        print (item['video_url'])
                except:
                    pass
                # video image_url
                try:
                    video_imageurlDom = listDom.xpath("div//span[contains(@class, 'video-slate-img-url')]/@value")
                    if (video_imageurlDom):
                        item['video_image_url'] = video_imageurlDom[0]
                        print (item['video_image_url'])
                except:
                    pass
                # images
                try:
                    imagesDom = listDom.xpath("div//div[contains(@class, 'review-image-container')]//img[@class='review-image-tile']/@src")
                    if (imagesDom):
                        images = []
                        for imageDom in imagesDom:
                            images.append(self.formatImage(imageDom))
                        if (len(images) > 0):
                            item['images'] = images
                            # print (item['images'])
                except:
                    pass
                # helpful_yes
                try:
                    helpful_yesDom = listDom.xpath("div//span[contains(@class, 'review-votes')]/text()")
                    if (helpful_yesDom):
                        helpful_yes_count = self.formatNumber(helpful_yesDom[0].strip().split(" ")[0], "co.uk")
                        if (helpful_yes_count.isdigit()):
                            item['helpful_yes'] = self.formatNumber(helpful_yesDom[0].strip().split(" ")[0], "co.uk")
                            # print (item['helpful_yes'])
                        elif (helpful_yes_count == "One"):
                            item['helpful_yes'] = "1"
                            # print (item['helpful_yes'])
                except Exception as err:
                    print (err)
                data.append(item)
        if (len(data) > 0):
            return data
        else:
            return False

    def getSummary(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.co.uk"
            sys.exit()
        tree = etree.HTML(html)
        data = {}
        # total_count        # page_count
        try:
            totalReviewCountDom = tree.xpath("//span[contains(@class, 'totalReviewCount')]/text()")
            if (totalReviewCountDom):
                data['count'] = self.formatNumber(totalReviewCountDom[0], "co.uk")
                data['page_count'] = int(self.formatNumber(totalReviewCountDom[0], "co.uk"))/10 + 1
        except:
            pass
        # rating
        try:
            ratingDom = tree.xpath("//i[@data-hook='average-star-rating']/span/text()")
            if (ratingDom):
                data['rating'] = self.formatRating(ratingDom[0], "co.uk")
                # print (data['rating'])
        except:
            pass
        if (len(data) > 0):
            return data
        return False