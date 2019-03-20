#coding=utf-8
__author__ = 'zs'
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1', 'http://quotes.toscrape.com/page/2']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        print(page)
        filename = 'quotes-%s.html' % page
        with open(filename) as f:
            f.write(response.body)
            self.log('saved file %s' % filename)
