#-*-coding:utf-8*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class crack_tan_code():
    def crack_tan_code(self,url):
        try:
            global driver
            binary=FirefoxBinary('/home/buweixin/下载/firefox/firefox-bin')
            driver=webdriver.Firefox(firefox_binary=binary)
            driver.get(url)
            html=driver.page_source
            html_1=html.encode("utf-8")
            if(html_1.find("ui-dialog")!=-1 or html_1.find("加油！您和宝贝只有一个验证码的距离啦！")!=-1 or html_1.find("ui-dialog-close")!=-1):
                driver.refresh()
        except Exception as err:
            print err