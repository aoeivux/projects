#将我们爬取后的数据 存放到pandas中
#做一个小的分析
#分析各个类型的电影的有多少部
#动作片
#喜剧片
#爱情片
#输出到mysql的表中
#dataFrame 和我们excel的二维表是一样的
#安装数据分析模块
#pandas  pip instal pandas
#       pip install fsspec
import pandas as pd
import pymysql


class PandasPipeline:

    def __init__(self):
        #构造我们列头
        self.df=pd.DataFrame(columns=['movieNAME','movieURL','movieTYPE','movieUPDATE'])
        self.index=0
        #链接数据库
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='movie',
                                    password='123456',
                                    database='db_movie',
                                    charset='utf8mb4')
        # 创建一个游标对象
        self.cursor = self.conn.cursor()


    def open_spider(self, spider):
        pass

     #构建我们每一个Series 就是我们的一行数据
    def process_item(self, item, spider):
        self.df.loc[self.index]=[item['movieNAME'],item['movieURL'],item['movieTYPE'],item['movieUPDATE']]
        self.index+=1
        return item


     #保存的路径自己修改一下
    def close_spider(self,spider):
        #统计一下
        #将数据存放到pandas的同时 我们做了一个统计
        dongzuo_df= self.df.query("movieTYPE=='动作片'").count()
        print(dongzuo_df['movieTYPE'])
        print(type(dongzuo_df['movieTYPE']))
        aiqing_df = self.df.query("movieTYPE=='爱情片'").count()
        print(aiqing_df['movieTYPE'])
        print(type(aiqing_df['movieTYPE']))
        sql = 'INSERT INTO tb_calc_count VALUES(null,%s,%s)'
        self.cursor.execute(sql,('动作片的数量',str(dongzuo_df['movieTYPE'])))
        self.cursor.execute(sql,('爱情片的数量',str(aiqing_df['movieTYPE'])))
        self.conn.commit()
        #统计数据并将数据插入到数据表中
        #Pychart  Echart 动态的大屏  JS  AJAX

        self.conn.close()
        self.df.to_excel('f://movie_result.xlsx',index=False)



