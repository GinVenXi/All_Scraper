#-*-coding:utf-8*-
from lxml import etree
import sys
import pytz
import datetime

#对源码进行解析
class keywords_analysis():
    def process(self, html, page_id,keyword):
        if html == '' or html == 'None':
            print ("Can't get them html from http://www.jd.com.cn/")
            sys.exit()
        tree = etree.HTML(html)
        data = []
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        listDoms = tree.xpath("//*[@id='J_goodsList']/ul/li")
        if (listDoms):
            page_position = 1
            for itemDom in listDoms:
                item = {'page_position': page_position, 'page_id': page_id,'keyword':keyword,'last_update_time':last_update_time}
                page_position += 1
                # sku
                try:
                    skuDom = itemDom.xpath("@data-sku")
                    if (skuDom[0]):
                        # print (skuDom[0])
                        item['sku'] = skuDom[0]
                    else:
                        continue
                except:
                    continue

                # img
                try:
                    imgsDom = itemDom.xpath("div/div[@class='p-img']/a/img")
                    if (imgsDom):
                        for imgDom in imgsDom:
                            try:
                                if (imgDom.xpath("@src")[0] != ""):
                                    # print (imgDom.xpath("@src")[0])
                                    item['image_url'] = imgDom.xpath("@src")[0]
                            except:
                                if (imgDom.xpath("@data-lazy-img")[0] != ""):
                                    # print (imgDom.xpath("@data-lazy-img")[0])
                                    item['image_url'] = imgDom.xpath("@data-lazy-img")[0]
                except:
                    pass

                # price
                try:
                    priceDom = itemDom.xpath("div/div[@class='p-price']/strong/i/text()")
                    if (priceDom):
                        # print (priceDom[0])
                        item['price'] = priceDom[0]
                except:
                    pass

                # title
                try:
                    titleDom = itemDom.xpath("div/div[contains(@class, 'p-name')]/a/@title")
                    if (titleDom):
                        # print (titleDom[0])
                        item['title'] = titleDom[0].encode("utf-8")
                except:
                    pass

                # review_count
                try:
                    review_countDom = itemDom.xpath("div/div[@class='p-commit']/strong/a/text()")
                    if (review_countDom):
                        # print (review_countDom[0])
                        item['review_count'] = review_countDom[0].encode("utf-8")
                except:
                    pass

                # shop
                try:
                    shopDom = itemDom.xpath("div/div[@class='p-shop']/span/a/@title")
                    if (shopDom):
                        # print (shopDom[0])
                        item['shop_name'] = shopDom[0].encode("utf-8")
                    shoplinkDom = itemDom.xpath("div/div[@class='p-shop']/span/a/@href")
                    if (shoplinkDom):
                        # print (shoplinkDom[0])
                        item['shop_link'] = "https:"+shoplinkDom[0]
                        shopid = shoplinkDom[0].split("-")[1].replace(".html", "").strip()
                        # print (shopid)
                        item['shop_id'] = shopid
                except Exception as err:
                    print (err)

                #productpage_url
                try:
                    product_urlDom=itemDom.xpath(".//div//a/@href")
                    if(len(product_urlDom)>0):
                        item['productpage_url']="https:"+product_urlDom[0]
                        # print item['productpage_url']
                except Exception as err:
                    print err
                data.append(item)
        return data

    def getPageCount(self, html):
        pageCount = 1
        if (html == '' or html == None):
            return pageCount
        tree = etree.HTML(html)
        listDom = tree.xpath("//*[@id='J_bottomPage']/span[@class='p-skip']/em[1]/b/text()")
        if (listDom):
            for list in listDom:
                if (list.isdigit()):
                    pageCount = list
                    break
        # else:
        #     listDom = tree.xpath("//*[@id='pagn']//span[@class='pagnLink']/a/text()")
        #     if (listDom):
        #         if (listDom[-1].isdigit()):
        #             pageCount = listDom[-1]
        # print (pageCount)
        return (pageCount)
