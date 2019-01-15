# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleplaycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    URL = scrapy.Field()
    Price = scrapy.Field()
    Genre = scrapy.Field()
    Downloads = scrapy.Field()
    Rating = scrapy.Field()
    Review_number = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Version = scrapy.Field()