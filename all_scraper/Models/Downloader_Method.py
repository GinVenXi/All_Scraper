#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import json
import urllib

import requests
import sys
from lxml import etree

from Downloader.Abstract import Downloader_Abstract
from Downloader.Selenium import Downloader_Selenium

import time

from requests import RequestException
from selenium.webdriver.support.select import Select


class Model_Downloader_Method(Downloader_Abstract):
    def __init__(self, method):
        self.method = method

    def print_ts(self , message):
        print "[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)

    def getContent(self):
        return self.content

    def downloader_init(self):
        try:
            global downloader_perform
            downloader_perform = Downloader_Selenium(self.method)
        except Exception as err:
            print (err)

    def downloader_login(self):
        try:
            global downloader_perform
            try:
                downloader_perform.set_page_load_timeout(60)
                url = "https://www.amazon.com/bestsellers"
                downloader_perform.get_html(url)
                # 判断机器人
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    while (robot):
                        print "get a robot"
                        time.sleep(1)
                        downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    try:
                        time.sleep(3)
                        downloader_perform.click("nav-link-accountList")
                        time.sleep(10)
                        downloader_perform.send_key("ap_email", "2142232499@qq.com")
                        time.sleep(1)
                        downloader_perform.send_key("ap_password", "Cdef2345$")
                        time.sleep(1)
                        downloader_perform.xpath_click("//*[@type='checkbox' and @name='rememberMe']")
                        time.sleep(1)
                        downloader_perform.click("signInSubmit")
                        time.sleep(30)
                        return True
                    except Exception as err:
                        print (err)
                        return False
            except:
                # 获取登录按钮//*[@id="nav-link-accountList"]
                try:
                    time.sleep(3)
                    downloader_perform.click("nav-link-accountList")
                    time.sleep(10)
                    downloader_perform.send_key("ap_email", "2142232499@qq.com")
                    time.sleep(1)
                    downloader_perform.send_key("ap_password", "Cdef2345$")
                    time.sleep(1)
                    downloader_perform.xpath_click("//*[@type='checkbox' and @name='rememberMe']")
                    time.sleep(1)
                    downloader_perform.click("signInSubmit")
                    time.sleep(30)
                    return True
                except:
                    return False
        except Exception as err:
            print (err)

    def downloader_quit(self):
        try:
            global downloader_perform
            downloader_perform.quit()
        except Exception as err:
            print (err)

    def Scrape(self, asin):
        # downloader_perform.implicitly_wait(5)
        # try:
        #     sel = downloader_perform.xpath("//select[@id='native_dropdown_selected_size_name']")
        #     # native_dropdown_selected_size_name
        #     time.sleep(3)
        #     value = downloader_perform.is_option_value_present(asin, 'native_dropdown_selected_size_name','option', None)
        #
        #     time.sleep(2)
        #     Select(sel).select_by_value(value)
        #     # downloader_perform.select(sel, value)
        # except:
        #     pass
        # time.sleep(1)
        html = downloader_perform.get_page_source()
        return html

    def get_utf8_page(self, url):  # 判断页面的请求状态来做异常处理
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "utf-8"
            if response.status_code == 200:  # 200是请求成功
                return response.text
            return None
        except RequestException:
            return None

    def downloader(self, url):
        try:
            global downloader_perform
            downloader_perform.set_page_load_timeout(5)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        # print "get a robot"
                        robot_html = downloader_perform.get_page_source()
                        # print (robot_html)
                        tree = etree.HTML(robot_html)
                        src = tree.xpath("//div[@class='a-row a-text-center']/img/@src")
                        # print (src[0])
                        if (src):
                            imageUrl = src[0]
                            decodeurl = "http://47.88.2.41/captcha.php?url=" + str(imageUrl)
                            text = self.get_utf8_page(decodeurl)
                            result = json.loads(text.split("</font>")[1].replace("(", "").replace(")", "").strip())
                            # print (result['captcha'])
                            check_code = result['captcha']
                            downloader_perform.send_key("captchacharacters", check_code)
                            time.sleep(1)
                            downloader_perform.xpath_click("//*[@class='a-button-text']")
                        time.sleep(1)
                        # downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                # 判断是出错信息
                try:
                    # //*[@id="g"]/div/a/img //*[@id="g"]/div/a/img
                    noData_note = downloader_perform.xpath("//*[@id='g']/div/a/img/@alt")
                    if (noData_note):
                        # print noData_note
                        return 2
                except:
                    pass
            except:
                # print ("time out after 8 seconds when loading page")
                # 判断是出错信息
                try:
                    # //*[@id="g"]/div/a/img //*[@id="g"]/div/a/img
                    noData_note = downloader_perform.xpath("//*[@id='g']/div/a/img/@alt")
                    if (noData_note):
                        # print noData_note
                        return 2
                except:
                    pass
                try:
                    downloader_perform.xpath("//*[@id='nav-flyout-ya-signin']")
                except:
                    try:
                        downloader_perform.xpath("//*[@id='add-to-cart-button']")
                    except:
                        try:
                            downloader_perform.xpath("//*[@id='add-to-cart-button-ubb']")
                        except:
                            try:
                                downloader_perform.xpath("//*[@id='add-to-wishlist-button-submit']")
                            except:
                                try:
                                    downloader_perform.xpath("//*[@id='dv-action-box-wrapper']")
                                except:
                                    try:
                                        downloader_perform.xpath("//*[@id='ebooksImportantMessage_feature_div']")
                                    except:
                                        return 0
            # downloader_perform.scrollTo(0, 10000)
            # time.sleep(1)
            # downloader_perform.scrollTo(0, 0)
            asin = url.split("/")[-1].strip()
            html = self.Scrape(asin)
            if(html == False):
                return 0
            elif(html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def review_Scraper(self):
        try:
            # downloader_perform.implicitly_wait(3)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
        return html

    def review_downloader(self, url):
        try:
            global downloader_perform
            # offer_downloader_perform = Downloader_Selenium("chrome")
            downloader_perform.set_page_load_timeout(10)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        # print "get a robot"
                        # time.sleep(1)
                        # downloader_perform.refresh()
                        robot_html = downloader_perform.get_page_source()
                        # print (robot_html)
                        tree = etree.HTML(robot_html)
                        src = tree.xpath("//div[@class='a-row a-text-center']/img/@src")
                        # print (src[0])
                        if (src):
                            imageUrl = src[0]
                            decodeurl = "http://47.88.2.41/captcha.php?url=" + str(imageUrl)
                            text = self.get_utf8_page(decodeurl)
                            result = json.loads(text.split("</font>")[1].replace("(", "").replace(")", "").strip())
                            # print (result['captcha'])
                            check_code = result['captcha']
                            downloader_perform.send_key("captchacharacters", check_code)
                            time.sleep(1)
                            downloader_perform.xpath_click("//*[@class='a-button-text']")
                        time.sleep(1)
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                try:
                    # 判断没有评论信息
                    noReviews = downloader_perform.xpath("//*[@class='a-row a-spacing-small']/span[@class='a-size-base']")
                    if (noReviews):
                        if (noReviews.text == "Share your thoughts with other customers"):
                            return 2
                except Exception as err:
                    print (err)
            except:
                print ("time out after 10 seconds when loading review page")
                try:
                    current_url = urllib.unquote(downloader_perform.url())
                    # print (current_url)
                    # print (url)
                    if (current_url != url):
                        return 0
                    downloader_perform.xpath("//*[@id='nav-flyout-ya-signin']")
                except:
                    # self.offer_quit()
                    return 0
                try:
                    # 判断没有评论信息
                    noReviews = downloader_perform.xpath("//*[@class='a-row a-spacing-small']/span[@class='a-size-base']")
                    if (noReviews):
                        if (noReviews.text == "Share your thoughts with other customers"):
                            return 2
                except Exception as err:
                    print (err)
            downloader_perform.scrollTo(0, 10000)
            time.sleep(1)
            downloader_perform.scrollTo(0, 0)
            html = self.review_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def keywords_Scraper(self):
        try:
            # downloader_perform.implicitly_wait(1)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
        else:
            return html

    def keywords_downloader(self, url):
        try:
            global downloader_perform
            try:
                downloader_perform.set_page_load_timeout(10)
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        # print "get a robot"
                        robot_html = downloader_perform.get_page_source()
                        # print (robot_html)
                        tree = etree.HTML(robot_html)
                        src = tree.xpath("//div[@class='a-row a-text-center']/img/@src")
                        # print (src[0])
                        if (src):
                            imageUrl = src[0]
                            decodeurl = "http://47.88.2.41/captcha.php?url=" + str(imageUrl)
                            text = self.get_utf8_page(decodeurl)
                            result = json.loads(text.split("</font>")[1].replace("(", "").replace(")", "").strip())
                            # print (result['captcha'])
                            check_code = result['captcha']
                            downloader_perform.send_key("captchacharacters", check_code)
                            time.sleep(1)
                            downloader_perform.xpath_click("//*[@class='a-button-text']")
                        time.sleep(1)
                        # downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                # print (downloader_perform.url())
                current_url = (urllib.quote(downloader_perform.url())).replace("%25", "%")
                # print (current_url.replace("%25", "%"))
                # print (urllib.quote(url))
                if (current_url != urllib.quote(url)):
                    return 0
            except:
                print ("time out after 10 seconds when loading page")
                # 进行网址判断
                try:
                    # print (downloader_perform.url())
                    current_url = (urllib.quote(downloader_perform.url())).replace("%25", "%")
                    # print (current_url.replace("%25", "%"))
                    # print (urllib.quote(url))
                    if (current_url != urllib.quote(url)):
                        return 0
                    # downloader_perform.xpath("//*[@id='refinements']")
                except:
                    pass
                    # try:
                    #     downloader_perform.xpath("//*[@id='nav-flyout-ya-signin']")
                    # except:
                    #     return 0
            # 关键词查找没有结果返回None
            try:
                no_results = downloader_perform.xpath("//*[@id='noResultsTitle']")
                if (no_results):
                    return 2
            except:
                pass
            html = self.keywords_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    # offer_list 下载器
    def offer_Scraper(self):
        try:
            # downloader_perform.implicitly_wait(3)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
            return False
        else:
            return html

    def refresh_again(self):
        global downloader_perform
        downloader_perform.refresh()

    def offer_downloader(self, url):
        try:
            global downloader_perform
            downloader_perform.set_page_load_timeout(10)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        # print "get a robot"
                        # time.sleep(1)
                        # downloader_perform.refresh()
                        '''
                        破解验证码
                        '''
                        # print "get a robot"
                        robot_html = downloader_perform.get_page_source()
                        # print (robot_html)
                        tree = etree.HTML(robot_html)
                        src = tree.xpath("//div[@class='a-row a-text-center']/img/@src")
                        # print (src[0])
                        if (src):
                            imageUrl = src[0]
                            decodeurl = "http://47.88.2.41/captcha.php?url=" + str(imageUrl)
                            text = self.get_utf8_page(decodeurl)
                            result = json.loads(text.split("</font>")[1].replace("(", "").replace(")", "").strip())
                            # print (result['captcha'])
                            check_code = result['captcha']
                            downloader_perform.send_key("captchacharacters", check_code)
                            time.sleep(1)
                            downloader_perform.xpath_click("//*[@class='a-button-text']")
                        time.sleep(1)
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                # 判断是出错界面
                try:
                    # //*[@id="g"]/div/a/img //*[@id="g"]/div/a/img
                    noData_note = downloader_perform.xpath("//*[@id='g']/div/a/img/@alt")
                    if (noData_note):
                        # print noData_note
                        return 0
                except:
                    pass
                # 判断没有offer数据
                try:
                    noOffer_note = downloader_perform.xpath("//*[@id='olpOfferList']/div/p")
                    if (noOffer_note):
                        # print (noOffer_note.text)
                        # com, co.uk
                        if (noOffer_note.text == "There are currently no listings for this product."):
                            return 2
                        # fr
                        elif (noOffer_note.text == "Il n'y a actuellement aucune mise en vente pour ce produit."):
                            return 2
                        # es
                        elif (noOffer_note.text == "No existen listados para este producto."):
                            return 2
                except:
                    pass
            except:
                print ("time out after 10 seconds when loading page")
                # 判断没有offer数据
                try:
                    noOffer_note = downloader_perform.xpath("//*[@id='olpOfferList']/div/p")
                    if (noOffer_note):
                        # print (noOffer_note.text)
                        # com, co.uk, ca
                        if (noOffer_note.text == "There are currently no listings for this product."):
                            return 2
                        # de
                        elif (noOffer_note.text == "Es gibt derzeit keine Listungen für dieses Produkt."):
                            return 2
                        # co.jp
                        elif (noOffer_note.text == "現在、この商品の出品はありません。"):
                            return 2
                        # fr
                        elif (noOffer_note.text == "Il n'y a actuellement aucune mise en vente pour ce produit."):
                            return 2
                        # es
                        elif (noOffer_note.text == "No existen listados para este producto."):
                            return 2
                        # it
                        elif (noOffer_note.text == "Al momento non ci sono offerte per questo prodotto."):
                            return 2
                except:
                    pass
                try:
                    downloader_perform.xpath("//*[@id='olpOfferList']")
                except:
                    return 0
            html = self.offer_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def inventory_Scraper(self):
        try:
            # offer_downloader_perform.click("nav-search-submit-text")
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
        else:
            return html

    def inventory_downloader(self, url):
        try:
            global downloader_perform
            downloader_perform.set_page_load_timeout(10)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        print "get a robot"
                        time.sleep(1)
                        downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
            except:
                print ("time out after 10 seconds when loading inventory page")
            html = self.inventory_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def topreviewer_Scraper(self):
        try:
            downloader_perform.implicitly_wait(3)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
            return False
        else:
            return html

    def topreviewer_downloader(self, url):
        try:
            global downloader_perform
            # offer_downloader_perform = Downloader_Selenium("chrome")
            downloader_perform.set_page_load_timeout(20)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        print "get a robot"
                        time.sleep(1)
                        downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                current_url = downloader_perform.url()
                # print (current_url)
                # print (url)
                if (current_url != url):
                    return 0
            except:
                current_url = downloader_perform.url()
                # print (current_url)
                # print (url)
                if (current_url != url):
                    return 0
                print ("time out after 20 seconds when loading topreviewer page")
            html = self.topreviewer_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def seller_Scraper(self):
        try:
            # downloader_perform.implicitly_wait(3)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
            return False
        else:
            return html

    def seller_downloader(self, url):
        try:
            global downloader_perform
            # offer_downloader_perform = Downloader_Selenium("chrome")
            downloader_perform.set_page_load_timeout(15)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        print "get a robot"
                        time.sleep(1)
                        downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                current_url = downloader_perform.url()
                # print (current_url)
                # print (url)
                if (current_url != url):
                    return 0
            except:
                print ("time out after 15 seconds when loading seller page")
                try:
                    current_url = downloader_perform.url()
                    # print (current_url)
                    # print (url)
                    if (current_url != url):
                        return 0
                    downloader_perform.xpath("//*[@id='nav-flyout-ya-signin']")
                except:
                    # self.offer_quit()
                    return 0
            html = self.seller_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)

    def sellerproduct_Scraper(self):
        try:
            # downloader_perform.implicitly_wait(3)
            html = downloader_perform.get_page_source()
        except Exception as err:
            print (err)
            return False
        else:
            return html

    def sellerproduct_downloader(self, url):
        try:
            global downloader_perform
            # offer_downloader_perform = Downloader_Selenium("chrome")
            downloader_perform.set_page_load_timeout(30)
            try:
                downloader_perform.get_html(url)
                try:
                    robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                    # 当前日期
                    import datetime
                    now = datetime.datetime.now()
                    now_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open("./log.log", "a") as f:
                        f.write(str(now_date) + "---find a robot" + "\n")
                    while (robot):
                        print "get a robot"
                        time.sleep(1)
                        downloader_perform.refresh()
                        try:
                            robot = downloader_perform.xpath("/html/body/div/div[1]/div[2]/div/p")
                        except:
                            break
                except:
                    pass
                current_url = downloader_perform.url()
                # print (current_url)
                # print (url)
                if (current_url != url):
                    return 0
            except:
                print ("time out after 30 seconds when loading seller_product page")
                try:
                    current_url = downloader_perform.url()
                    # print (current_url)
                    # print (url)
                    if (current_url != url):
                        return 0
                    downloader_perform.xpath("//*[@id='nav-flyout-ya-signin']")
                except:
                    return 0
            html = self.sellerproduct_Scraper()
            if (html == False):
                return 0
            elif (html == None):
                return 2
            else:
                self.content = html
                return 1
        except Exception as err:
            print (err)