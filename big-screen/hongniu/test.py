#数据分析三剑客  numpy    pandas    maltplotib
#数据分析主要是使用的pandas
#你学习numpy就是学习pandas，numpy就是pandas的基础
#pandas本质上就是EXCEL
#Excel本质上就是一个二维表
#pandas最核心的东西   二维表+索引(序号)
#引入pandas
#首先我们要先安装pandas
# pip install numpy
# pip install pandas
import numpy as np
import pandas as pd
#手动的创建一个pandas的dataFrame
dates = pd.date_range('20230601', periods=7)
print(dates)
#1.数据  2.序号 我们可以把任何的东西当作序号   3.表头
#如果我们不给dataframe它序号
#也不给他表头
#它会自动生成表头和序号，默认的序号和表头从0开始的
#df = pd.DataFrame(np.random.randn(7,4))
# df = pd.DataFrame(np.random.randn(7,4),index=[1,2,3,4,5,6,7],columns=list('ABCD'))
# print(df)



#读取我们的csv的文件将这个csv的文件变成一个dataFrame

#读取我们数据表的数据,将数据表转换为dataFrame
import pymysql
conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='zxczxc000',
                                    database='django',
                                    charset='utf8mb4')
movie_df=pd.read_sql('select * from oss_movie',conn)
print(movie_df)




#####################################################################################
#1.筛选 D列的数据大于1
#筛选完数据之后会得到一个新的dataframe
print('###################################################')
#统计有多少部资源

# new_df=df.query('D > 1')
# print(new_df)

#2.排序

#3.统计
#计算所有的资源
sum_count=movie_df.count()
print(sum_count[0])
#计算电影有多少部
movie_count=movie_df.query('type in ["动作片","喜剧片","爱情片","科幻片","恐怖片","战争片","剧情片","战争片","动漫电影"]').count()
print(movie_count[0])
#计算电视剧有多少部
tv_count=movie_df.query('type in ["国产剧","港澳剧","日剧","欧美剧","台湾剧","泰剧","韩剧"]').count()
print(tv_count[0])
#计算综艺有多少部
show_count=movie_df.query('type in ["综艺"]').count()
print(show_count[0])
#计算动漫有多少部
cartoon_count=movie_df.query('type in ["动漫"]').count()
print(cartoon_count[0])

print("------------------------------------------------")
#计算1月份新增的资源数据
month01=movie_df.query('update_time.str.contains("2023-01")', engine='python').count()
print(month01[0])
#计算2月份新增的资源数据
month02=movie_df.query('update_time.str.contains("2023-02")', engine='python').count()
print(month02[0])
#计算3月份新增的资源数据
month03=movie_df.query('update_time.str.contains("2023-03")', engine='python').count()
print(month03[0])
#计算4月份新增的资源数据
month04=movie_df.query('update_time.str.contains("2023-04")', engine='python').count()
print(month04[0])
#计算5月份新增的资源数据
month05=movie_df.query('update_time.str.contains("2023-05")', engine='python').count()
print(month05[0])
#计算6月份新增的资源数据
month06=movie_df.query('update_time.str.contains("2023-06")', engine='python').count()
print(month06[0])

#计算电影下的各种分类的占比
print("------------------------------------------------")
dongzuo_count=movie_df.query('type =="动作片"').count()
print(dongzuo_count[0])
xiju_count=movie_df.query('type =="喜剧片"').count()
print(xiju_count[0])
aiqing_count=movie_df.query('type =="爱情片"').count()
print(aiqing_count[0])
kehuan_count=movie_df.query('type =="科幻片"').count()
print(kehuan_count[0])
kongbu_count=movie_df.query('type =="恐怖片"').count()
print(kongbu_count[0])
zhanzhen_count=movie_df.query('type =="战争片"').count()
print(zhanzhen_count[0])
dongman_count=movie_df.query('type =="动漫电影"').count()
print(dongman_count[0])
print("######################################################")


#根据电影的评分做排名 我们只要前10条数据 TOP10
order_df=movie_df.sort_values(by='score',ascending=False).head(10)
print(order_df)



#加载csv的文件合并两个dataframe 对票房数据做排序
