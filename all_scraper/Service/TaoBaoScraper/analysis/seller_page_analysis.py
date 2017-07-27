#-*-coding:utf-8*-
from lxml import etree
import pytz
import datetime


#ratepage解析页面
class seller_page_analysis():
    def process(self, html,url):
        if html == '' or html == 'None':
            print "Can't get the html from https://www.taobao.com"
        tree = etree.HTML(html)
        data = []
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        item = {'last_update_time':last_update_time,'seller_page_link':url}

        try:
            #seller_page_link
            item['seller_page_link']=url
            Dom = tree.xpath("//*[@id='shop-rate-box']//div//div[@class='col-sub']//div[@class='left-box']")
            #seller_name
            try:
                if(len(Dom)>0):
                    nicknameDom=Dom[0].xpath(".//div[@class='bd']//div//div[@class='title']/span/@data-nick")
                    if(len(nicknameDom)>0):
                        item['seller_name']=nicknameDom[0]
                        print item['seller_name']
            except Exception as err:
                print err
            #seller_loacation
            try:
                #region
                if(len(Dom)>0):
                    #//*[@id="shop-rate-box"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li[2]
                    regionDom=Dom[0].xpath(".//div[@class='bd']//div//ul/li[2]/text()")
                    if(len(regionDom)>0):
                        item['seller_location']=regionDom[0]
                        print item['seller_location']
            except Exception as err:
                print err
            #seller_credit
            try:
                #credit
                if(len(Dom)>0):
                    creditDom=Dom[0].xpath(".//div[@class='bd']//div[2]//ul//li[1]//text()")
                    if(len(creditDom)>0):
                        item['seller_credit']=creditDom[0]
                        print item['seller_credit']
            except Exception as err:
                print err

            Dom1=tree.xpath("//*[@class='rate-box box-shadow']//div[@class='bd bd-v3']")
            #seller_conform
            try:
                #conform
                if(len(Dom1)>0):
                    conformDom=Dom1[0].xpath(".//ul[@class='dsr-info']//li[1]//div[1]//em[@class='count']/text()")
                    if(len(conformDom)>0):
                        item['seller_conform']=conformDom[0]
                        print item['seller_conform']
            except Exception as err:
                print err
            #seller_service
            try:
                #service
                if(len(Dom1)>0):
                    serviceDom=Dom1[0].xpath(".//ul[@class='dsr-info']//li[2]//div[1]//em[@class='count']/text()")
                    if(len(serviceDom)>0):
                        item['seller_service']=serviceDom[0]
                        print item['seller_service']
            except Exception as err:
                print err
            #seller_logistics
            try:
                if(len(Dom1)>0):
                    logisticsDom=Dom1[0].xpath(".//ul[@class='dsr-info']//li[3]//div[1]/em[@class='count']/text()")
                    if(len(logisticsDom)>0):
                        item['seller_logistics']=logisticsDom[0]
                        print item['seller_logistics']
            except Exception as err:
                print err
            #review_count
            try:
                if(len(Dom1)>0):
                    reviewer_countDOm=Dom1[0].xpath(".//ul[@class='dsr-info']//li[1]//div[2]//div[@class='total']//span[2]/text()")
                    if(len(reviewer_countDOm)>0):
                        item['review_count']=reviewer_countDOm[0]
                        print item['review_count']
            except Exception as err:
                print err
            #//*[@id="shop-rate-box"]/div[1]/div[1]/div/div[3]/div[1]/div[1]/h4/em
            Dom2=tree.xpath("//*[@id='shop-rate-box']/div[1]/div[1]/div[@class='main-wrap']//div[@class='box-shadow-combo']")
            #favorable_rate
            try:
                if(len(Dom2)>0):
                    favorable_rateDom=Dom2[0].xpath(".//div[@class='rate-box box-his-rate']//div[@class='hd']//h4/em/text()")
                    if (len(favorable_rateDom)>0):
                        item['favorable_rate']=favorable_rateDom[0]
                        print item['favorable_rate']
            except Exception as err:
                print err

            Dom3=tree.xpath("//*[@id='shop-rate-box']//div[1]//div[@class='personal-rating col-main']//div[@class='main-wrap']")
            #csspeed
            try:
                if(len(Dom3)>0):
                    csspeedDom=Dom3[0].xpath(".//div[@class='tb-rate-shop-month']//div[2]//div[1]//div[@class='title']/em/text()")
                    if(len(csspeedDom)>0):
                        item['csspeed']=csspeedDom[0]
                        print item['csspeed']
            except Exception as err:
                print err
            #csrate
            try:
                if(len(Dom3)>0):
                    csrateDom=Dom3[0].xpath(".//div[@class='tb-rate-shop-month']//div[2]//div[2]//div[@class='title']/em/text()")
                    if(len(csrateDom)>0):
                        item['csrate']=csrateDom[0]
                        print item['csrate']
            except Exception as err:
                print err
            #dispute_rate
            try:
                if(len(Dom3)>0):
                    disputerateDom=Dom3[0].xpath(".//div[@class='tb-rate-shop-month']//div[2]//div[3]//div[@class='title']/em/text()")
                    if(len(disputerateDom)>0):
                        item['dispute_rate']=disputerateDom[0]
                        print item['dispute_rate']
            except Exception as err:
                print err
            #penaltynum
            try:
                if(len(Dom3)>0):
                    penaltynumDom=Dom3[0].xpath(".//div[@class='tb-rate-shop-month']//div[2]//div[4]//div[@class='title']/em/text()")
                    if(len(penaltynumDom)>0):
                        item['penalty_num']=penaltynumDom[0]
                        print item['penalty_num']
            except Exception as err:
                print err
            if(len(item)>0):
                data.append(item)
            if(len(data)>0):
                return data
        except Exception  as err:
            print err
