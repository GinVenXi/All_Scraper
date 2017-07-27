#-*-coding:utf-8*-
import sys

class reviews_analysis():
    def process(self, text, url):
        if text == '' or text == 'None':
            print "Can't get the html from JD"
            sys.exit()
        data = []
        for i in range(len(text['comments'])):
            item={}
            #review_json_link
            try:
                item['review_json_link']=url
                # print item['review_json_link']
            except Exception as err:
                print err
            #goodrate
            try:
                item['goodrate']=text['productCommentSummary']['goodRateShow']
                # print item['goodrate']
            except Exception as err:
                print err
            #poor_count
            try:
                item['poor_count']=text['productCommentSummary']['poorCountStr']
                # print item['poor_count']
            except Exception as err:
                print err
            #general_count
            try:
                item['general_count']=text['productCommentSummary']['generalCountStr']
                # print item['general_count']
            except Exception as err:
                print err
            #good_count
            try:
                item['good_count']=text['productCommentSummary']['goodCountStr']
                # print item['good_count']
            except Exception as err:
                print err
            #review_count
            try:
                item['review_count']=text['productCommentSummary']['commentCountStr']
                # print item['review_count']
            except Exception as err:
                print err
            #product_id
            try:
                item['product_id']=text['productCommentSummary']['productId']
                # print item['product_id']
            except Exception as err:
                print err
            # reviewer_id　
            try:
                item['reviewer_id']=text['comments'][i]['id']
                # print item['reviewer_id']
            except Exception as err:
                print err
            #review_content
            try:
                item['review_content']=text['comments'][i]['content']
                # print item['review_content']
            except Exception as err:
                print err
            #review_time
            try:
                item['review_time']=text['comments'][i]['creationTime']
                # print item['review_time']
            except Exception as err:
                print err
            #product_information
            try:
                item['product_information']=text['comments'][i]['referenceName']
                # print item['product_information']
            except Exception as err:
                print err
            # #referenceTime
            # try:
            #     item['referenceTime']=text['comments'][i]['referenceTime']
            #     print item['referenceTime']
            # except Exception as err:
            #     print err
            #reviewer_name
            try:
                item['reviewer_name']=text['comments'][i]['nickname']
                # print item['reviewer_name']
            except Exception as err:
                print err
            # #imgUrl
            # try:
            #     item_imgurl={}
            #     temp = ""
            #     for img_t in range(len(text['comments'][i]['images'])):
            #         item_img="https:"+text['comments'][i]['images'][img_t]['imgUrl']
            #         temp=temp+item_img+","
            #     item['imgUrl']=temp
            #     print item['imgUrl']

                    # temp=""
                    # for img in item_img:
                    #     # temp=""
                    #     img=temp+img+","
                    # item['imgUrl']=temp
                    # print item['imgUrl']
            # except Exception as err:
            #     print err
            if(len(item)>0):
                data.append(item)
        if(len(data)>0):
            return data