#-*-coding:utf-8*-
from lxml import etree
import sys
import pytz
import datetime

class products_analysis():
    def process(self, html,sku):
        if html == '' or html == 'None':
            print ("Can't get them html from http://www.jd.com")
            sys.exit()
        tree = etree.HTML(html)
        tz = pytz.timezone('Asia/Shanghai')
        last_update_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        item = {'last_update_time':last_update_time,'sku':sku}
        data = []
        # price
        try:
            priceDom = tree.xpath("//div[contains(@class, 'summary-price')]//span[@class='p-price']/span[contains(@class, 'price')]/text()")
            if (priceDom):
                # print (priceDom[0])
                item['price'] = priceDom[0]
        except:
            pass

        # shipping
        try:
            shippingDom = tree.xpath("//div[contains(@class, 'J-dcashDesc')]/text()")
            if (shippingDom):
                item['shipping'] = shippingDom[0].strip().encode('utf-8')
                # print (item['shipping'])
            else:
                shippingDom=tree.xpath("//*[@class='line1 clearfix']/a/text()")
                if(shippingDom):
                    item['shipping']=shippingDom[0].encode("utf-8").replace("\n","")
        except:
            pass

        # img
        try:
            imgsDom = tree.xpath("//div[@id='spec-list']/ul/li/img")
            if (imgsDom):
                images = []
                for imgDom in imgsDom:
                    try:
                        if (imgDom.xpath("@src")[0] != ""):
                            images.append(imgDom.xpath("@src")[0])
                    except:
                        if (imgDom.xpath("@data-lazy-img")[0] != ""):
                            images.append(imgDom.xpath("@data-lazy-img")[0])
                if (len(images) > 0):
                    item['image_url'] =images
                print (item['image_url'])
        except:
            pass

        # title
        try:
            titleDom = tree.xpath("//div[@class='sku-name']/text()")
            if (titleDom):
                item['title'] = titleDom[0].strip().encode('utf-8')
                # print (item['title'])
        except:
            pass

        # review_count
        try:
            review_countDom = tree.xpath("//div[@id='comment-count']/a[contains(@class, 'count')]/text()")
            if (review_countDom):
                item['review_count'] = review_countDom[0].strip().encode('utf-8')
                # print (item['review_count'])
        except:
            pass

        # shop
        try:
            shopDom = tree.xpath("//div[@id='popbox']//h3/a/text()")
            if (shopDom):
                item['shop_name'] = shopDom[0].strip().encode('utf-8')
                # print (item['shop_name'])
                shoplinkDom = tree.xpath("//div[@class='pop-score-summary']/a/@href")
                if (shoplinkDom):
                    item['shop_link'] = "https:" + shoplinkDom[0]
                    # print (item['shop_link'])
                    if (item['shop_link']):
                        shop_id = shoplinkDom[0].split("-")[1].replace(".html", "").strip()
                        item['shop_id'] = shop_id
                        # print (item['shop_id'])
                else:
                    shoplinkDom = tree.xpath("//div[@id='popbox']//h3/a/@href")
                    if (shoplinkDom):
                        item['shop_link'] = "https:" + shoplinkDom[0]
                        # print (item['shop_link'])
                try:
                    shop_sum = tree.xpath("//div[@class='pop-score-summary']//div[@class='score-sum']/span/text()")
                    if (shop_sum):
                        item['shop_score'] = shop_sum[0]
                        # print (item['shop_score'])
                except Exception as err:
                    print (err)
                #sellerpage_url
                try:
                    sellerpage_urlDom=tree.xpath("//*[@class='pop-score-summary']/a[1]/@href")
                    if(sellerpage_urlDom):
                        item['sellerpage_url']="https:"+sellerpage_urlDom[0]
                        # print item['sellerpage_url']
                except Exception as err:
                    print err
        except Exception as err:
            print (err)
        if (len(item) > 0):
            data.append(item)
        if (len(data) > 0):
            return data

