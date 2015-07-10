# -*- coding: utf-8 -*-
import scrapy, sys, os, time
import logging

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from ManagedScraper.items import WebItem
from scrapy.http import Request
from scrapy.conf import settings

from scrapy import log
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

class DmozSpiderSpider(CrawlSpider):
    name = "dmoz-spider"
    allowed_domains = ["dmoz.org"]
    start_urls = ['http://www.dmoz.org/Computers/',
                  'http://www.dmoz.org/Society/',
                  'http://www.dmoz.org/Sports/']
     
    rules = [Rule(LxmlLinkExtractor(allow=('(http://www.dmoz.org/).+')), callback = 'parse_item', follow=True)]

    #LOG_FILE = "data/scrapy_%s.log" % datetime.now().strftime('%Y-%m-%dZ%H-%M')
    #logfile = open(LOG_FILE, 'w')
    #log_observer = ScrapyFileLogObserver(logfile, level=logging.INFO)
    #log_observer.start()

    def parse_item(self, response):

        item = WebItem()

        item['title'] = response.xpath('//title/text()').extract().pop().encode('utf-8')
        item['url'] = response.url

        return item