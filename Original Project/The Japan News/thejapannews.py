import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TheJapanNewsSpider(CrawlSpider):
    name = 'TheJapanNews'
    allowed_domains = ['the-japan-news.com']
    start_urls = ['https://the-japan-news.com/']

    custom_settings = {
        'DOWNLOAD_DELAY' : 2,
    }


rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

def parse_item(self, response):
        yield{
           'category': response.xpath('//*[@id="newsSubgenreListWrapper"]/section/header/h1/text()').getall(),
           'category2': response.css('.headline::text').getall(),
            'article title': (response.xpath('//h1/text()').getall()),
            'summary': (response.xpath('//p/text()').getall())
            }



            ##editedListWrapper > div > section > ul > li.newListItem.news.photoNone.out1.masonry-brick.lt > article > a > div > header > h1 > span
            ##editedListWrapper > div > section > ul > li.newListItem.news.photoIs.horizontal.out2.masonry-brick.rt > article > a > div.vCol.block1 > header > h1 > span