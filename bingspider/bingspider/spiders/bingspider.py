#! /usr/bin/python3


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import Spider
from bingspider.items import Article

class ArticleSpieder(Spider):
    name="article"
    allowed_domain = ["cn.bing.com"]
    start_urls = ["https://cn.bing.com"]
    
    def parse(self, response):
        item = Article()
        item['title'] = response.xpath('//h1/text()').extract()
        item['link'] = response.xpath('//a/@href	').extract()
        return item

    
