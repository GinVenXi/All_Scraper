#-*-coding:utf-8*-
from lxml import etree
import sys
import pytz
import datetime

class products_analysis():
    def process(self, html,product_id):
        if html == '' or html == 'None':
            print "Can't get the html from https://www.taobao.com"
            sys.exit()
        tree = etree.HTML(html)
        data = []
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        item={'last_update_time':last_update_time,'product_id':product_id}

        try:
            Dom = tree.xpath("//*[@id='detail']//div[@id='J_DetailMeta']//div[@class='tm-clear']//div[@class='tb-wrap']")
            # title
            try:
                if(len(Dom)>0):
                    titleDom = Dom[0].xpath(".//div[@class='tb-detail-hd']/h1/a//text()")
                    if (len(titleDom) >0):
                        item['title'] = titleDom[0]
                else:
                    titleDom=tree.xpath("//*[@id='bd']//div[@id='detail']/div[@class='tb-detail-bd tb-clear']/div[@class='tb-summary tb-clear']/div[@class='tb-item-info tb-clear']/div[@class='tb-item-info-r']/div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']/div[@id='J_Title']/h3[@class='tb-main-title']/@data-title")
                    if(len(titleDom)>0):
                        item['title']=titleDom[0]
            except Exception as err:
                print(err)
            # before_price
            # if have no current_price,then before_price is current_price
            try:
                if(len(Dom)>0):
                    before_priceDom = Dom[0].xpath(".//div[@class='tm-fcs-panel']/dl[@id='J_StrPriceModBox']/dd/span[@class='tm-price']/text()")
                    if (len(before_priceDom)>0):
                        item['before_price'] = before_priceDom[0]
                    else:
                        before_priceDom = tree.xpath("//*[@id='detail']//div[@id='J_DetailMeta']/div[@class='tm-clear']/div[@class='tb-property']/div[@class='tb-wrap']/div[@class='tm-fcs-panel']/dl[@class='tm-tagPrice-panel']/dd/span[@class='tm-price']/text()")
                        if (len(before_priceDom)>0):
                            item['before_price'] = before_priceDom[0]
                elif('bwx'):
                    before_priceDom=tree.xpath("//*[@id='bd']//div[@id='detail']/div[@class='tb-detail-bd tb-clear']/div[@class='tb-summary tb-clear']/div[@class='tb-item-info tb-clear']/div[@class='tb-item-info-r']/div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']//li[@id='J_StrPriceModBox']/div[@class='tb-property-cont']/strong[@id='J_StrPrice']/em[@class='tb-rmb-num']/text()")
                    if(len(before_priceDom)>0):
                        item['before_price']=before_priceDom[0]

                elif('cyj'):
                    before_priceDom=Dom[0].xpath(".//div[@class='tm-fcs-panel']//dl[@class='tm-tagPrice-panel']/dd/span[@class='tm-price']/text()")
                    if(len(before_priceDom)>0):
                        item['before_price']=before_priceDom[0]
                elif('lll'):
                    before_priceDom=tree.xpath("//*[@id='J_DetailMeta']/div[1]/div[1]/div/div[2]/dl[1]/dd/span[@lcass='tm-price']/text()")
                    if(len(before_priceDom)>0):
                        item['before_price']=before_priceDom[0]
                else:
                    pass
            except Exception as err:
                print (err)
            # current_price
            try:
                if(len(Dom)>0):
                    current_priceDom = Dom[0].xpath(".//div[@class='tm-fcs-panel']/dl[@id='J_PromoPrice']/dd/div[@class='tm-promo-price']/span[@class='tm-price']/text()")
                    if (len(current_priceDom)>0):
                        item['current_price'] = current_priceDom[0]
                else:
                    current_priceDom=tree.xpath("//*[@id='bd']//div[@id='detail']/div[@class='tb-detail-bd tb-clear']/div[@class='tb-summary tb-clear']/div[@class='tb-item-info tb-clear']/div[@class='tb-item-info-r']/div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']//li[@id='J_PromoPrice']/div[@class='tb-property-cont']/div[@id='J_Promo']/div[@id='J_PromoHd']/div[@class='tb-promo-item-bd']/strong[@class='tb-promo-price']/em[@id='J_PromoPriceNum']/text()")
                    if(len(current_priceDom)>0):
                        item['current_price']=current_priceDom[0]
                    else:
                        pass
            except Exception as err:
                    print(err)
            # shipping
            try:
                if(len(Dom)>0):
                    feeDom = Dom[0].xpath(".//div[@class='tb-meta']//dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/div[@class='tb-postAge-info']/p/em[@class='tm-yen']/text()")
                    if (len(feeDom) > 0):
                        item['shipping'] = feeDom[0]
                    elif ("bwx"):
                        # 第二种
                        feeDom = Dom[0].xpath(".//div[@class='tb-meta']/dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/div[@class='tb-postAge-info']/p/span/text()")
                        if (len(feeDom) > 0):
                            item['shipping'] = feeDom[0]
                            # print item['shipping']
                    elif ("cyj"):
                        # 第三种
                        feeDom = Dom[0].xpath(".//div[@class='tb-meta']//dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/div[@id='J_PostageToggleCont']/p/span/text()")
                        if (len(feeDom) > 0):
                            item['shipping'] = feeDom[0]
                            # print item['shipping']
                    # elif("hhh"):
                    #     #第二种
                    #     feeDom=Dom[0].xpath(".//div[@class='tb-meta']/dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/div[@class='tb-postAge-info']/p/span/text()")
                    #     if (len(feeDom) > 0):
                    #         # print feeDom[0]
                    #         item['fee'] = feeDom[0]
                    #         print item['fee']
                elif('bwx'):
                    # 第二种
                    feeDom = tree.xpath("//*[@id='bd']//div[@id='detail']//div[@class='tb-item-info-r']//div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']/div[@id='J_logistic']/div[@class='tb-logistic tb-clearfix']/div[@id='J_LogisticInfo']/div[@id='J_WlServiceInfo']/span[@class='wl-servicetitle']/text()")
                    if (len(feeDom) > 0):
                        item['shipping'] = feeDom[0]
                        # print item['shipping']

                    # elif('cyj'):
                    #     #第四种
                    #     feeDom=Dom[0].xpath(".//div[@class='tb-meta']//dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/div[@id='J_PostageToggleCont']/p/span/text()")
                    #     if(len(feeDom)>0):
                    #         item['fee']=feeDom[0]
                    #         print item['fee']
                elif('lll'):
                    #第三种
                    feeDom=tree.xpath("//*[@id='J_PostageToggleCont']/p/span/text()")
                    if(len(feeDom)>0):
                        item['shipping']=feeDom[0]
                else:
                    pass
            except Exception as err:
                print err
            # shop_location
            try:
                if(len(Dom)>0):
                    regionDom = Dom[0].xpath(".//div[@class='tb-meta']/dl[@class='tm-delivery-panel']/dd/div[@class='tb-postAge']/span[@class='tb-deliveryAdd']/text()")
                    if (len(regionDom)>0):
                        item['shop_location'] = regionDom[0]
                else:
                    regionDom=tree.xpath("//*[@id='detail']//div[@class='tb-item-info-r']//div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']/div[@id='J_logistic']/div[@class='tb-logistic tb-clearfix']/div[@id='J_LogisticInfo']/div[@class='wl-areainfo clearfix']/span[@id='J_WlAreaInfo']/span[@id='J-From']/text()")
                    if(len(regionDom)>0):
                        item['shop_location']=regionDom[0]
                    else:
                        pass
            except Exception as err:
                print (err)
            # sell_count
            try:
                if(len(Dom)>0):
                    sell_countsDom = Dom[0].xpath(".//ul[@class='tm-ind-panel']/li[@class='tm-ind-item tm-ind-sellCount ']/div[@class='tm-indcon']/span[@class='tm-count']/text()")
                    if (len(sell_countsDom)>0):
                        item['sell_count'] = sell_countsDom[0]
                else:
                    sell_countsDom=tree.xpath("//*[@id='bd']//div[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-summary tb-clear']//div[@class='tb-item-info-r']//div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']//li[@id='J_Counter']/div[@class='tb-counter-bd']/div[@class='tb-sell-counter']/a/strong[@id='J_SellCounter']/text()")
                    if(len(sell_countsDom)>0):
                        item['sell_count']=sell_countsDom[0]
                    else:
                        pass
            except Exception as err:
                print (err)
            # review_count
            try:
                if(len(Dom)>0):
                    tocommentsDom = Dom[0].xpath(".//ul[@class='tm-ind-panel']/li[@class='tm-ind-item tm-ind-reviewCount canClick tm-line3']/div[@class='tm-indcon']/span[@class='tm-count']/text()")
                    if (len(tocommentsDom)>0):
                        # print tocommentsDom[0]
                        item['review_count'] = tocommentsDom[0]
                else:
                    tocommentsDom=tree.xpath("//*[@id='detail']//div[@class='tb-item-info-r']//div[@class='tb-property tb-property-x']/div[@class='tb-wrap tb-wrap-newshop']//li[@id='J_Counter']/div[@class='tb-counter-bd']/div[@class='tb-rate-counter']/a[@id='J_ReviewTabTrigger']/strong[@id='J_RateCounter']/text()")
                    if(len(tocommentsDom)>0):
                        item['review_count']=tocommentsDom[0]
                    else:
                        pass
            except Exception as err:
                print (err)
            # in_stock
            try:
                if (len(Dom) > 0):
                    in_stockDom = Dom[0].xpath(".//div[@class='tb-key']/div[@class='tb-skin']/div[@class='tb-sku']/dl[@class='tb-amount tm-clear']/dd[@id='J_Amount']/em[@id='J_EmStock']/text()")
                    if (len(in_stockDom)>0):
                        item['in_stock'] = in_stockDom[0]
                else:
                    in_stockDom=tree.xpath("//*[@id='detail']//div[@class='tb-item-info-r']//div[@class='tb-wrap tb-wrap-newshop']/div[@id='J_isku']/div[@class='tb-skin']/dl[@class='tb-amount tb-clear']/dd/em/span[@id='J_SpanStock']/text()")
                    if(len(in_stockDom)>0):
                        item['in_stock']=in_stockDom[0]
                    else:
                        pass
            except Exception as err:
                print (err)
            Dom1 = tree.xpath("//*[@id='J_DetailMeta']//div[@class='tb-gallery']")
            # collect_count
            try:
                if (len(Dom1) > 0):
                    collect_countsDom = Dom1[0].xpath(".//p[@class='tm-action tm-clear']/span[@id='J_CollectCount']/text()")
                    if (len(collect_countsDom)>0):
                        item['collect_count'] = collect_countsDom[0].encode("utf-8").replace("（", "").replace("人气）", "").strip()
                        # print item['collect_count']
                else:
                    collect_countsDom=tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-summary tb-clear']//div[@class='tb-item-info tb-clear']//div[@class='tb-item-info-l']//div[@id='J_Social']/ul/li[@class='tb-social-fav']/a[@class='J_TDialogTrigger']/em[@class='J_FavCount']/text()")
                    if(len(collect_countsDom)>0):
                        item['collect_count']=collect_countsDom[0].encode("utf-8").replace("（", "").replace("人气）", "").strip()
                        # print item['collect_count']
                    else:
                        pass
            except Exception as err:
                print (err)

            Dom2 = tree.xpath("//*[@id='header']//div[@id='shop-info']//div[@class='main-info']")
            # discription,service,logistics
            # discription
            try:
                if(len(Dom2)>0):
                    #第一种
                    # discriptionDom = Dom2[0].xpath(".//div[@class='shopdsr-item']/div[@class='shopdsr-score shopdsr-score-down-ctrl']/span[@class='shopdsr-score-con']/text()")
                    #//*[@id="shop-info"]/div[2]/div[1]/div[2]/span
                    discriptionDom=tree.xpath("//*[@id='shop-info']/div[2]/div[1]/div[2]/span[@class='shopdsr-score-con']/text()")
                    # print discriptionDom
                    if (len(discriptionDom)>0):
                        # print discriptionDom[0]
                        item['discription'] = discriptionDom[0]
                        # print item['discription']

                elif('hhh'):
                    discriptionDom = tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-bd']/div[@class='tb-shop-rate']/dl/dd/a/text()")
                    if (len(discriptionDom) > 0):
                        # print discriptionDom[0]
                        item['discription'] = discriptionDom[0]
                        # item['service']=discriptionDom[1]
                        # item['logistics']=discriptionDom[2]
                        # print item['discription']
                        # print item['service']
                        # print item['logistics']


                elif('ttt'):
                        discriptionDom = tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-service-info']/ul[@class='shop-service-info-list']/li[@class='shop-service-info-item']/span[@class='rateinfo']/em/text()")
                        if (len(discriptionDom) > 0):
                            # print discriptionDom[0]
                            item['discription'] = discriptionDom[0]
                            # item['service']=discriptionDom[1]
                            # item['logistics']=discriptionDom[2]
                            # print item['discription']
                            # print item['service']
                            # print item['logistics']
                elif('lll'):
                    discriptionDom=tree.xpath("//*[@id='shop-info']/div[2]/div[1]/div[2]/span[@class='shopdsr-score-con']/text()")
                    if(len(discriptionDom)>0):
                        item['discription']=discriptionDom[0]
                        # item['service']=discriptionDom[1]
                        # item['logistics']=discriptionDom[2]
                        # print item['discription']
                        # print item['service']
                        # print item['logistics']
                else:
                    pass
            except Exception as err:
                print (err)
            # service
            try:
                if(len(Dom2)>0):
                    #第一种
                    # serviceDom = Dom2[0].xpath(".//div[@class='shopdsr-item']/div[@class='shopdsr-score shopdsr-score-down-ctrl']/span[@class='shopdsr-score-con']/text()")
                    serviceDom=tree.xpath("//*[@id='shop-info']/div[2]/div[2]/div[2]/span[@class='shopdsr-score-con']/text()")
                    if (len(serviceDom)>0):
                        # print serviceDom[1]
                        item['service'] = serviceDom[0]
                        # print item['service']
                elif('hhh'):
                    #第二种
                    serviceDom=tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-bd']/div[@class='tb-shop-rate']/dl/dd/a/text()")
                    if(len(serviceDom)>0):
                        # print serviceDom[1]
                        item['service']=serviceDom[1]
                        # print item['service']
                elif('bwx'):
                    #第三种
                    serviceDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-service-info']/ul[@class='shop-service-info-list']/li[@class='shop-service-info-item']/span[@class='rateinfo']/em/text()")
                    if(len(serviceDom)>0):
                        # print serviceDom[1]
                        item['service']=serviceDom[1]
                        # print item['service']
                elif('cyj'):
                    serviceDom=tree.xpath("//*[@id='shop-info']/div[2]/div[2]/div[2]/span[@class='shopdsr-score-con']/text()")
                    if(len(serviceDom)>0):
                        item['service']=serviceDom[0]
                        # print item['service']
                else:
                    pass

            except Exception as err:
                print (err)
            # logistics
            try:
                if (len(Dom2) > 0):
                    # logisticsDom = Dom2[0].xpath(".//div[@class='shopdsr-item']/div[@class='shopdsr-score shopdsr-score-down-ctrl']/span[@class='shopdsr-score-con']/text()")
                    logisticsDom=tree.xpath("//*[@id='shop-info']/div[2]/div[3]/div[2]/span[@class='shopdsr-score-con']/text()")
                    if (len(logisticsDom)>0):
                        # print logisticsDom[2]
                        item['logistics'] = logisticsDom[0]
                        # print item['logistics']
                elif('hhh'):
                    #第二种
                    logisticsDom=tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-bd']/div[@class='tb-shop-rate']/dl/dd/a/text()")
                    if(len(logisticsDom)>0):
                        # print logisticsDom[2]
                        item['logistics']=logisticsDom[2]
                        # print item['logistics']
                elif('lll'):
                    #第三种
                    logisticsDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-service-info']/ul[@class='shop-service-info-list']/li[@class='shop-service-info-item']/span[@class='rateinfo']/em/text()")
                    if(len(logisticsDom)>0):
                        # print logisticsDom[2]
                        item['logistics']=logisticsDom[2]
                        # print item['logistics']
                elif('bwx'):
                    #第四种
                    logisticsDom=tree.xpath("//*[@id='shop-info']/div[2]/div[3]/div[2]/span[@class='shopdsr-score-con']/text()")
                    if(len(logisticsDom)>0):
                        item['logistics']=logisticsDom[0]
                        # print item['logistics']
                else:
                    pass
            except Exception as err:
                print (err)

            Dom3 = tree.xpath("//*[@id='header']//div[@id='headerCon']//div[@id='shopExtra']")
            # shop_name,shop_link
            # seller_nickname
            try:
                if (len(Dom3) > 0):
                    nicknameDom = Dom3[0].xpath(".//div[@class='slogo']//a[@class='slogo-shopname']/strong/text()")
                    if (len(nicknameDom)>0):
                        # print nicknameDom[0]
                        item['shop_name'] = nicknameDom[0]
                        # print item['shop_name']
                elif('bwx'):
                    #第二种
                    nicknameDom=tree.xpath("//*[@id='bd']//div[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-hd']/div[@class='tb-shop-seller']/dl/dd/a/text()")
                    # print ("###############################################")
                    # print nicknameDom
                    if(len(nicknameDom)>0):
                        # print nicknameDom[0]
                        item['shop_name']=nicknameDom[0]
                        # print item['shop_name']
                elif('cyj'):
                        #第三种
                        nicknameDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-name']/div[@class='shop-name-wrap']/a[@class='shop-name-link']/text()")
                        if(len(nicknameDom)>0):
                            # print nicknameDom[0]
                            item['shop_name']=nicknameDom[0]
                            # print item['shop_name']
                elif('hhh'):
                        #第四种
                        nicknameDom=tree.xpath("//*[id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']/div[@class='summary-popup J_TSummaryPopup']/div[@class='more-info']/div[@class='shop-more-info']//p[@class='info-item']/text()")
                        if(len(nicknameDom)>0):
                            item['shop_name']=nicknameDom[0]
                            # print item['shop_name']
                        else:
                            nicknameDom=tree.xpath("//*[id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']/div[@class='summary-popup J_TSummaryPopup']/div[@class='more-info']/div[@class='shop-more-info']//p[@class='info-item']/span/@data-tnick")
                            if(len(nicknameDom)>0):
                                item['shop_name']=nicknameDom[0]
                                # print item['shop_name']
                            else:
                                pass
                elif('hhhh'):
                        #第五种
                        nicknameDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-name']/div[@class='shop-name-wrap']/a[@class='shop-name-link']/text()")
                        if(len(nicknameDom)>0):
                            item['shop_name']=nicknameDom[0]
                            # print item['shop_name']
                        else:
                            pass
                else:
                    pass
            except Exception as err:
                    print err

            # shop_link(此处的店家链接需要拼接url组成)
            try:
                if (len(Dom3) > 0):
                    shopLinkDom1 = Dom3[0].xpath(".//div[@class='slogo']//a/@href")
                    shopLinkDom2 = Dom3[0].xpath(".//div[@class='slogo']//a/@data-spm")
                    if(len(shopLinkDom1[0])>0):
                        item['shop_link'] = 'https:' + shopLinkDom1[0] + '?spm=' + shopLinkDom2[0]
                        # print item['shop_link']
                elif('hhh'):
                    #第二种
                    shopLinkDom=tree.xpath("//*[@id='bd']//div[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-hd']/div[@class='tb-shop-name']/dl/dd/strong/a/@href")
                    if(len(shopLinkDom)>0):
                        # print shopLinkDom[0]
                        item['shop_link']="https:"+shopLinkDom[0]
                        # print item['shop_link']
                elif('bwx'):
                    #第三种
                    shopLinkDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-name']/div[@class='shop-name-wrap']/a[@class='shop-name-link']/@href")
                    # print shopLinkDom
                    if(len(shopLinkDom)>0):
                        # print shopLinkDom[0]
                        item['shop_link']="https:"+shopLinkDom[0]
                        print item['shop_link']
                elif('cyj'):
                    #第四种
                    shopLinkDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-name']/div[@class='shop-name-wrap']/a/@href")
                    if(len(shopLinkDom)>0):
                        item['shop_link']="https:"+shopLinkDom[0]
                        # print item['shop_link']
                    else:
                        pass
                elif('hhhhh'):
                    #第五种
                    shopLinkDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='shop-name']/div[@class='shop-name-wrap']/a/@href")
                    if(len(shopLinkDom)>0):
                        item['shop_link']="https:"+shopLinkDom[0]
                        # print item['shop_link']
                    else:
                        pass
                else:
                    pass

            except Exception as err:
                print (err)
                pass

            Dom4 = tree.xpath("//*[@id='J_DetailMeta']//div[@class='tm-clear']")
            # image_url
            try:
                if (len(Dom4) > 0):
                    pic_urlDom = Dom4[0].xpath("//ul[@id='J_UlThumb']/li/a/img/@src")
                    if(len(pic_urlDom)>0):
                        images=[]
                        for image in pic_urlDom:
                            images.append(image)
                        if(len(images)>0):
                            item['image_url']=images
                else:
                    pic_urlDom=tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-summary tb-clear']//div[@class='tb-item-info tb-clear']//div[@class='tb-item-info-l']//div[@class='tb-gallery']/ul[@id='J_UlThumb']/li/div[@class='tb-pic tb-s50']/a/img/@data-src")
                    if(len(pic_urlDom)>0):

                        images=[]
                        for image in pic_urlDom:
                            images.append(image)
                        if(len(images)>0):
                            item['image_url']=images
                    else:
                        pass
            except Exception as err:
                print (err)

            # Dom5 =tree.xpath("//*[@id='bd']//div[@class='grid-s5m0 tm-clear']//div[@class='col-sub']//div[@id='J_DcShopArchive']")
            # #shopRateLink
            # try:
            #     if (len(Dom5) > 0):
            #         # // *[ @ id = "side-shop-info"] / div / div[2] / div[1]
            #         shopRateLinkDom = Dom5[0].xpath(".//div[@id='side-shop-info']//div[@class='shop-intro']//div[@class='main-info']//div[1]/div[@class='shopdsr-score shopdsr-score-up-ctrl']/span[@class='shopdsr-score-con']/text()")
            #         if(len(shopRateLinkDom)>0):
            #             # print shopRateLinkDom[0]
            #             item['shopRateLink'] = "https:"+shopRateLinkDom[0]
            #             print item['shopRateLink']
            #     elif("hhh"):
            #         #第二种
            #         shopRateLinkDom=tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-bd']/div[@class='tb-shop-rate']/dl/dd[@class='tb-rate-lower']/a/@href")
            #         if(len(shopRateLinkDom)>0):
            #             # print shopRateLinkDom[0]
            #             item['shopRateLink']="https:"+shopRateLinkDom[0]
            #             print item['shopRateLink']
            #     elif('bwx'):
            #         #第三种
            #         shopRateLinkDom=tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='summary-popup J_TSummaryPopup']/div[@class='more-info']/div[@class='shop-dynamic-score']/ul/li/a/@href")
            #         if(len(shopRateLinkDom)>0):
            #             print shopRateLinkDom[0]
            #             item['shopRateLink']=shopRateLinkDom[0]
            #             print item['shopRateLink']
            #     elif('cyj'):
            #         #第四种
            #         shopRateLinkDom=tree.xpath("//*[@id='header']//div[@id='headerCon']//div[@id='shopExtra']//div[@id='shop-info']//div[@class='extra-info ks-popup-hidden ks-overlay-hidden']/div[@class='ks-popup-content']//div[@class='bd']/div[@class='shop-rate']/ul[@class='render-byjs']/li/a/@href")
            #         print shopRateLinkDom
            #         # shopRateLinkDom=tree.xpath("//*[@id='ks-component2234']/div/div/div/div[1]/ul/li[1]/a[@href]")
            #
            #         if(len(shopRateLinkDom)>0):
            #             item['shopRateLink']="https:"+shopRateLinkDom[0]
            #             print item['shopRateLink']
            #     else:
            #         pass
            Dom5=tree.xpath(".//*[@id='header']//div[@id='headerCon']//div[@id='shopExtra']//div[@id='shop-info']//div[3]/div[@class='ks-popup-content']")
            # print Dom5
            #sellerpage_url
            try:
                if(len(Dom5)>0):
                    #第一种
                    shopRateLinkDom=Dom5[0].xpath(".//div[@class='bd']//div[@class='shop-rate']/ul[@class='render-byjs']/li[1]/a/@href")
                    if(len(shopRateLinkDom)>0):
                        item['sellerpage_url']="https:"+shopRateLinkDom[0]
                        # print item['sellerpage_url']
                elif ("hhh"):
                    # 第二种
                    shopRateLinkDom = tree.xpath("//*[@id='detail']//div[@class='tb-detail-bd tb-clear']//div[@class='tb-sidebar tb-clear']//div[@id='J_ShopInfo']/div[@class='tb-shop-info-wrap']/div[@class='tb-shop-info-bd']/div[@class='tb-shop-rate']/dl/dd/a/@href")
                    if (len(shopRateLinkDom) > 0):
                        # print shopRateLinkDom[0]
                        item['sellerpage_url'] = "https:" + shopRateLinkDom[0]
                        # print item['sellerpage_url']
                elif ('bwx'):
                    # 第三种
                    shopRateLinkDom = tree.xpath("//*[@id='J_Header']//div[@id='header']//div[@id='header-content']//div[@class='shop-summary J_TShopSummary']//div[@class='summary-popup J_TSummaryPopup']/div[@class='more-info']/div[@class='shop-dynamic-score']/ul/li/a/@href")
                    if (len(shopRateLinkDom) > 0):
                        # print shopRateLinkDom[0]
                        item['sellerpage_url'] = "https:"+shopRateLinkDom[0]
                        # print item['sellerpage_url']
                else:
                    pass
            except Exception as err:
                print err
            if (len(item) > 0):
                data.append(item)
            if (len(data) > 0):
                return data

        except Exception as err:
            print err
