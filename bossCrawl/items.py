# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosscrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    position = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    #公司地点
    place = scrapy.Field()
    #需求
    require = scrapy.Field()
    #学历要求
    education = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #公司类型
    type = scrapy.Field()
    #融资阶段
    stage = scrapy.Field()
    #公司规模
    scale = scrapy.Field()
