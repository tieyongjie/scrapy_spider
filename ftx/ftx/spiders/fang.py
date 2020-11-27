# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import NewHouseItem, ESFHosuseItem


class FangSpider(RedisSpider):
    name = 'fang'
    allowed_domains = ['fang.com']
    # start_urls = ['http://fang.com/']
    redis_key = 'fang:urls'

    # https://www.fang.com/SoufunFamily.html

    def parse(self, response):
        trs = response.css('.outCont tr')
        province = None
        for tr in trs:
            # tr 标签里面提取省份

            # 如果 tr 省份标签,就用上一个的 tr
            pro = tr.css('td[valign="top"] strong::text').get()
            # 不清楚自己写的对不 写完之后一起进行测试
            if pro:
                # 如果是有内容的
                # 防止省份是空格 pro 出去两端空格之后 还有内容就修改省份
                if pro.strip():
                    province = pro

            # 海外的页面结构不一样
            if province == "其他":
                continue

            city_a = tr.css("td a")
            for city in city_a:
                # 城市名与城市网址
                city_name = city.css('a::text').get()
                city_link = city.css('a::attr(href)').get()
                # 分析每一个城市的请求
                yield scrapy.Request(city_link,
                                     callback=self.parsel_city,
                                     meta={
                                         'province': province,
                                         'city_name': city_name
                                     })

    def parsel_city(self, response):
        """过程 新房 二手房"""
        new_house_url = response.css('#dsy_D04_01::attr(href)').get()
        print(new_house_url, 'new_house_url')
        yield scrapy.Request(new_house_url,
                             meta=response.meta,
                             callback=self.parse_new_house)
        old_house_url = response.css('#dsy_D05_01::attr(href)').get()
        print('old_house_url', old_house_url)
        yield scrapy.Request(old_house_url,
                             meta=response.meta,
                             callback=self.parse_old_house)

    def parse_new_house(self, response):
        province = response.meta.get("province")
        city = response.meta.get("city")
        # print(response.text)
        lis = response.css("div.nl_con ul li")
        for li in lis:
            name = li.css(".nlcd_name>a::text").get()
            if name:
                name = name.strip()
            print(name)
            house_type_list = li.css(".house_type a::text").getall()
            area = ''.join(li.css(".house_type::text").re('[\d~平米]+'))
            print(area)
            address = li.css(".address a::attr(title)").get()
            print(address)
            district = li.css(".address a span::text").get()
            if district:
                district = district.strip()
            print(district)
            sale = li.css(".nhouse_price span::text").get()
            em = li.css(".nhouse_price em::text").get()
            if sale and em:
                sale = sale + em
            print(sale)
            origin_url = li.css(".nlcd_name a::attr(href)").get()
            if origin_url:
                origin_url = 'https:' + origin_url
            print(origin_url)
            item = NewHouseItem(
                province=province, city=city, name=name, room=house_type_list, area=area, district=district,
                sale=sale,
                origin_url=origin_url,
            )
            yield item
        next_url = response.css('next::attr(href)').get()
        if next_url:
            next_url = response.urljoin(next_url)
            # print(next_url)
            yield scrapy.Request(url=next_url,
                                 callback=self.parse_new_house,
                                 meta={"province": province, "city": city},
                                 dont_filter=True)

    def parse_old_house(self, response):
        print(response.url)
        # print(response.text)
        province = response.meta.get("province")
        city = response.meta.get("city")
        # print(province)
        dls = response.css(".shop_list_4 dl")
        for dl in dls:
            # print(dl)
            title = dl.css(".tit_shop::text").get()
            print(title)
            rooms = dl.xpath("./dd[1]/p[1]//text()").re('\S+')
            rooms = ''.join(rooms)
            print(rooms)
            name = dl.css(".add_shop a::text").re('\S+')
            print(name)
            address = dl.css(".add_shop span::text").get()
            print(address)
            origin_url = dl.css("h4 a::attr(href)").get()
            if origin_url:
                origin_url = response.urljoin(origin_url)
            print(origin_url)
            Item = ESFHosuseItem(province=province, city=city, rooms=rooms, name=name, address=address,
                                 origin_url=origin_url)
            yield Item
        # 使用xpath指定位置提取内容
        next_url = response.xpath("//div[@class='page_al']/p[3]/a/@href").get()

        # 如果是增量爬虫
        if next_url == None:
            next_url = response.xpath("//div[@class='page_al']/p[1]/a/@href").get()
        next_url = response.urljoin(next_url)
        print(next_url)

        yield scrapy.Request(url=next_url, callback=self.parse_old_house, meta={"info": (province, city)},
                             dont_filter=True)
