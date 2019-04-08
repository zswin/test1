# -*- coding: utf-8 -*-
import scrapy
from ..items import QlaliasItem
import time
from datetime import datetime

class SpdrAliasSpider(scrapy.Spider):
    name = 'spdr_alias'
    allowed_domains = ['qlstats.net']
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S UTC'

    num = 0
    all_players = []
    with open('d:/list.txt', encoding='utf-8') as f:
        for line in f.readlines():
            lst = line.split(',')
            sid = lst[0]
            all_players.append(sid)
    start_urls = ['https://qlstats.net/aliases/{}'.format(all_players[0])]

    def parse(self, response):
        item = QlaliasItem()
        item['steam_id'] = response.xpath("//div[@class='row']//div[@class='col-xs-12']/a/text()").extract_first()
        alst = []
        aliases = response.xpath("//div[@class='row']//tbody/tr")
        for a in aliases:
            als = a.xpath("./td").extract()
            for tmp in als:
                if 'tdcenter' in tmp:
                    continue
                tmp = tmp.replace("<td>", "").replace("</td>", "").replace("</span>", "")
                tmp = tmp.replace('<span class="ql1">', '')
                tmp = tmp.replace('<span class="ql2">', '')
                tmp = tmp.replace('<span class="ql3">', '')
                tmp = tmp.replace('<span class="ql4">', '')
                tmp = tmp.replace('<span class="ql5">', '')
                tmp = tmp.replace('<span class="ql6">', '')
                tmp = tmp.replace('<span class="ql7">', '')
                tmp = tmp.replace('<span class="ql8">', '')
                tmp = tmp.replace('<span class="ql9">', '')
                if tmp is not None:
                    alst.append(tmp)
        item["aliases"] = '，'.join(alst)

        yield item

        if self.num < len(self.all_players):
            self.num += 1
            new_url = "https://qlstats.net/aliases/{}".format(self.all_players[self.num])
            yield scrapy.Request(url=new_url, callback=self.parse)
