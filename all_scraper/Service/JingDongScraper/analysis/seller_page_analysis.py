#-*-coding:utf-8*-
from lxml import etree
import sys
import pytz
import datetime

class seller_page_analysis():
    def process(self, html, url,shop_id):
        if html == '' or html == 'None':
            print ("Can't get them html from http://www.jd.com")
            sys.exit()
        tree = etree.HTML(html)
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        item = {'seller_page_link':url,'seller_id':shop_id,'last_update_time':last_update_time}
        data = []
        # # seller_page_link
        # try:
        #     item['seller_page_link'] = url
        # except Exception as err:
        #     print err
        # seller_name
        try:
            seller_nameDom = tree.xpath("//div[@class='jHeader']/div[@class='jLogo']/em/text()")
            if (seller_nameDom):
                item['seller_name'] = seller_nameDom[0].strip().encode('utf-8')
                # print (item['seller_name'])
        except:
            pass

        # shop_logo_url
        try:
            seller_logDom = tree.xpath("//div[@class='jHeader']/div[@class='jLogo']/img/@src")
            if (seller_logDom):
                item['seller_logo_url'] = "https:" + seller_logDom[0]
                # print (item['seller_logo_url'])
        except:
            pass

        # seller_location 卖家所在地
        try:
            seller_locationDom = tree.xpath("//div[@class='j-shop-info']/p//span[@class='value']/text()")
            if (seller_locationDom):
                item['seller_location'] = seller_locationDom[0].strip().encode('utf-8')
                # print (item['seller_location'])
        except:
            pass

        # score_sum 卖家评分
        try:
            seller_scoreDom = tree.xpath("//div[@class='j-rating-content']/div[@class='j-rating-info']")
            if (seller_scoreDom):
                # 总评分
                try:
                    seller_total = seller_scoreDom[0].xpath("div[contains(@class, 'total-score')]//p[@class='total-score-num']/span/text()")
                    if (seller_total):
                        item['seller_total'] = seller_total[0].strip()
                        # print (item['seller_total'])
                except:
                    pass
                # 180天内店铺动态评分
                try:
                    seller_second = seller_scoreDom[0].xpath("div[@class='j-score'][1]/div[contains(@class, 'item-180')]/span[contains(@class, 'score-180')]/text()")
                    if (seller_second):
                        # 商品质量满意度
                        item['seller_quality'] = seller_second[0]
                        # print (item['seller_quality'])
                        # 服务态度满意度
                        item['seller_attitude'] = seller_second[1]
                        # print (item['seller_attitude'])
                        # 物流速度满意度
                        item['seller_speed'] = seller_second[2]
                        # print (item['seller_speed'])
                        # 商品描述满意度
                        item['seller_discription'] = seller_second[3]
                        # print (item['seller_discription'])
                        # 退换货处理满意度
                        item['seller_return'] = seller_second[4]
                        # print (item['seller_return'])
                except:
                    pass
                # 90天内平台监控店铺服务
                try:
                    seller_third = seller_scoreDom[0].xpath("div[@class='j-score'][2]/div[contains(@class, 'item-90')]/div[contains(@class, 'service-data')]//span[@class='service-des-self']/span[contains(@class, 'value')]/text()")
                    if (seller_third):
                        # 售后处理时长
                        item['seller_processtime'] = seller_third[0]
                        # print (item['seller_processtime'])
                        # 交易纠纷率
                        item['seller_dispute'] = seller_third[1]
                        # print (item['seller_dispute'])
                        # 退换货返修率
                        item['seller_rework'] = seller_third[2]
                        # print (item['seller_rework'])
                except:
                    pass
        except Exception as err:
            print (err)

        # 店铺违法违规信息
        try:
            heguiDom = tree.xpath("//div[contains(@class, 'hegui-info')]/h3//a[1]/text()")
            if (heguiDom):
                item['seller_hegui'] = heguiDom[0].strip().encode('utf-8')
                # print (item['seller_hegui'])
        except:
            pass

        if (len(item) > 0):
            data.append(item)
        if (len(data) > 0):
            return data


