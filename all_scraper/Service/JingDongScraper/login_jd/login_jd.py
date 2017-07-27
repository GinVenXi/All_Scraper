#-*-coding:utf-8*-
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time

class login_jd():
    def login_JD(self):
        try:
            loginUrl = 'https://passport.jd.com/new/login.aspx'
            binary = FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
            global driver
            driver = webdriver.Firefox(firefox_binary=binary)
            driver.get(loginUrl)
            driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div[2]/a").click()
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18951855579")
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("bwxhhjy201961")
            driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
        except Exception as err:
            print err

