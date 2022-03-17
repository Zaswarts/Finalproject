from attr import attr
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Jptimes3Spider(CrawlSpider):
    name = 'jptimes3'
    allowed_domains = ['japantimes.co.jp']
    start_urls = ['https://www.japantimes.co.jp/']

    custom_settings = {
        'DOWNLOAD_DELAY' : 1,
    }

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@data-tb-region="Top News"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="wrapper"]/section[1]/div/div[2]/div[2]/div[3]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="wrapper"]/section[2]/div[1]'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        yield{
           'category': response.xpath('//h3[@class="single-post-categories"]/a/text()').getall(),
           'category2': response.xpath('//*[@id="wrapper"]/section[2]/div[1]/section[4]/div/div[2]/a/article/header/hgroup/h3/a/text()').getall(),
            'article title': (response.xpath('//h1/text()').getall()),
            'article title 2': (response.xpath('//p/text()').getall())
            }
        
        
