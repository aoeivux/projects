import scrapy


class HongniuziyuanSpider(scrapy.Spider):
    name = "hongniuziyuan"
    allowed_domains = ["hongniuziyuan.com"]
    start_urls = ["https://hongniuziyuan.com"]

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # 数据解析
    def parse(self, response):
        print("开始解析网页中的数据")
        pass
        print("解析结束")
