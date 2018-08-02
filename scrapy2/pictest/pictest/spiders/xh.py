# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from ..items import PictestItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = []
    for i in range(44):
        start_urls.append("http://www.xiaohuar.com/list-1-%d.html"%i)

    def parse(self, response):
        next = response.css("div.page")
        allPics = response.css('div.masonry_brick')
#        print(pic.css('div.item_t img::attr("src")').extract_first())
        for pic in allPics:
            item = PictestItem()
            name = pic.css('div.item_t img::attr("alt")').extract_first()
            addr = pic.css('div.item_t img::attr("src")').extract_first()
            addr = response.urljoin(addr)
            print(addr)
            item['name'] = name
            item['addr'] = addr
            yield item

