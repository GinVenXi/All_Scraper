#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from lxml import etree
import re
from Models.processor import Model_Processor
import sys

'''
        # 新浪视频解析代码*
'''
class Model_Processor_Sina_Video(Model_Processor):

    def process(self, html):
        if html == '' or html == 'None':
            print ("Can't get them html from http://video.sina.com.cn/")
            sys.exit()
        tree = etree.HTML(html)
        try:
            shipin_a_tags = tree.xpath("//*[@class='VF_wrap']/div[contains(@class, 'VF')]//a")
            if (shipin_a_tags):
                # print (len(shipin_a_tags))
                data = []
                for a_tag in shipin_a_tags:
                    item = {}
                    try:
                        if ("http" in a_tag.xpath("@href")[0]):
                            # url
                            item['url'] = self.formatUrl(a_tag.xpath("@href")[0].strip(), "sina")
                            # print (item['url'])
                            # 新闻类型
                            if (item['url']):
                                type = item['url'].split(".sina.com.cn")[0].replace("http://", "")
                                if ("slide" in type and "." in type):
                                    type = "slide"
                                elif ("." in type):
                                    type = type.split(".")[1]
                                item['type'] = type
                                # print (item['type'])
                            # title
                            try:
                                item['title'] = a_tag.xpath("@title")[0].replace("\n", "").strip()
                            except:
                                try:
                                    item['title'] = a_tag.xpath("text()")[0].replace("\n", "").strip()
                                except:
                                    item['title'] = a_tag.xpath("preceding-sibling::div/div[@class='tl']/strong/text()")[0].replace("\n", "").strip()
                            # print item['title']
                            # 新闻id
                            try:
                                item['url_id'] = str(item['url'].split("/")[-1].split(".")[0])
                                # print (item['url_id'])
                            except:
                                pass
                    except:
                        pass
                    try:
                        # 判断url中是否有数字，即url中是否包含id
                        url_id = (re.search('.*([0-9]+).*', item['url_id']))
                    except:
                        pass
                    if (len(item) > 0 and url_id != None):
                        # print (item)
                        data.append(item)
            if (len(data)>0):
                return data
        except Exception as err:
            print (err)