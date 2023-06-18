#下载一个网站的所有的蓝光电影
#蓝光电影数据保存起来 只要带网盘  磁力链接
#1.发起请求
#2.解析我们页面
#3.存储数据   保存到我mysql数据库中
#4.使用pyqt 做一个查询界面  专门用来查找电影的网盘地址
import requests
from lxml import etree

if __name__ == '__main__':
    site='https://www.4khdr.cn/forum.php?mod=forumdisplay&fid=2&filter=typeid&typeid=3&page='
    website='https://www.4khdr.cn/'
    #模拟浏览器携带数据
    #如何将我们爬虫程序伪装为浏览器
    headers={}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    headers['Accept-Encoding'] = 'gzip, deflate, br'
    headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
    headers['Cookie'] = 'hvLw_2132_saltkey=wi2IIP09; hvLw_2132_lastvisit=1686115229; hvLw_2132_visitedfid=2; _clck=1gn55re|2|fc9|0|1253; hvLw_2132_seccodecSAzht=1195.17a95c27ef9fa084b6; hvLw_2132_st_t=0%7C1686125971%7C0b7c48371debd8f176ed6dbed9e41aa6; hvLw_2132_forum_lastvisit=D_2_1686125971; hvLw_2132_lastact=1686126197%09forum.php%09viewthread; hvLw_2132_st_p=0%7C1686126197%7Ccb3dfeef829e469349988296fffcd73c; hvLw_2132_viewid=tid_4538; _clsk=18yg2h3|1686126199672|9|1|u.clarity.ms/collect'
    for pagenum in range(1,21):
        page=f'https://www.4khdr.cn/forum.php?mod=forumdisplay&fid=2&filter=typeid&typeid=3&page={pagenum}'
        print(page)
        response=requests.get(page,headers=headers)
        dom=etree.HTML(response.text)
        # @属性  我们获取的标签的属性   text() 获取标签的正文
        # 我要把整个网站的全部的阿里云盘的资源
        #//table[@class="t_table"][2]/tbody/tr/td//a
        movie_4k_hrefs=dom.xpath('//*[@id="waterfall"]/li/h3/a/@href')
        for movie_4k_href in movie_4k_hrefs:
            link_real_url=website+str(movie_4k_href)
            code=link_real_url.replace('https://www.4khdr.cn/thread-','').replace('-1-1.html','');
            print(code)
            data_context=requests.get(link_real_url,headers=headers)
            #print(data_context.text)
            data_dom=etree.HTML(data_context.text)
            res_title = data_dom.xpath('//table[@class="t_table"]//a/text()');
            res_link=data_dom.xpath('//table[@class="t_table"]//a/@href');
            print(','.join(res_link))
            print(','.join(res_title))





