#-*-coding:utf-8*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import re
import json

class get_text():

    def get_html_text(self,url):
        try:
            # binary=FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            # driver=webdriver.Firefox(firefox_binary=binary)
            # global driver
            driver.get(url)
            time.sleep(2)
            #将下拉框拉到最后
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            return driver.page_source
        except Exception as err:
            print err

    def get_html_text_1(self,url):
        try:
            driver.get(url)
            # time.sleep(3)
            return driver.page_source
        except Exception as err:
            print err

    def get_json_text(self,url):
        try:
            # binary=FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            global driver
            # driver = webdriver.Firefox(firefox_binary=binary)
            driver = webdriver.PhantomJS()
            driver.get(url)
            review_test = driver.page_source
            temp = review_test
            # 利用正则表达式将头部的fetchJSON_comment98vv2327(去掉
            J = re.sub(r'\w*\(', '', review_test)
            # 去除开头结尾的html数据
            S = J.replace('<html><head></head><body>', '').replace(');</body></html>', '')
            latesttext = S.encode("utf-8")
            # 去除中间夹杂的div等html数据
            retext = re.compile('<[^>]+>')
            text = json.loads(retext.sub("", latesttext))
            # print text['comments'][0]['content']
            return text
        except Exception as err:
            print err

class login_jd():
    def login_JD(self):
        try:
            loginUrl = 'https://passport.jd.com/new/login.aspx'
            # binary = FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            global driver
            driver = webdriver.Chrome()
            # # driver = webdriver.Firefox(firefox_binary=binary)
            # driver.get(loginUrl)
            # driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div[2]/a").click()
            # time.sleep(1)
            # driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18951855579")
            # time.sleep(1)
            # driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("bwxhhjy201961")
            # time.sleep(1)
            # driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
        except Exception as err:
            print err