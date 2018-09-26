# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TencentspiderSpider(scrapy.Spider):
    #spider name
    name = 'tencentSpider'
    allowed_domains = ['tencent.com']
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [''.join([url, str(offset)]),]


    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['position_name'] = each.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = each.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = each.xpath("./td[2]/text()").extract_first()
            item['people_num'] = each.xpath("./td[3]/text()").extract_first()
            item['work_location'] = each.xpath("./td[4]/text()").extract_first()
            item['publish_time'] = each.xpath("./td[5]/text()").extract_first()

            yield item

        if self.offset < 1680:
            self.offset += 10

        yield scrapy.Request(''.join([self.url, str(self.offset)]), callback = self.parse)
