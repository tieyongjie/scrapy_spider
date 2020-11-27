import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import Maoyan100Item


class MaoyanSpider(RedisSpider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    # start_urls = [f'https://maoyan.com/board/4?offset={i}' for i in range(0, 10)]
    def start_requests(self):
        for i in range(1, 11):
            url = f'https://maoyan.com/board/4?offset={i}'
            yield scrapy.Request(url=url, callback=self.parse
                                 )

    def parse(self, response):
        dds = response.css('.content dd')
        item = Maoyan100Item()
        for dd in dds:
            item['name'] = dd.css('.name a::text').get()
            item['star'] = dd.css('.star::text').get().split()[0]
            integer = dd.css('.integer::text').get()
            fraction = dd.css('.fraction::text').get()
            item['score'] = integer + fraction
            item['releasetime'] = dd.css('.releasetime::text').get()
            yield item
