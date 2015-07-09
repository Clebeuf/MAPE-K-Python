# -*- coding: utf-8 -*-
import scrapy


class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz-spider"
    allowed_domains = ["dmoz.org"]
    start_urls = (
        'http://www.dmoz.org/',
    )

    def parse(self, response):
        pass
