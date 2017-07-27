#-*-coding:utf-8*-
from selenium.webdriver import ActionChains
import time

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
