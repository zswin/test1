# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class QlstatsPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        file_name = 'd:/' + today + '.csv'
        lst = []

        lst.append(item['rank'] if item['rank'] is not None else '-')
        lst.append((item['nick'] if item['nick'] is not None else '-') + ' ')
        lst.append(item['glicko'] if item['glicko'] is not None else '-')
        lst.append(item['games'] if item['games'] is not None else '-')
        lst.append(item['region'] if item['region'] is not None else '-')
        lst.append(item['player_id'] if item['player_id'] is not None else '-')
        lst.append(item['steam_id'] if item['steam_id'] is not None else '-')
        lst.append(item['joined'] if item['joined'] is not None else '-')
        lst.append((item['status'] if item['status'] is not None else '-').replace('the',''))
        lst.append((item['win_rate'] if item['win_rate'] is not None else '-'))
        lst.append(item['kill_ratio'] if item['kill_ratio'] is not None else '-')
        lst.append(item['href'] if item['href'] is not None else '-')
        line = ','.join(lst) + '\n'
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(line)
        return item
