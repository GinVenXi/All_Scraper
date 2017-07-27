#-*-coding:utf-8*-
from lxml import etree
import pytz
import datetime

class keywords_analysis():

    def process(self, html,page_id,keyword):
        if html == '' or html == 'None':
            print "Can't get them html from https://www.taobao.com"
        tree = etree.HTML(html)
        data = []
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        try:
            Dom = tree.xpath("//*[@id='mainsrp-itemlist']//div[@class='items']//div[contains(@class, 'item')]")
            page_position = 1
            # page_id =1
            for dom in Dom:
                item = {'page_position':page_position,'page_id':page_id,'keyword':keyword,'last_update_time':last_update_time}
                page_position+=1
                try:
                    titleDom = dom.xpath(".//div[contains(@class, 'ctx-box')]/div[contains(@class, 'title')]/a/text()")
                    if len(titleDom) == 0 or len(titleDom) == 1:
                        pass
                    elif len(titleDom) == 2:
                        title1 = titleDom[1].titleDom[1].replace("\n", "").strip()
                        titlesum = title1.strip()
                        pass
                    elif len(titleDom) == 3:
                        title1 = titleDom[1].replace("\n", "").strip()
                        title2 = titleDom[2].replace("\n", "").strip()
                        titlesum = title1 + " " + title2
                        pass
                    elif len(titleDom) == 4:
                        title1 = titleDom[1].replace("\n", "").strip()
                        title2 = titleDom[2].replace("\n", "").strip()
                        title3 = titleDom[3].replace("\n", "").strip()
                        titlesum = title1 + " " + title2 + " " + title3
                        pass
                    elif len(titleDom) == 5:
                        title1 = titleDom[1].replace("\n", "").strip()
                        title2 = titleDom[2].replace("\n", "").strip()
                        title3 = titleDom[3].replace("\n", "").strip()
                        title4 = titleDom[4].replace("\n", "").strip()
                        titlesum = title1 + " " + title2 + " " + title3 + " " + title4
                        pass
                    item['title'] = titlesum

                except:
                    pass
                # price
                try:
                    # price
                    priceDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-1 g-clearfix')]/div[contains(@class,'price')]/strong/text()")
                    item['current_price'] = priceDom[0]
                except Exception as err:
                    print err
                # shipping
                try:
                    feeDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-1 g-clearfix')]/div[contains(@class,'icon-service-free')]")
                    if (feeDom != ""):
                        item['shipping'] = '0'
                except:
                    item['shipping'] = '1'
                    pass
                #sell_count
                try:
                    # sell_count
                    sellDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-1 g-clearfix')]/div[contains(@class,'deal-cnt')]/text()")
                    item['sell_count'] = sellDom[0]
                except Exception as err:
                    print err
                # shop_name
                try:
                    # shop_name
                    nickDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-3 g-clearfix')]/div[contains(@class,'shop')]/a[contains(@class,'J_ShopInfo')]/span[2]/text()")
                    item['shop_name'] = nickDom[0]
                except Exception as err:
                    print err
                #shop_location
                try:
                    # shop_location
                    locDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-3 g-clearfix')]/div[contains(@class,'location')]/text()")
                    if (locDom[0] != ""):
                        item['shop_location'] = locDom[0]
                except Exception as err:
                    print err

                # shop_link
                try:
                    # shop_link
                    linkDom = dom.xpath( ".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-3 g-clearfix')]/div[contains(@class,'shop')]/a[contains(@class,'J_ShopInfo')]/@href")
                    item['shop_link'] = "https:" + linkDom[0]
                except Exception as err:
                    print err
                #seller_id
                try:
                    # seller_id
                    userIdDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-3 g-clearfix')]/div[contains(@class,'shop')]/a[contains(@class,'J_ShopInfo')]/@data-userid")
                    item['seller_id'] = userIdDom[0]
                except Exception as err:
                    print err
                #product_id
                try:
                    itemIdDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-3 g-clearfix')]/div[contains(@class,'shop')]/a[contains(@class,'J_ShopInfo')]/@data-nid")
                    item['product_id'] = itemIdDom[0]
                except:
                    pass
                # productpage_url
                try:
                    # productpage_url(供给product使用的url)
                    nidDom = dom.xpath(".//div[contains(@class,'ctx-box')]/div[contains(@class,'row-2 title')]/a[contains(@class,'J_ClickStat')]/@href")
                    item['productpage_url'] = "https:" + nidDom[0]
                except Exception as err:
                    print err
                if (len(item)>0):
                        data.append(item)
            if (len(data)>0):
                return data
        except Exception as err:
           print err