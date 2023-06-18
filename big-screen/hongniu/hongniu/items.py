# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    mname = scrapy.Field()
    paper = scrapy.Field()
    score = scrapy.Field()
    box_office =scrapy.Field()
    popularity =scrapy.Field()
    other_name = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    show_time = scrapy.Field()
    update_time = scrapy.Field()
    content = scrapy.Field()
    playlist01 = scrapy.Field()
    playlist02 = scrapy.Field()
