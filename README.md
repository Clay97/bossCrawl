# bossCrawl
抓取boss直聘热门城市有关爬虫的职位信息，最终将数据存储在mongo数据库中。  
职位信息包括职位名称，薪水，公司地点，需求（工作经验或工作时长），学历要求，公司名称，公司类型，融资阶段，公司规模.  
如果你想抓取其他职位信息，你需要在**setting.py**中的**QUERY**字段中添加你所希望抓取的职位。  
如果你想抓取其他城市的相关工作，你需要在**setting.py**中的**CITY_CODE**字段中添加城市代码。访问 https://www.zhipin.com/wapi/zpCommon/data/city.json 查看城市代码。

