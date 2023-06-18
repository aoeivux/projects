import scrapy
import random

from ..items import MovieItem

class HongniuziyuanSpider(scrapy.Spider):
    name = "hongniuziyuan"
    allowed_domains = ["hongniuziyuan.com"]
    start_urls = ["https://hongniuziyuan.com"]
    start = 1
    end = 52


    def start_requests(self):
        start_num =self.start
        end_num = self.end
        if start_num is None:
            start_num = 1
        if end_num is None:
            end_num = 10
        # print(start_num)
        # print(end_num)
        urls = []
        #请大家根据实际的情况来修改我们的分页的数据 测试一般前2页就可以 如果正式爬取的话，页码要多一些
        for i in range(int(start_num),int(end_num)):
            urls.append(f'https://www.hongniuziyuan.com/index.php/index/index/page/{i}.html?ac=detail')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movieNames= response.css('div.xing_vb>ul>li>span>a::text').getall()
        movieLinks = response.css('div.xing_vb>ul>li>span>a::attr(href)').getall()
        movieTypes=response.css('div.xing_vb>ul>li>span.xing_vb5::text').getall()
        movieUpdates=response.css('div.xing_vb>ul>li>span.xing_vb7::text').getall()
        #,movieLinks,movieTypes,movieUpdates
        for  x in zip(movieNames,movieLinks,movieTypes,movieUpdates):
            link=response.urljoin(x[1])
            # print(link)
            yield scrapy.Request(url=link, callback=self.parse2)

    #如果获取的列表的数据存在数据的话，获取第一个,如果没有的话 就是空字符串
    def  convert(self,list):
        if len(list)>0:
            return list[0]
        else:
            return ''

    #如果获取的列表的数据存在数据的话，获取第一个,如果没有的话 就是空字符串
    def  convertList(self,list):
         return ','.join(list)

    def parse2(self,response):
       #电影名称
       movieName = response.css('div.warp>div:nth-child(1)>div>div>div>img::attr(alt)').getall()
       #电影海报
       paper=response.css('div.warp>div:nth-child(1)>div>div>div>img::attr(src)').getall()
       #别名
       otherName= response.css("div.vodinfobox>ul>li:nth-child(1)>span::text").getall()
       #电影的评分
       score=response.css('div.vodh>label::text').getall()

       director = response.css("div.vodinfobox>ul>li:nth-child(2)>span::text").getall()
       actor = response.css("div.vodinfobox>ul>li:nth-child(3)>span::text").getall()
       types = response.css("div.container>div>dl>dd::text").getall()
       area = response.css("div.vodinfobox>ul>li:nth-child(5)>span::text").getall()
       language = response.css("div.vodinfobox>ul>li:nth-child(6)>span::text").getall()
       showtime = response.css("div.vodinfobox>ul>li:nth-child(7)>span::text").getall()
       updatetime = response.css("div.vodinfobox>ul>li:nth-child(8)>span::text").getall()
       content = response.css("div.vodplayinfo::text").getall()
       playlist01 = response.css("div#play_1>ul>li>a::attr(href)").getall()
       playlist02 = response.css("div#play_2>ul>li>a::attr(href)").getall()

       movie=MovieItem()
       movie['mname']=self.convert(movieName)
       movie['paper']=self.convert(paper)
       movie['score']=self.convert(score)
       movie['box_office']=str((round(random.uniform(0, 10), 2)))
       movie['popularity']=str((round(random.uniform(0, 10), 2)))
       movie['other_name']=self.convert(otherName)
       movie['director'] = self.convert(director)
       movie['actor'] = self.convert(actor)
       #这里的类型有问题-begin
       movie['type'] = self.convert(types).split('/')[0].replace(' ','')
       # 这里的类型有问题-end
       movie['area'] = self.convert(area)
       movie['language'] = self.convert(language)
       movie['show_time'] = self.convert(showtime)
       movie['update_time'] = self.convert(updatetime)
       movie['content']=self.convert(content)
       movie['playlist01'] =self.convertList(playlist01)
       movie['playlist02']=self.convertList(playlist02)
       print(score)
       print(paper)
       print(movieName)
       print(types)
       print(area)
       print(language)
       print(showtime)
       print(updatetime)
       print(content)
       print(playlist01)
       print(playlist02)
       print(otherName)
       print(director)
       print(actor)
       yield movie

