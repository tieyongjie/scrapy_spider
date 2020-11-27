# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pymongo
import redis
import json
import pymysql
from openpyxl import Workbook
import csv


class Maoyan100Pipeline:
    def __init__(self):
        self.file = open('猫眼100.txt', mode='a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item['name'] + ',' + item['star'] + item['score'] + item['releasetime'] + '\n')
        return item

    def close_item(self):
        self.file.close()


class MonGoDBPipeline:

    def __init__(self):
        self.client = pymongo.MongoClient(
            host='49.233.35.5',
            port=27017,
            username='ubuntu',
            password='951028'
        )
        self.collection = self.client.test
        self.maoyan = self.collection.maoyan

    def process_item(self, item, spider):
        self.maoyan.insert(dict(item))
        return item

    def close_spider(self):
        self.client.close()


class RedisPipeline(object):

    def __init__(self):
        # 初始化链接redis
        self.redis_cli = redis.Redis(
            host='49.233.35.5',
            password='123456',
            port=6379,
            db=1,
        )

    def process_item(self, item, spider):
        # 保存到redis
        self.redis_cli.lpush('maoyan', json.dumps(dict(item), ensure_ascii=False))
        return item

    def close_spider(self, spider):
        self.redis_cli.close()


class ExcelPipeline(object):
    # 调用__init__()方法构造对象
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['name', 'star', 'score', 'releasetime'])

    def process_item(self, item, spider):
        self.ws.append([item['name'], item['star'], item['score'], item['releasetime']])
        return item

    def __del__(self):
        # 调用__del__() 销毁对象，释放其空间
        self.wb.save('猫眼100.xlsx')



class MySQLPipeline(object):
    """
    create database quotes charset=utf8;
    use quotes;
    create table quotes (txt text, author char(20), tags char(200));
    """

    def __init__(self):
        self.connect = pymysql.connect(
            host='49.233.35.5',
            port=3306,
            db='maoyan100',  # 数据库名
            user='ubuntu',
            passwd='123456',
            charset='utf8',
            use_unicode=True
        )
        # 创建操作数据的游标
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 保存到mysql
        # 执行sql语句
        sql = "insert into maoyan100(title, star, score, releasetime) value(%s, %s, %s, %s)"
        self.cursor.execute(sql, (item['name'], item['star'], item['score'], item['releasetime'])
        )
        # 提交数据执行数据
        self.connect.commit()
        return item

    # 关闭链接
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

