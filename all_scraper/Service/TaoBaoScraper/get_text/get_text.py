#-*-coding:utf-8*-
import json
import time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
import requests
from selenium.webdriver import ActionChains
import time
#获取源码
class get_text():
    #获取keywords,product,sellerpage页面的html源码
    def __init__(self):
        global driver
        driver = webdriver.Chrome()

    def get_html_text(self,url):
        try:
            # binary = FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            # driver = webdriver.Chrome()
            # driver = webdriver.Firefox(firefox_binary=binary)
            global driver
            driver.get(url)
            return driver.page_source
        except Exception as err:
            print err

    def quit(self):
        global driver
        driver.quit()

    #获取review页面的json源码
    def get_json_text(self,url):
        try:
            # binary=FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            # driver = webdriver.Firefox(firefox_binary=binary)
            driver = webdriver.PhantomJS()
            driver.get(url)
            review_test = driver.page_source
            review_text = review_test
            # print review_text
            bwx = review_text.replace('<html><head></head><body>"rateDetail":', '').replace('</body></html>', '')
            # print bwx
            text = json.loads(bwx)
            return text
        except Exception as err:
            print err

#淘宝模拟登录
class login_taobao():
    def login_taobao(self):
        loginUrl = 'https://login.taobao.com/'
        # Binary = FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
        global driver
        # driver = webdriver.Firefox(firefox_binary=Binary)
        driver = webdriver.Firefox()
        driver.get(loginUrl)
        driver.find_element_by_xpath("//*[@id='J_QRCodeLogin']/div[5]/a[1]").click()
        time.sleep(2)
        # //*[@id="J_Form"]/div[2]/span
        driver.find_element_by_xpath("//*[@id='J_Form']/div[2]/label/i").send_keys("18951855579")
        time.sleep(2)
        # //*[@id="TPL_password_1"]
        # driver.find_element_by_xpath("//*[@id='password-label']/i").send_keys("bwxhhjy0605")
        driver.find_element_by_xpath("//*[@id='TPL_password_1']").send_keys("bwxhhjy0605")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
        time.sleep(3)
        html=driver.page_source
        html_1=html.encode("utf-8")
        if(html_1.find("bwxhhjy")!=-1):
            print("成功登录")
        else:
            login=login_taobao()
            login.login_taobao()
            html = driver.page_source
            html_1 = html.encode("utf-8")
            if (html_1.find("bwxhhjy") != -1):
                print("成功登录")
            else:
                print("报告长官，没能顺利登录，速来支援")
                sys.exit()

        # # 找到淘宝网首页按钮并进行点击
        # logindriver.find_element_by_xpath("//*[@id='J_SiteNavHome']/div/a/span").click()
        # 打印cookie
        # cookie_list = logindriver.get_cookies()
        # print cookie_list[0]

#破解图像验证码
class crack_verification_code():

    def crack_Verification_Code(html):
        try:
            tree = etree.HTML(html)
            src = tree.xpath("//*[@id='checkcodeImg']/@src")
            if (src):
                imageUrl = "https:" + src[0] + ".png"
                decodeUrl = "http://47.88.2.41/captcha.php?url=" + str(imageUrl)
                latestUrl = decodeUrl.encode("utf-8")
                codeText = requests.get(latestUrl)
                print codeText
                result = json.loads(codeText.split("</font>")[1].replace("(", "").replace(")", "").strip())
                check_code = result['captcha']
                # global driver
                # //*[@id="checkcodeInput"]
                driver.find_element_by_xpath("//*[@id='query']//div[@class='view']//p/input[@id='checkcodeInput']").send_keys(check_code)
                time.sleep(2)
                # //*[@id="query"]/div[2]/input
                driver.find_element_by_xpath("//*[@id='query']//div[@class='submit']//input[@type='submit']").click()
                time.sleep(2)
                return driver.page_source
            else:
                print ("no found image")
        except Exception as err:
            print err

#破解滑块验证码
class crack_slide_code():
    # 破解滑块验证码
    def crack_slide_code(self):
        try:
            # 以下为定位验证码所在位置操作
            # 将网页截图
            global driver
            driver.save_screenshot("screen.png")
            # 定位验证码的位置
            element = driver.find_element_by_xpath("//*[@id='J_StaticForm']//form[@id='J_Form']//div[@id='nocaptcha']//div[@class='nc_wrapper']//div[@class='nc_scale']//span[@class='nc_iconfont btn_slide']")
            # 获取滑块验证码的坐标
            location = element.location
            # 获取滑块验证码的长宽
            size = element.size
            # 找到一整块滑块验证码的位置坐标
            rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height']))

            # 点击滑动验证码并按住不放
            ActionChains(driver).click_and_hold(on_element=element).perform()
            time.sleep(3)
            # 移动滑动验证码到指定位置
            ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=location['x'],yoffset=location['y']).perform()
            time.sleep(3)
            # 释放鼠标
            ActionChains(driver).release(on_element=element).perform()
            time.sleep(3)
        except Exception as err:
            print err




