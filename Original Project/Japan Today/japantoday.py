import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JapantodaySpider(CrawlSpider):
    name = 'japantoday'
    allowed_domains = ['japantoday.com']
    start_urls = ['https://japantoday.com/']

    custom_settings = {
        'DOWNLOAD_DELAY' : 2,
    }

rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body'), callback='parse_item', follow=True),
    )

def parse_item(self, response):
        yield{  'category': response.xpath('//a[@class="section-title-inner text-color"]/a/text()').getall(),
           'category2': response.xpath('//a[class="text-primary text-uppercase text-small text-strong"]/a/text()').getall(),
            'article title': (response.xpath('//h2/text()').getall()),
            'article title 2': (response.xpath('//h4/text()').getall()),
            'article title 3': (response.xpath('//h3/text()').getall()),
            }
