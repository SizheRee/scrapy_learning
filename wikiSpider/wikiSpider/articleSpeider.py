#! /usr/bin/python3


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import Spider
from wikiSpider.items import Article
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpieder(Spider):
    name="article"
    allowed_domain = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
    "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
                  callback="parse_item", follow=True)]

    
    def parse_item(self, response):
        item = Article()
        item['title'] = response.xpath('//h1/text()')[0].extract()
        item['link'] = response.xpath('//a/@href').extract()
        return item

    
