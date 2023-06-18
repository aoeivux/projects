# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyProPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='movie',
                                    password='123456',
                                    database='db_movie',
                                    charset='utf8mb4')
        # 创建一个游标对象
        self.cursor = self.conn.cursor()

    #每次爬取数据如何处理
    def process_item(self, item, spider):
        #这里的item就是我们刚才yield的数据
        #开始将数据存储到数据库db_movie的tb_movie整个表
        sql='INSERT INTO tb_movie VALUE(null,%s,%s,%s,%s)'
        self.cursor.execute(sql,(item['movieNAME'],item['movieURL'],item['movieTYPE'],item['movieUPDATE']))
        self.conn.commit()
        return item

    #爬虫结束之后的操作
    def close_spider(self,spider):
        self.cursor.close()