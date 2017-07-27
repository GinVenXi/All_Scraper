#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import sys
from lxml import etree
from Models.processor import Model_Processor

class Model_Processor_Seller_Base_Es(Model_Processor):
    def __init__(self):
        pass

    def process(self, html):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.amazon.es"
            sys.exit()
        tree = etree.HTML(html)
        data = {}

        # sellerLogo 卖家标志 //*[@id="sellerLogo"]
        try:
            logoDom = tree.xpath("//*[@id='sellerLogo']/@src")
            # print (logoDom)
            if (logoDom):
                data['logo_url'] = logoDom[0]
        except:
            print ("sellerLogo error")

        # sellerName 卖家名字
        try:
            nameDom = tree.xpath("//*[@id='sellerName']/text()")
            if (nameDom):
                data['name'] = nameDom[0].strip()
        except:
            print ("sellerName error")

        # rating 卖家评级
        try:
            ratingDom = tree.xpath("//*[@id='seller-feedback-summary']//*[@class='a-icon-alt']/text()")
            if (ratingDom):
                data['rating'] = Model_Processor().formatRating(ratingDom[0], "es")
        except:
            print ("seller rating error")


        try:
            feedbackDom = tree.xpath("//*[@id='feedback-summary-table']//tr")
            if (feedbackDom):
                # print (feedbackDom)
                for itemDom in feedbackDom:
                    # print (itemDom.xpath("td[1]/text()"))
                    typeDom = itemDom.xpath("td[1]/text()")
                    if (typeDom):
                        type = Model_Processor().formatType(typeDom[0].strip()).lower()
                        # print (type)
                        # feedback type thirty_days
                        thirtyDaysDom = itemDom.xpath("td[2]/span/text()")
                        if (thirtyDaysDom):
                            # print (thirtyDaysDom[0].strip())
                            if (thirtyDaysDom[0].strip() != '-'):
                                thirtyDaysDom = Model_Processor().formatNumber(thirtyDaysDom[0].strip(), "es")
                                data['feedback_'+type+'_thirty_days'] = thirtyDaysDom
                            else:
                                data['feedback_'+type+'_thirty_days'] = ""
                        # feedback type ninty_days
                        nintyDaysDom = itemDom.xpath("td[3]/span/text()")
                        if (nintyDaysDom):
                            # print (nintyDaysDom[0].strip())
                            if (nintyDaysDom[0].strip() != '-'):
                                nintyDaysDom = Model_Processor().formatNumber(nintyDaysDom[0].strip(), "es")
                                data['feedback_'+type+'_ninty_days'] = nintyDaysDom
                            else:
                                data['feedback_'+type+'_ninty_days'] = ""
                        # feedback type twelve_months
                        twelveMonthsDom = itemDom.xpath("td[4]/span/text()")
                        if (twelveMonthsDom):
                            # print (twelveMonthsDom[0].strip())
                            if (twelveMonthsDom[0].strip() != '-'):
                                twelveMonthsDom = Model_Processor().formatNumber(twelveMonthsDom[0].strip(), "es")
                                data['feedback_'+type+'_twelve_months'] = twelveMonthsDom
                            else:
                                data['feedback_'+type+'_twelve_months'] = ""
                        # feedback type lifetime
                        lifetimeDom = itemDom.xpath("td[5]/span/text()")
                        if (lifetimeDom):
                            # print (lifetimeDom[0].strip())
                            if (lifetimeDom[0].strip() != '-'):
                                lifetimeDom = Model_Processor().formatNumber(lifetimeDom[0].strip(), "es")
                                data['feedback_'+type+'_lifetime'] = lifetimeDom
                            else:
                                data['feedback_'+type+'_lifetime'] = ""
            else:
                print ("no feedback")
        except:
            print ("feedback info error")

        if (len(data)):
            return data

        return False