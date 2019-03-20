# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SmokerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_cn = scrapy.Field()
    name_eng = scrapy.Field()
    smoke_type = scrapy.Field()
    tar = scrapy.Field()
    nicotine = scrapy.Field()
    co = scrapy.Field()
    package_type = scrapy.Field()
    spec = scrapy.Field()
    is_middle = scrapy.Field()
    pack_barcode = scrapy.Field()
    bar_barcode = scrapy.Field()
    pack_retail_price = scrapy.Field()
    bar_retial_price = scrapy.Field()
    whole_sale_price = scrapy.Field()
    time_to_market = scrapy.Field()
    sale_status = scrapy.Field()
    pic_url = scrapy.Field()
