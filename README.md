# bossCrawl
抓取boss直聘热门城市有关爬虫的职位信息，最终将数据存储在mongo数据库中。  
职位信息包括职位名称，薪水，公司地点，需求（工作经验或工作时长），学历要求，公司名称，公司类型，融资阶段，公司规模.  
如果你想抓取其他职位信息，你需要在**setting.py**中的**QUERY**字段中添加你所希望抓取的职位。  
```
QUERY ={'爬虫'}
```
如果你想抓取其他城市的相关工作，你需要在**setting.py**中的**CITY_CODE**字段中添加城市代码。访问 https://www.zhipin.com/wapi/zpCommon/data/city.json 查看城市代码。  
```
CITY_CODE ={'101010100','101020100','101280100','101280600','101210100','101030100','101110100','101190400','101200100','101230200','101250100','101270100','101180100','101040100'}

```
此外你如果你没有安装mongo数据库，还可以将书库库存储在本地，在**setting.py**中进行如下设置：
```
ITEM_PIPELINES = {
    'bossCrawl.pipelines.MongoPipeline': 300,
    #'bossCrawl.pipelines.BosscrawlPipeline': 300,
}
```
