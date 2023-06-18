# -*- coding: utf-8 -*-
import scrapy




class HongniuSpider(scrapy.Spider):
    #爬虫的名字
    name = "hongniu"
    #爬虫需要爬取的网址
    allowed_domains = ["www.hongniuziyuan.com"]
    #爬虫的入口
    start_urls = ["https://www.hongniuziyuan.com"]

    #发起请求
    def start_requests(self):
        #有规则的网址
        urls=[]
        for pagenum  in range(1,581):
            urls.append(f'https://www.hongniuziyuan.com/index.php/vod/type/id/SCCCCS/page/{pagenum}.html?ac=detail')

        #没有规则网址
        # urls = [
        #     "https://www.hongniuziyuan.com/index.php/vod/type/id/SCCCCS/page/1.html?ac=detail",
        # ]
        for url in urls:
            #爬取到数据之后 交给当前爬虫中parse来解析
            yield scrapy.Request(url=url, callback=self.parse)


    #数据解析  LXML  XPATH
    def parse(self, response):
        print('开始解析网页中数据')

        #print(response.body)  #网页的全部源代码
        #提取我们感兴趣的数据
        #css选择器  HTML  CSS  JavaScript
        #<div id='free'>      #free  id选择器
        #<div class="free">   .free  类选择
        #<div></div>          div  标签选择器
        #并集选择器
        #兄弟选择器
        #标签是2个 属性::attr(href)  正文::text
        hrefs= response.css('div.xing_vb>ul>li>span.xing_vb4>a::attr(href)').getall()
        titles = response.css('div.xing_vb>ul>li>span.xing_vb4>a::text').getall()
        types = response.css('div.xing_vb>ul>li>span.xing_vb5::text').getall()
        print(types)
        updatetimes = response.css('div.xing_vb>ul>li>span.xing_vb7::text').getall()
        print(updatetimes)
        movieList=[]
        for x in zip(hrefs,titles,types,updatetimes):
           movieinfo={
            '电影名字':x[1],
            '电影URL':x[0],
            '电影类型':x[2],
            '最后更新时间':x[3]
           }
           movieList.append(movieinfo)

        # href=response.xpath('//strong').getall()
        # print(href)
        print('网页解析结束')
        return movieList
        #

    #执行爬虫
    # scrapy  crawl  爬虫的名字
    # scrapy  crawl  hongniu  执行名字叫做hongniu的爬虫
    # scrapy  crawl  hongniu  -o  hongniu.csv 爬取数据并输出到csv的文件中
    # scrapy  crawl hongniu  -o   hongniu.json  爬取数据并输出到json格式的文件中
    # scrapy  crawl hongniu  -o   hongniu.xml  爬取数据并输入到xml格式的文件中

    #保存我们爬取数据
    #下一步我们就是要保存的我们数据  Excel MySQL CSV  Pandas XML  JSON
    #
