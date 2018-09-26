#coding=utf-8
__author__ = 'zs'
import scrapy
'''version1
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1', 'http://quotes.toscrape.com/page/2']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        print('-'*10)
        filename = 'd:/zs/test1/scrapy/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' % filename)
'''
'''version 2
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract()

            }
'''
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com/page/1']

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract()
                }
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
#            next_page = response.urljoin(next_page)
#            yield scrapy.Request(next_page, callback = self.parse)

