# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import datetime
import pandas as pd


class HongniuPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='zxczxc000',
                                    database='django',
                                    charset='utf8mb4')

        # 创建一个游标对象
        self.cursor = self.conn.cursor()

    # 每次开启爬虫的时候
    def open_spider(self, spider):
        # 把数据表的数据清空掉
        sql1 = 'TRUNCATE TABLE oss_movie'
        self.cursor.execute(sql1)
        sql2 = 'TRUNCATE TABLE oss_movie_calc'
        self.cursor.execute(sql2)
        sql3 = 'TRUNCATE TABLE oss_movie_month_grow'
        self.cursor.execute(sql3)
        sql4 = 'TRUNCATE TABLE oss_movie_type_calc'
        self.cursor.execute(sql4)
        sql5 = 'TRUNCATE TABLE oss_movie_score_order'
        self.cursor.execute(sql5)
        sql6 = 'TRUNCATE TABLE oss_movie_booking_office_order'
        self.cursor.execute(sql6)
        sql7 = 'TRUNCATE TABLE oss_movie_popularity_order'
        self.cursor.execute(sql7)
        self.conn.commit()

    # 每次爬取数据如何处理
    def process_item(self, item, spider):
        # 这里的item就是我们刚才yield的数据
        # 开始将数据存储到数据库db_movie的tb_movie整个表
        sql = 'INSERT INTO oss_movie VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (item['mname'], item['paper'], item['score'], item['box_office'], item['other_name'],item['director'],item['actor'],item['type'],item['area'],item['language'],item['show_time'],item['update_time'],item['content'],item['playlist01'],item['playlist02'], item['popularity']))
        self.conn.commit()
        print(item)
        return item

    # 爬虫结束之后的操作
    def close_spider(self, spider):
        # 统计1 每个资源的个数-begin
        self.movie_df = pd.read_sql('select * from oss_movie',self.conn)
        sum_count = self.movie_df .count()
        # 计算电影有多少部
        movie_count = self.movie_df .query(
            'type in ["动作片","喜剧片","爱情片","科幻片","恐怖片","战争片","剧情片","战争片","动漫电影"]').count()
        # 计算电视剧有多少部
        tv_count = self.movie_df.query('type in ["国产剧","港澳剧","日剧","欧美剧","台湾剧","泰剧","韩剧"]').count()
        # 计算综艺有多少部
        show_count = self.movie_df.query('type in ["综艺"]').count()
        # 计算动漫有多少部
        cartoon_count = self.movie_df.query('type in ["动漫"]').count()
        sql = 'INSERT INTO oss_movie_calc VALUES(null,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (str(sum_count[0]),str(movie_count[0]),str(tv_count[0]),str(show_count[0]),str(cartoon_count[0])))

        # 统计1 每个资源的个数-end

        #统计2  获取从1月份开始到现在每个月的数据的增量情况-begin
        #vmware virtualbox
        now=datetime.datetime.now()
        y=now.strftime('%Y')
        print(y)
        m=now.strftime('%m')
        print(m)
        for i in range(1,int(m)+1):
            imonth=self.convertDate(i)
            month = self.movie_df.query(f'update_time.str.contains("{y}-{imonth}")', engine='python').count()
            sql = 'INSERT INTO oss_movie_month_grow VALUES(null,%s,%s)'
            self.cursor.execute(sql, (str(i),str(month[0])))

        # 统计2  获取从1月份开始到现在每个月的数据的增量情况-end


        #统计3  统计电影分类下的各种类型的资源的占比-begin
        typelist=["动作片","喜剧片","爱情片","科幻片","恐怖片","战争片","剧情片","战争片","动漫电影"]
        for type in typelist:
            res_count = self.movie_df.query(f'type =="{type}"').count()
            sql = 'INSERT INTO oss_movie_type_calc VALUES(null,%s,%s)'
            self.cursor.execute(sql, (str(type), str(res_count[0])))
        # 统计3  统计电影分类下的各种类型的资源的占比-end

        # 统计4  统计电影的评分，根据电影的评分，找出前10名展示在前台-begin
        order_df1 = self.movie_df.sort_values(by='score', ascending=False).head(10)
        for index, row in order_df1.iterrows():
            sql = 'INSERT INTO oss_movie_score_order VALUES(null,%s,%s)'
            self.cursor.execute(sql, (str(row['mname']), str(row['score'])))
        # 统计4  统计电影的评分，根据电影的评分，找出前10名展示在前台-end
        self.conn.commit()
        # 统计 结束

        # 统计5 统计电影的票房排名，根据电影的票房，找出前10名展示在前台-begin
        order_df2 = self.movie_df.sort_values(by='box_office', ascending=False).head(10)
        for index, row in order_df2.iterrows():
            sql = 'INSERT INTO oss_movie_booking_office_order VALUES(null,%s,%s)'
            self.cursor.execute(sql, (str(row['mname']), str(row['box_office'])))
        # 统计5 统计电影的票房排名，根据电影的票房，找出前10名展示在前台-end
        self.conn.commit()
        # 统计 结束

        # 统计6 统计电影的人气排名，根据电影的人气，找出前10名展示在前台-begin
        order_df3 = self.movie_df.sort_values(by='popularity', ascending=False).head(10)
        for index, row in order_df3.iterrows():
            sql = 'INSERT INTO oss_movie_popularity_order VALUES(null,%s,%s)'
            self.cursor.execute(sql, (str(row['mname']), str(row['popularity'])))
        # 统计6 统计电影的人气排名，根据电影的人气，找出前10名展示在前台-end
        self.conn.commit()
        # 统计 结束

        self.cursor.close()
        # pass


    def  convertDate(self,num):
        if num>=10:
           return str(num)
        else:
            return f'0{num}'