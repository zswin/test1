# -*- coding: utf-8 -*-
import scrapy
from ..items import QlstatsItem
import time

class SpdrQlstatsSpider(scrapy.Spider):
    name = 'spdr_qlstats'
    allowed_domains = ['qlstats.net']
    start_urls = ['https://qlstats.net/ranks/ca/1']
    prefix = "https://qlstats.net"
    page = 1
    page_url = "https://qlstats.net/ranks/ca/1?page={}"

    def parse(self, response):
        items = []
        sel = response.xpath("//div[@class='row']//tbody/tr")
        for sub in sel:
            item = QlstatsItem()
            item['rank'] = sub.xpath("./td[1]/text()").extract_first()
            item['href'] = self.prefix + sub.xpath("./td[2]/a/@href").extract_first()
            item['nick'] = sub.xpath("./td[2]/a/span[@class='ql7']/text()").extract_first()
            item["glicko"] = sub.xpath("./td[3]/text()").extract_first().replace(' ± ', '+-')
            item["games"] = sub.xpath("./td[4]/text()").extract_first()
            item["region"] = ""
            item["player_id"] = ""
            item["steam_id"] = ""
            item["joined"] = ""
            item["status"] = ""
            item["win_rate"] = ""
            item["kill_ratio"] = ""
            item["aliases"] = ""
            # get detail info
            if item["href"] is not None:
                time.sleep(1)
                yield scrapy.Request(item['href'], meta={'item':item}, callback=self.detail_parse)
            else:
                yield item

        if self.page <= 84:
            self.page += 1
            new_page_url = self.page_url.format(self.page)
            time.sleep(1)
            yield scrapy.Request(url=new_page_url, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta["item"]
        lst = response.xpath("//div[@class='row']//p/text()").extract()
        private = response.xpath("//div[@class='row']//div[@class='col-xs-6 xol-sm-8 col-md-9']/text()").extract_first()
        item["player_id"] = lst[1].replace('\n      ', '').replace('Player ID:', '')
        item["steam_id"] = response.xpath("//div[@class='row']//p/a/text()").extract_first() + '\t'
        item["status"] = lst[6].replace('\n', '').replace(' ', '').replace('Status:', '')
        if private is None:
            item["region"] = lst[0].replace('\n      ', '').replace('Region:', '')
            item["player_id"] = lst[1].replace('\n      ', '').replace('Player ID:', '')
            item["steam_id"] = response.xpath("//div[@class='row']//p/a/text()").extract_first() + '\t'
            item["joined"] = response.xpath("//div[@class='row']//p/span/@title").extract_first().replace(',','/')
            item["status"] = lst[6].replace('\n','').replace(' ','').replace('Status:', '')
            item["win_rate"] = response.xpath("//div[@id='gbtabcontainer']//div[@id='tab-overall']/div/small/text()")\
                .extract_first().replace(',','/')
            item["kill_ratio"] = response.xpath("//div[@id='gbtabcontainer']/div[@id='tab-overall']/div/small[2]/text()")\
                .extract_first().replace(',','/')
#
        return item
