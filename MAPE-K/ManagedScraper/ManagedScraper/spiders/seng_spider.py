# -*- coding: utf-8 -*-
import scrapy


class SengSpiderSpider(scrapy.Spider):
    name = "seng-spider"
    allowed_domains = ["courses.seng.uvic.ca"]
    start_urls = (
        'http://www.courses.seng.uvic.ca/',
    )

    def parse(self, response):
        pass
