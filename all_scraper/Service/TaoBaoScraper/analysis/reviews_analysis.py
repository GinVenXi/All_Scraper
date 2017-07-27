#-*-coding:utf-8*-
from lxml import etree
import sys
import pytz
import datetime

#评论页解析json数据
class reviews_analysis():
    def process(self,text,url):
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        if text == '' or text == 'None':
            print "Can't get the html from taobao_review"
            sys.exit()

        data = []
        item = {}
        for i in range(len(text['rateList'])):
            item={}
            item['review_json_link']=url
            item['last_update_time']=last_update_time
            # 总评价数量
            try:
                # print text['rateCount']['total']
                item['review_count'] = text['rateCount']['total']
            except Exception as err:
                print err
            # 带有图片的评论数量
            try:
                # print text['rateCount']['picNum']
                item['image_count'] = text['rateCount']['picNum']
            except Exception as err:
                print err
            try:
                # 评论
                # print text['rateList'][i]['rateContent']
                item['review_content'] = text['rateList'][i]['rateContent']
            except Exception as err:
                print err
            try:
                # 评论时间
                # print text['rateList'][i]['rateDate']
                item['review_time'] = text['rateList'][i]['rateDate']
            except Exception as err:
                print err
            try:
                # 购买产品类型相关
                # print text['rateList'][i]['auctionSku']
                item['product_information'] = text['rateList'][i]['auctionSku']
            except Exception as err:
                print err

            try:
                # 评价人名称
                # print text['rateList'][i]['displayUserNick']
                item['reviewer_name'] = text['rateList'][i]['displayUserNick']
            except Exception as err:
                print err

            try:
                # 评价人id
                # print text['rateList'][i]['id']
                item['reviewer_id'] = text['rateList'][i]['id']
            except Exception as err:
                print err
            try:
                # 评论中图片url
                # print text['rateList'][i]['pics']
                item['image_url'] = text['rateList'][i]['pics']
            except Exception as err:
                print err

            try:
                # 卖家id
                # print text['rateList'][i]['sellerId']
                item['seller_id'] = text['rateList'][i]['sellerId']
            except Exception as err:
                print err
            if (len(item) > 0):
                data.append(item)

        if (len(data) > 0):
            # print ("##################################################################################################################################################################################")
            # print data
            # return data[0]
            # print (len(data))
            return data
            # print data
