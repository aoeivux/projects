import requests
import lxml
from lxml import etree

if __name__ == '__main__':
    #  需要爬取的网址
    site = 'https://www.doutula.com/photo/list/?page='

    # 爬取前十页
    for i in range(1, 11):
        url = site + str(i)
        # print(url)
        # 伪装成浏览器，因为有一些网站防止程序形式请求网站
        headers = {}
        headers['User-Agent']  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        headers['Accept-Language'] = 'en-US,en;q=0.9'
        headers['Cookie'] = 'Hm_lpvt_2fc12699c699441729d4b335ce117f40=1686120745; Hm_lvt_2fc12699c699441729d4b335ce117f40=1686119936; XSRF-TOKEN=eyJpdiI6ImJuREd4Z2lOeTdOazlsXC9NVzBKa3hRPT0iLCJ2YWx1ZSI6IjVMcDRjV0ZGa1lYWGdyXC9RZmdyQitKVzI4OVRRTU1zdm5uc3F2TmgxRnNReldMdERyajJneVhnZnZuNjBtYVR0IiwibWFjIjoiMjVhZDIyMzhiZGZkZjRhM2YwNDk0OTk3ZTc4ZmJhZmE5Mjk5NTMyYzNmNzUzZGJkNTJkNDk5YjJhMDUyOGQ5YSJ9; doutula_session=eyJpdiI6IjhpRWFvXC9WM0gwMkNodlNyTk5vU1hRPT0iLCJ2YWx1ZSI6IlRpY3F5KzhSYUxQeWxZTXVJdjdPTEZcL1ZHVlRJaUl4ZDVZbHViTTkrRjVUdmtrZ3ppUGVsTlwvd2RSUjZrR01ZaCIsIm1hYyI6IjdkYzIzOWI4MmJjYWRjNGJhMTRhM2E0ZjQ2ZDY1YjdmODNlNWU0MDA1NjM3Yzk5ZTUwMzE2NDI4Mjc2MWNjZDkifQ%3D%3D; _agep=1686119937; _agfp=75e308b281c78ae731f41c5ba56633cd; _agtk=00d97456b04957652f0033c3f36e13d9'
        # 发送请求
        response = requests.get(url, headers=headers)
        # 获取到我们的返回数据
        # print(response.text)
        # 分析数据， 从源代码中拿到需要的数据
        dom = etree.HTML(response.text)
        # 通过xpath定位到我们需要的数据/
        # /img[@data-backup] 表示选择所有具有data-backup属性的img元素，作为上一步选择的a元素的子元素。
        # /@data-backup 表示选择上一步选择的元素的data-backup属性。
        img = dom.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a/img[@data-backup]/@data-backup')
        # 选择img中data-original属性
        img1 = dom.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a/img/@data-original')
        print(img1)

        for img_download_url in img:
            print(img_download_url)
            # 获取图片的二进制数据
            img_data = requests.get(img_download_url, headers=headers).content
            # 图片名称
            img_name = img_download_url.split('/')[-1]
            # 保存图片
            with open('/Users/aoeivux/Downloads/doutulatest/' + img_name, 'wb') as f:
                f.write(img_data)
                print('下载成功')




