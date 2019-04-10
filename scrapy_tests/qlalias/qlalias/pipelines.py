# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class QlaliasPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        file_name = 'd:/' + today + '.csv'
        lst = []
        steam_id = item['steam_id'] if item['steam_id'] is not None else '-'
        #nick = item['nick'] if item['nick'] is not None else '-'
        #joined = item['joined'] if item['joined'] is not None else '-'
        aliases = item['aliases'] if item['aliases'] is not None else '-'
        lst.append(steam_id + '\t')
        #lst.append(nick)
        #lst.append(joined)
        lst.append(aliases)
        line = ','.join(lst) + '\n'
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(line)

        return item
