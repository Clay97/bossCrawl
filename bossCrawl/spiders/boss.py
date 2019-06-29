# -*- coding: utf-8 -*-
import scrapy
from bossCrawl.items import BosscrawlItem
from urllib.parse import quote
class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    base_url = 'http://zhipin.com'


    def start_requests(self):
        for job in self.settings.get('QUERY'):
            for code in self.settings.get('CITY_CODE'):
                url ='https://www.zhipin.com/c'+code+'/?query='+quote(job)+'&page=1'
                print(url)
                yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        #提取职位列表
        jobs = response.xpath("//div[@class='job-primary']").extract()
        #遍历职位列表，提取信息
        for job in jobs:
            positionitem = BosscrawlItem()
            info = scrapy.Selector(text=job)
            positionitem['position'] =info.xpath("//div[@class='job-title']/text()").extract_first()
            positionitem['salary'] = info.xpath("//span[@class='red']/text()").extract_first()
            info_primary = info.xpath("//div[@class='info-primary']/p/text()").extract()
            positionitem['place'] = info_primary[0]
            positionitem['education']  =info_primary[-1]
            positionitem['require'] = info_primary[1]
            if len(info_primary)==4:
                positionitem['require']=info_primary[1]+' '+info_primary[2]
            positionitem['company'] = info.xpath("//div[@class='company-text']/h3/a/text()").extract_first()
            info_company = info.xpath("//div[@class='company-text']/p/text()").extract()
            positionitem['type'] = info_company[0]
            positionitem['scale'] = info_company[-1]
            positionitem['stage']=''
            if len(info_company)==3:
                positionitem['stage']=info_company[1]
            yield positionitem
        #提取url
        urls =response.xpath("//div[@class='page']/a/@href").extract()
        for url in urls[1:]:
            if 'javascript'in url:
                continue
            item = 'https://www.zhipin.com'+url
            yield scrapy.Request(url=item,callback=self.parse)

