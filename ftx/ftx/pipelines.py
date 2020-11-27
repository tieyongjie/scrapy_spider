# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from .items import NewHouseItem, ESFHosuseItem


class MonGoDBPipeline:

    def __init__(self):
        self.client = pymongo.MongoClient(
            host='49.233.35.5',
            port=27017,
            username='ubuntu',
            password='951028'
        )
        self.collection = self.client.test
        self.new_house = self.collection.new_house
        self.old_house = self.collection.old_house

    def process_item(self, item, spider):
        if isinstance(item, NewHouseItem):
            self.new_house.insert(dict(item))
        elif isinstance(item, ESFHosuseItem):
            self.old_house.insert(dict(item))
        return item

    def close_spider(self):
        self.client.close()
