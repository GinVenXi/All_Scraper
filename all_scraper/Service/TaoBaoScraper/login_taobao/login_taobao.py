#-*-coding:utf-8*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


#淘宝模拟登录
class login_taobao():
    def login_taobao(self):
        loginUrl = 'https://login.taobao.com/'
        Binary = FirefoxBinary("/home/buweixin/下载/firefox/firefox-bin")
        global driver
        driver = webdriver.Firefox(firefox_binary=Binary)
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
        # # 找到淘宝网首页按钮并进行点击
        # logindriver.find_element_by_xpath("//*[@id='J_SiteNavHome']/div/a/span").click()
        # 打印cookie
        # cookie_list = logindriver.get_cookies()
        # print cookie_list[0]