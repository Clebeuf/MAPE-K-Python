# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CalendarItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    

class WebItem(scrapy.Item):

    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        super(WebItem, self).__setitem__(key, value)

    url     = scrapy.Field()
    title   = scrapy.Field()