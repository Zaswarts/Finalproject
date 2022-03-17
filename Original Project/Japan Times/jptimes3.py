from attr import attr
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Jptimes3Spider(CrawlSpider):
    name = 'jptimes3'
    allowed_domains = ['japantimes.co.jp']
    start_urls = ['https://www.japantimes.co.jp/']

    custom_settings = {
        'DOWNLOAD_DELAY' : 3,
    }

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id="page"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'category' : response.css('h3 > span.category-column::text').getall(),
            'category2' : response.css('h3.category-column::text').getall(),
            'article title' : response.css('p.article-title::text').getall(),
            'summary' : response.xpath('//*[@id="wrapper"]/section[2]/div[1]/section[4]/div/ul/li[4]/a/article/header/hgroup/p/text()').getall()
            }
        
        
