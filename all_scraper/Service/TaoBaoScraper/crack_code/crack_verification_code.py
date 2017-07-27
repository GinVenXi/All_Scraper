#-*-coding:utf-8*-
from lxml import etree
import requests
import json
import time

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
                global driver
                # //*[@id="checkcodeInput"]
                driver.find_element_by_xpath("//*[@id='query']//div[@class='view']//p/input[@id='checkcodeInput']").send_keys(check_code)
                time.sleep(2)
                # //*[@id="query"]/div[2]/input
                driver.find_element_by_xpath("//*[@id='query']//div[@class='submit']//input[@type='submit']").click()
                time.sleep(2)

            else:
                print ("no found image")
        except Exception as err:
            print err
