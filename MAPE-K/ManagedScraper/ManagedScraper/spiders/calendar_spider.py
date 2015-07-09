# -*- coding: utf-8 -*-
import scrapy


class CalendarSpiderSpider(scrapy.Spider):
    name = "calendar-spider"
    allowed_domains = ["web.uvic.ca"]
    start_urls = (
        'http://www.web.uvic.ca/',
    )

    def parse(self, response):
        pass
