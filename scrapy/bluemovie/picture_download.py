#1.发起请求
#2.解析我们页面
#3.存储数据   保存到我mysql数据库中
#4.使用pyqt 做一个查询界面  专门用来查找电影的网盘地址
import requests
from lxml import etree

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"图片已成功保存为 {filename}")
    else:
        print("下载图片时出错")


if __name__ == '__main__':
    site='https://www.zhihu.com/question/266744006'
    website='https://www.4khdr.cn/'
    #模拟浏览器携带数据
    #如何将我们爬虫程序伪装为浏览器
    headers={}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    headers['Accept-Encoding'] = 'gzip, deflate, br'
    headers['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'

    headers['Cookie'] = '__snaker__id=ulDhfS22y5yFNtix; SESSIONID=dIGp5XFttw36fONs7uunqwBaNRsgAhnotELIWKYbm0M; JOID=V1oRC0gA24LVgaI8cw0qWxkIQc1kJP6t_aSGGVwl_6f6qYcYVh46C7yAozZ0pyRjgOSEh7-wLKqKWzyk0BTlf4k=; osd=UFkTBUgH2IDbgaU_cQMqXBoKT81jJ_yj_aOFG1Il-KT4p4cfVRw0C7uDoTh0oCdhjuSDhL2-LK2JWTKk1xfncYk=; _zap=eb52ab3c-967d-41d9-8975-bbaeb3d4986f; d_c0=AOCYyWhp6xaPTgTsWzgQ8WuLJ7055bS-x48=|1686535337; YD00517437729195%3AWM_TID=8YnEtXEeXPdEABVRVUfV1PUabaEaYKfC; _xsrf=790ec492-2db7-459e-ba22-38c67eb3aac9; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1686535339,1686904180,1687087902; YD00517437729195%3AWM_NI=tEbXsSmEbeNK3N87AnYHTftnPxg5ilouqG9qZWi5JqQj6AQgcC8bkV0ewr8bZRaZ3stG0F2y0Tf2hmZEXE0TqPNiCUuOFcvsiLUKXKV6FTlCfLBLMrwdJqU1P7BefQS%2BbTM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeafcd5bfb9ab68cb2708b8e8eb6c15a878b8facd43ca698bcbbc73bb7e7ab8fce2af0fea7c3b92ab89baeb9f259af9bae86cd41f192f8d8c4669b989c87f76694a8a9d6ec68adabbfa8bc7b9a89a7d6c97b93b6faa2d46da19df883ea5ef4bbb993bb6a9a8eafbbb279b89900a7b173f48caad3eb679a9b98a6b360b390828ac25fb7918a84f579ab949bacdb4196ea8ab5ef49a6948eadd07ab5bc8692d83b94e98e86e55b91f5aeb5d037e2a3; gdxidpyhxdE=5OK7eqVg8pCSVs00nhEigsggXBC%2BK16%5CvOUGjX6vrIVDr1wZp4JHO0PUCY%5C7WLDK1hYM%5CdM%2Bdas6jQ7dByvTj3ZJ3g2b6LukC%5Cxhy1gSpoBqLwWghYIu2vBG0SHNLu3Y2ysLuBN4S%2B3liDbJUXWGX%2B7dRMye7bmrYyUwJUOzGagjdNyM%3A1687089645652; captcha_session_v2=2|1:0|10:1687088749|18:captcha_session_v2|88:SHNVcFRDa01HdU8rem10VXJqRTZCck9Ea3BCMGdsSDBicDYwa3V6anlldks2N3VhNW9Wa3p0WDcxVlN3cU15MQ==|62f041eaeaa19de2710f5fca94eceff585eaff0ec7f5bcbc35beae9dcd36f36c; o_act=login; ref_source=undefined; expire_in=15552000; q_c1=17566eaddaef42c3a7ee20c2566bae92|1687088765000|1687088765000; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1687088766; tst=r; z_c0=2|1:0|10:1687088768|4:z_c0|92:Mi4xalp0UERRQUFBQUFBNEpqSmFHbnJGaGNBQUFCZ0FsVk5leng4WlFBZUlwWm50Q216YnhucFk1bERKblA2Y0ZCcXBB|ee5577bfbad2882da9f6ab9619f3cc857d42549465d5994b23cfefe3c50f6946; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1687088768|1687087901'
    # print(page)
    response = requests.get(site, headers = headers)
    print(response.text)
    dom = etree.HTML(response.text)

    picture_urls=dom.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div/div/div[2]/span[1]/div/div/span/figure/img/@data-original')

    print(picture_urls)
    
    for url in picture_urls:
        print(url)
        download_url = url.split('/')[-1].split('?')[0]
        print(download_url)
        download_image(url, download_url)


