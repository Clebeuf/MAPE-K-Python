# -*- coding: utf-8 -*-
import scrapy

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

class CalendarSpiderSpider(CrawlSpider):
    name = "calendar-spider"
    allowed_domains = ["uvic.ca"]
    start_urls = [
        'http://web.uvic.ca/calendar2015-09/CDs/CSC/CTs.html',
        'http://web.uvic.ca/calendar2015-09/CDs/CSC/466.html'
    ]
     
    #(http://web.uvic.ca/calendar2015-09/CDs/)(CSC|MATH|SENG).+')
    
    rules = [Rule(LxmlLinkExtractor(allow=('(http://web.uvic.ca/calendar2015-09/CDs/).+'), 
                                    restrict_xpaths=('//div[@id="CDpage"]', '//ul[@class="CDTL"]')),
                                    callback = 'parse_item', follow=True)]

    def parse_item(self, response):

        item = WebItem()
        item['title'] = response.xpath('//title/text()').extract().pop().encode('utf-8')
        item['url'] = response.url

        return item