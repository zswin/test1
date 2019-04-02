# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QlstatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    nick = scrapy.Field()
    glicko = scrapy.Field()
    games = scrapy.Field()
    region = scrapy.Field()
    player_id = scrapy.Field()
    steam_id = scrapy.Field()
    joined = scrapy.Field()
    status = scrapy.Field()
    win_rate = scrapy.Field()
    kill_ratio = scrapy.Field()
    href = scrapy.Field()
    aliases = scrapy.Field()
