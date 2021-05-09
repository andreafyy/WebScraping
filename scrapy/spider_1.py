# -*- coding: utf-8 -*-
# Importing Libraries
import scrapy

# Declaring scrapy class
class Link(scrapy.Item):
    link = scrapy.Field()

# Actual program
class LinkListsSpider(scrapy.Spider):
    # Name of spider
    name = 'links'

    # Allowed domains and starting URL
    allowed_domains = ['https://www.rottentomatoes.com/']
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/']

    # Scrapy parser
    def parse(self, response):
        xpath = "//td[3]/a[@class = 'unstyled articleLink']/@href"
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.rottentomatoes.com/' + s.get()
            yield l