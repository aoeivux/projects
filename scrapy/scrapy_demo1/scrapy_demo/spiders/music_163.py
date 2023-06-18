import scrapy


class Music163Spider(scrapy.Spider):
    name = "music_163"
    allowed_domains = ["music.163.com"]
    start_urls = ["https://music.163.com"]

    def parse(self, response):
        pass
