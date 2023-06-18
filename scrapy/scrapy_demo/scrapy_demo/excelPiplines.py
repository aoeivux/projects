from openpyxl.workbook import Workbook


#使用到我们第三方的库 openpyxl
#pip install openpyxl


class ExcelPipeline:

    def __init__(self):
        #创建一个Excel工作簿
        self.wb=Workbook()
        #选择第一个工作表
        self.ws=self.wb.active
        #写入表头
        self.ws.append(['电影名称','电影网址','电影类型','最后更新时间'])


    def open_spider(self, spider):
        #self.wb.remove('f://movie.xls')
        pass


    def process_item(self, item, spider):
        #Excel的表一行数据
        #print(item)
        self.ws.append([item['movieNAME'],item['movieURL'],item['movieTYPE'],item['movieUPDATE']])
        return item



   #保存的路径自己修改一下
    def close_spider(self,spider):
        self.wb.save('f://movie.xls')
