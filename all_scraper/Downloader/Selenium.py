#!/usr/bin/env python
#--coding:utf-8-*-
#导入selenium模块
import os

from selenium import webdriver
#selenium键盘事件
#需要引入 keys 包
from selenium.webdriver.common.keys import Keys
#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
#导入下拉菜单类
from selenium.webdriver.support.select import Select
import time
from Downloader.Abstract import Downloader_Abstract
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Downloader_Selenium(Downloader_Abstract):
    def __init__(self , data):
        __strs = data.lower()
        if __strs == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--dns-prefetch-disable')
            # PROXY = "66.248.220.135:80"  # IP:PORT or HOST:PORT
            # options.add_argument('--proxy-server=http://%s' % PROXY)
            # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            # self.driver = webdriver.Chrome(chrome_options=options)
            # 添加一个自定义的代理插件（配置特定的代理，含用户名密码认证）
            # options.add_extension(get_chrome_proxy_extension(proxy='username:password@ip:port'))
            self.driver = webdriver.Chrome(chrome_options=options)
            # self.driver = webdriver.Chrome()
        elif __strs == "all":
            # 禁止加载资源
            firefox_profile = webdriver.FirefoxProfile()
            # firefox_profile.set_preference("browser.download.folderList", 2)
            # 禁止加载css文件
            # firefox_profile.set_preference("permissions.default.stylesheet", 2)
            # 禁止加载图片
            # firefox_profile.set_preference("permissions.default.image", 2)
            # 禁止加载JS
            # firefox_profile.set_preference("javascript.enable", False)
            # browser = webdriver.Firefox(firefox_profile=firefox_profile)
            self.driver = webdriver.Firefox(firefox_profile)
        elif __strs == "firefox_yimaibao":
            # 禁止加载资源
            firefox_profile = webdriver.FirefoxProfile()
            # firefox_profile.set_preference("browser.download.folderList", 2)
            # 禁止加载css文件
            # firefox_profile.set_preference("permissions.default.stylesheet", 2)
            # 禁止加载图片
            # firefox_profile.set_preference("permissions.default.image", 2)
            # 禁止加载JS
            # firefox_profile.set_preference("javascript.enable", False)
            # browser = webdriver.Firefox(firefox_profile=firefox_profile)
            firefox_profile.set_preference('network.proxy.type', 1)  # 默认值0，就是直接连接；1就是手工配置代理。
            firefox_profile.set_preference('network.proxy.socks', "66.248.220.135")
            firefox_profile.set_preference('network.proxy.socks_port', 80)
            firefox_profile.set_preference('network.proxy.ssl', "66.248.220.135")
            firefox_profile.set_preference('network.proxy.ssl_port', 80)
            firefox_profile.update_preferences()
            self.driver = webdriver.Firefox(firefox_profile)
        elif __strs == "phantomjs":
            self.driver = webdriver.PhantomJS()

    '''
    selenium 获取网页源码
    '''
    def get_html(self , url):
        self.open(url)
        return self.get_page_source()

    '''
    selenium 用于打开网页
    '''
    def open(self , url):
        return self.driver.get(url)

    '''
    selenium 获取网页资源
    '''
    def get_page_source(self):
        return self.driver.page_source

    '''
    selenium 设置浏览器打开时间
    '''
    def set_page_load_timeout(self , second):
        return self.driver.set_page_load_timeout(second)

    '''
    selenium 控制浏览器大小
    '''
    def set_window_size(self , width, height):
        return self.driver.set_window_size(width , height)

    '''
    selenium 浏览器最大化
    '''
    def maximize_window(self):
        return self.driver.maximize_window()

    '''
    selenium 控制浏览器后退
    '''
    def back(self):
        return self.driver.back()

    '''
    selenium 控制浏览器前进
    '''
    def forward(self):
        return self.driver.forward()

    '''
    selenium 控制浏览器刷新
    '''
    def refresh(self):
        return self.driver.refresh()

    '''
    selenium 清除文本
    '''
    def clear(self , id):
        # return self.driver.find_element_by_id(id).clear()
        return self.driver.find_element_by_xpath("//*[@id='"+id+"' and @rows='"+1+"']").clear()

    '''
    selenium 模拟按键输入
    '''
    def send_key(self , id , value):
        return self.driver.find_element_by_id(id).send_keys(value)

    '''
    selenium 单击元素
    '''
    def click(self , id):
        return self.driver.find_element_by_id(id).click()

    '''
    selenium 模拟点击2
    '''
    def click2(self , id , tag_name):
        return self.driver.find_element_by_id(id).find_element_by_tag_name(tag_name).click()

    '''
    WebElement 接口常用方法
    selenium submit() 提交
    '''
    def submit(self , id):
        return self.driver.find_element_by_id(id).submit()

    '''
    selenium 返回元素的尺寸
    '''
    def size(self , id):
        return self.driver.find_element_by_id(id).size

    '''
    selenium 返回元素的文本
    '''
    def text(self , id):
        return self.driver.find_element_by_id(id).text

    '''
    selenium 获得元素的属性，可以是id/name/type或其他任意属性
    '''
    def get_attribute(self , id , attribute):
        return self.driver.find_element_by_id(id).get_attribute(attribute)

    '''
    selenium 返回元素是否可见，返回结果为True或False
    '''
    def is_displayed(self , id):
        return  self.driver.find_element_by_id(id).is_displayed()

    '''
    selenium 鼠标事件 右击
    '''
    def context_click(self , id):
        #定位到要右击的元素
        right_click = self.driver.find_element_by_id(id)
        #对定位到的元素执行右击操作
        return ActionChains(self.driver).context_click(right_click).perform()

    '''
    selenium 鼠标事件 悬停
    '''
    def move_to_element(self , id):
        #定位到要悬停的元素
        above = self.driver.find_element_by_id(id)
        #对定位到的元素执行悬停操作
        return ActionChains(self.driver).move_to_element(above).perform()

    '''
    selenium 鼠标事件 双击
    '''
    def double_click(self , id):
        #定位到要双击的元素
        double_click = self.driver.find_element_by_id(id)
        #对定位到的元素执行双击操作
        return ActionChains(self.driver).double_click(double_click).perform()

    '''
    selenium 鼠标事件 拖动
    '''
    def drag_and_drop(self , source_id , target_id):
        #定位元素的原位置
        element = self.driver.find_element_by_id(source_id)
        #定位元素要移动到的目标位置
        target = self.driver.find_element_by_id(target_id)
        #执行元素的施放操作
        return ActionChains(self.driver).drag_and_drop(element , target).perform()

    '''
    selenium 键盘事件 删除键
    '''
    def backspace(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.BACK_SPACE)

    '''
    selenium 键盘事件 空格键
    '''
    def space(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.SPACE)

    '''
    selenium 键盘事件 制表键
    '''
    def tab(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.TAB)

    '''
    selenium 键盘事件 回退键
    '''
    def esc(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.ESCAPE)

    '''
    selenium 键盘事件 回车键
    '''
    def enter(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.ENTER)

    '''
    selenium 键盘事件 全选 ctrl + a (全选某输入框内容)
    '''
    def control_a(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.CONTROL, 'a')

    '''
    selenium 键盘事件 复制 ctrl + c
    '''
    def control_c(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.CONTROL, 'c')

    '''
    selenium 键盘事件 剪切 ctrl + x
    '''
    def control_x(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.CONTROL, 'x')

    '''
    selenium 键盘事件 粘贴 ctrl + v
    '''
    def control_v(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.CONTROL, 'v')

    '''
    selenium 键盘事件 F1-F12
    '''
    def f(self , id):
        return self.driver.find_element_by_id(id).send_keys(Keys.F5)

    '''
    selenium 获得验证信息 打印当前页面URL
    '''
    def url(self):
        return self.driver.current_url

    '''
    selenium 设置元素等待 显式等待
    '''
    def waitforelement(self, second, value):
        return WebDriverWait(self.driver, second).until(EC.presence_of_element_located(By.ID, value)
        )

    '''
    selenium 设置元素等待 隐式等待
    '''
    def implicitly_wait(self , second):
        return self.driver.implicitly_wait(second)

    '''
    selenium 设置元素等待 sleep休眠方法
    '''
    def sleep(self , second):
        return time.sleep(second)

    '''
    selenium 警告框处理
    '''
    def  switch_to_alert(self):
        return self.driver.switch_to_alert().accept()

    '''
    selenium 窗口截图 并指定截图图片的保存位置
    '''
    def get_screenshot_as_file(self , position):
        return self.driver.get_screenshot_as_file(position)

    '''
    selenium 调用JavaScript控制浏览器滚动条 参数为水平位置和垂直位置
    '''
    def scrollTo(self , horizontal_position = 0 , Vertical_position = 0):
        js = "window.scrollTo( " + str(horizontal_position) + " , " + str(Vertical_position) + ");"
        return self.driver.execute_script(js)

    ''' 解析网页
    selenium 获取网页Title (可能最后不放在这里)
    '''
    def get_page_title(self):
        return self.driver.title

    '''
    selenium 退出浏览器
    '''
    def quit(self):
        return self.driver.quit()


    '''
    selenium 使用xpath查找元素
    '''
    def xpath(self , value):
        return self.driver.find_element_by_xpath(value)

    def xpath_click(self, value):
        return self.driver.find_element_by_xpath(value).click()

    '''
    selenium 使用Select获取下拉菜单
    '''
    def select(self , sel , value):
        Select(sel).select_by_value(value)

    '''
    selenium select下拉框获取value值
    '''
    def is_option_value_present(self, asin , element_id, tag_name, option_text):
        select = self.driver.find_element_by_id(element_id)
        # 注意使用find_elements
        options_list = select.find_elements_by_tag_name(tag_name)
        for option in options_list:
            value = str(option.get_attribute("value"))[2:]
            # print (value)
            if(value == asin):
                print ("Value is: " + value)
                # print (option.get_attribute("value"))
                return option.get_attribute("value")
            # print ("Text is:" +option.text)
            # if option_text in option.text:
            #     select_value = option.get_attribute("value")
            #     print ("option_textoption_textoption_textValue is: " + select_value)
            #     break
        # return select_value
