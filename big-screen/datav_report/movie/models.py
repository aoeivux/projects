from django.db import models
import json
# Create your models here.
class  MovieInfo(models.Model):
    mname=models.CharField(verbose_name='电影名称',max_length=100)
    paper=models.CharField(verbose_name='电影海报',max_length=200)
    score=models.CharField(verbose_name='评分',max_length=50)
    box_office=models.CharField(verbose_name='票房',max_length=50)
    popularity=models.CharField(verbose_name='人气',max_length=50)
    other_name=models.CharField(verbose_name='别名',max_length=100)
    director=models.CharField(verbose_name='导演',max_length=100)
    actor=models.CharField(verbose_name='演员',max_length=300)
    type=models.CharField(verbose_name='类型',max_length=50)
    area=models.CharField(verbose_name='地区',max_length=100)
    language=models.CharField(verbose_name='语言',max_length=100)
    show_time=models.CharField(verbose_name='上映时间',max_length=100)
    update_time=models.CharField(verbose_name='最后更新时间',max_length=100)
    content=models.TextField(verbose_name='简介')
    playlist01=models.TextField(verbose_name='播放列表01')
    playlist02=models.TextField(verbose_name='播放列表02')


    def __str__(self):
        return self.mname

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    class Meta:
        db_table='oss_movie'  #实际在数据库中创建的表名
        verbose_name='电影'
        verbose_name_plural=verbose_name




class movieCalc(models.Model):
     sum_count=models.CharField(verbose_name='资源总数',max_length=100)
     movie_count = models.CharField(verbose_name='电影总数', max_length=100)
     tv_count = models.CharField(verbose_name='电视剧总数', max_length=100)
     show_count = models.CharField(verbose_name='综艺总数', max_length=100)
     cartoon_count = models.CharField(verbose_name='综艺总数', max_length=100)

     def __str__(self):
         return self.sum_count

     class Meta:
         db_table = 'oss_movie_calc'  # 实际在数据库中创建的表名
         verbose_name = '资源统计'
         verbose_name_plural = verbose_name


class movieMonthGrow(models.Model):
    month = models.CharField(verbose_name='月份', max_length=100)
    month_count = models.CharField(verbose_name='上传的资源数', max_length=100)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'oss_movie_month_grow'  # 实际在数据库中创建的表名
        verbose_name = '资源增量统计'
        verbose_name_plural = verbose_name


class movieTypeCalc(models.Model):
    typename = models.CharField(verbose_name='资源类型', max_length=100)
    typename_count = models.CharField(verbose_name='资源数', max_length=100)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'oss_movie_type_calc'  # 实际在数据库中创建的表名
        verbose_name = '电影类型分类统计'
        verbose_name_plural = verbose_name

# 电影评分排名
class movieScoreOrder(models.Model):
    mname = models.CharField(verbose_name='资源名称', max_length=100)
    score = models.CharField(verbose_name='资源评分', max_length=100)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'oss_movie_score_order'  # 实际在数据库中创建的表名
        verbose_name = '电影评分排名统计'
        verbose_name_plural = verbose_name

# 电影票房排名
class movieBookingOfficeOrder(models.Model):
    mname = models.CharField(verbose_name='资源名称', max_length=100)
    box_office = models.CharField(verbose_name='资源票房', max_length=100)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'oss_movie_booking_office_order'  # 实际在数据库中创建的表名
        verbose_name = '电影票房排名统计'
        verbose_name_plural = verbose_name


# 电影人气排名
class moviePopularityOrder(models.Model):
    mname = models.CharField(verbose_name='资源名称', max_length=100)
    popularity = models.CharField(verbose_name='资源人气', max_length=100)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'oss_movie_popularity_order'  # 实际在数据库中创建的表名
        verbose_name = '电影人气排名统计'
        verbose_name_plural = verbose_name