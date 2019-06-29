# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json

#存储到本地
class BosscrawlPipeline(object):
    def __init__(self):
        self.file = open('boss.txt', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        f = json.dumps(dict(item))+'\n'
        self.file.write(f)
        return item

    def close_spider(self,spider):
        self.file.close()

#存储到mongo数据库中
class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    def process_item(self, item, spider):
        self.db['position'].insert(dict(item))
        return item

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB','jd')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

