# -*- coding: utf-8 -*-
import scrapy
class PspiderSpider(scrapy.Spider):
    name = 'pspider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org']

    def parse(self, response):
        for p in response.xpath("//div"):
            x = p.xpath("./p/a[contains(@style, 'font')]").extract()
            if x != []:
                '''print(p.xpath("./p/a[contains(@style, 'font')]/b/text()").extract_first())
                print(p.xpath("./p[contains(@class, 'source')]/a/text()").extract_first())
                print(p.xpath("./p[contains(@class, 'source')]/a[contains(@href, 'https')]/text()").extract_first())
                print(p.xpath("./div[contains(@class, 'contson')]/text()").extract())
                '''
                title = p.xpath("./p/a[contains(@style, 'font')]/b/text()").extract_first()
                dyna = p.xpath("./p[contains(@class, 'source')]/a/text()").extract_first()
                author = p.xpath("./p[contains(@class, 'source')]/a[contains(@href, 'https')]/text()").extract_first()
                poet = p.xpath("./div[contains(@class, 'contson')]/text()").extract()
                yield {
                    'title':title,
                    'dyna':dyna,
                    'author':author,
                    'poet':poet
                }
        next_page_url = response.xpath("//a[contains(@id, 'amore')]/@href").extract_first()
        #next_page_url = self.start_urls[0] + next_page_url
        if next_page_url is not None:
            print(next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))
