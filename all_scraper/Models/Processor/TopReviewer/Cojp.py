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
解析函数(主要针对TopReviewwe页)
#############################################################
'''
class Model_Processor_TopReviewer_Cojp(Model_Processor):

    def process(self, html, begin, end):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.co.jp"
            sys.exit()
        tree = etree.HTML(html)
        data = []
        # print (html)
        for i in range(begin, end):
            reviewerDom = tree.xpath("//*[@id='reviewer"+str(i)+"']")
            if (reviewerDom):
                item = {}
                # 抓取rank //*[@id="reviewer1"]/td[1]
                try:
                    rankDom = reviewerDom[0].xpath("td[1]/text()")
                    if (rankDom):
                        item['rank'] = Model_Processor().formatNumber(rankDom[0], "co.jp")
                        # print (item['rank'])
                except Exception as err:
                    print (err)

                # 抓取profile_image_url
                try:
                    imgDom = reviewerDom[0].xpath("td[@class='img']/a/img/@src")
                    if (imgDom):
                        item['profile_image_url'] = Model_Processor().formatImage(imgDom[0])
                        # print (item['profile_image_url'])
                except:
                    pass

                # 抓取id
                try:
                    idDom = reviewerDom[0].xpath("td[3]/a/@href")
                    if (idDom):
                        item['top_reviewer_id'] = idDom[0].split("/")[4].strip()
                        # print (item['id'])
                except Exception as err:
                    print (err)

                # 抓取name
                try:
                    nameDom = reviewerDom[0].xpath("td[3]/a/b/text()")
                    if (nameDom):
                        item['name'] = nameDom[0].strip()
                        # print (item['name'])
                except Exception as err:
                    print (err)

                # 抓取review_count
                try:
                    totalReviewsDom = reviewerDom[0].xpath("td[4]/text()")
                    if (totalReviewsDom):
                        item['review_count'] = Model_Processor().formatNumber(totalReviewsDom[0], "co.jp")
                        # print (item['review_count'])
                except Exception as err:
                    print (err)

                # 抓取helpful_vote_count
                try:
                    helpfulVotesDom = reviewerDom[0].xpath("td[5]/text()")
                    if (helpfulVotesDom):
                        item['helpful_vote_count'] = Model_Processor().formatNumber(helpfulVotesDom[0], "co.jp")
                        # print (item['helpful_vote_count'])
                except Exception as err:
                    print (err)

                # 抓取helpful_vote_ratio
                try:
                    percentHelpfulDom = reviewerDom[0].xpath("td[6]/text()")
                    if (percentHelpfulDom):
                        item['helpful_vote_ratio'] = Model_Processor().formatNumber(percentHelpfulDom[0], "co.jp")
                        # print (item['percent_helpful_vote'])
                except Exception as err:
                    print (err)

                if(len(item) > 0):
                    data.append(item)
            else:
                print ("Pattern Mismatch: Dom [#reviewer"+str(i)+"] not found.")
                continue
        if (len(data) > 0):
            # print (len(data))
            return data

        print ("No available top reviewer data found.")
        return False