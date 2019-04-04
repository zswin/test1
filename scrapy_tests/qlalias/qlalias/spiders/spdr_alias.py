# -*- coding: utf-8 -*-
import scrapy
from ..items import QlaliasItem
import time
from datetime import datetime

class SpdrAliasSpider(scrapy.Spider):
    name = 'spdr_alias'
    allowed_domains = ['qlstats.net']
    start_urls = ['https://qlstats.net/players?page=6920']

    base_url = "https://qlstats.net/players?page={}"
    page_num = 6920
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S UTC'
    def parse(self, response):
        items = []
        sel = response.xpath("//div[@class='row']//tbody/tr")
        for sub in sel:
            item = QlaliasItem()
            item['player_id'] = sub.xpath("./td/text()").extract_first()
            item['nick'] = sub.xpath("./td//span[@class='ql7']/text()").extract_first()
            if item['nick'] == 'Anonymous':
                continue
            else:
                print(item['nick'], ' of ', self.page_num)
            tmp = sub.xpath("./td[3]/span/@title").extract_first()
            tmp = datetime.strptime(tmp, self.GMT_FORMAT).strftime("%Y-%m-%d %H:%M:%S")
            item["joined"] = tmp
            sid_url = "https://qlstats.net/player/" + item['player_id']
            yield scrapy.Request(url=sid_url, meta={"item":item}, callback=self.sid_parse)

        if self.page_num <= 10774:
            self.page_num += 1
            new_url = self.base_url.format(self.page_num)
            time.sleep(1)
            yield scrapy.Request(url=new_url, callback=self.parse)


    def sid_parse(self, response):
        item = response.meta["item"]
        sid = response.xpath("//div[@class='row']/div[@class='col-xs-6 col-sm-4 col-md-3']//p//a/text()").extract_first()
        item["steam_id"] = sid
        alias_url = "https://qlstats.net/aliases/{}".format(sid)
        yield scrapy.Request(url=alias_url, meta={"item":item}, callback=self.alias_parse)

    def alias_parse(self, response):
        item = response.meta["item"]
        alst = []
        aliases = response.xpath("//div[@class='row']//tbody/tr")
        for a in aliases:
            alias = a.xpath("./td/span/text()").extract_first()
            if alias is not None:
                alst.append(alias)
        item["aliases"] = '，'.join(alst)

        return item
