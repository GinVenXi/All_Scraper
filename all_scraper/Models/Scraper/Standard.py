#coding: utf-8
'''
创建人：Javen
创建时间：2017/2/10 21：59
'''
import json
import urllib2
from Models.Scrape.Firefox import Model_Scrape_Firefox
from Models.Static.Scrape.Status import Model_Static_Scrape_Status
from Models.scraper import Model_Scraper

class Model_Scraper_Standard(Model_Scraper):
    def __init__(self , region):
        super(Model_Scraper_Standard, self).__init__(region)
        self.region = region
        self.Scrape_Firefox = Model_Scrape_Firefox(region)

    def process(self , url):
        self.Scrape_Firefox.process(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        elif (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
            content = None
        return content

    def mobile_process(self, url):
        req = urllib2.Request(url=url)
        res_data = urllib2.urlopen(req)
        data = json.loads(res_data.read())
        return data

    def processReview(self, url):
        self.Scrape_Firefox.process_review(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        elif (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
            content = None
        return content

    def processkeywords(self, url):
        self.Scrape_Firefox.process_keywords(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        elif (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
            content = None
        return content

    def processOffer(self, url):
        self.Scrape_Firefox.process_offer(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        elif (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS_NO_DATA):
            content = None
        return content

    def processInventory(self, url):
        self.Scrape_Firefox.process_inventory(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        # self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        return content

    def processTopReviewer(self, url):
        self.Scrape_Firefox.process_TopReviewer(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        return content

    def processSeller(self, url):
        self.Scrape_Firefox.process_seller(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        return content

    def processSellerProduct(self, url):
        self.Scrape_Firefox.process_sellerproduct(url)
        self.lastScrapeStatus = self.Scrape_Firefox.getStatus()
        self.addScrape(self.Scrape_Firefox.getScrape())
        if (self.lastScrapeStatus == Model_Static_Scrape_Status.SUCCESS):
            content = self.Scrape_Firefox.getContent()
        return content