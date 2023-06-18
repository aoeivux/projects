# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    # 电影名字
    movieNAME = scrapy.Field()
    # 电影URL
    movieURL = scrapy.Field()
    # 电影类型
    movieTYPE = scrapy.Field()
    # 最后更新时间
    movieUPDATE = scrapy.Field()
