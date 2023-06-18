from requests import Response
from rest_framework.decorators import api_view

from .models import MovieInfo
from .models import movieCalc
from .models import movieMonthGrow
from .models import movieTypeCalc
from .models import movieScoreOrder
from .models import movieBookingOfficeOrder
from .models import moviePopularityOrder

from rest_framework import serializers


# Serializers define the API representation.
class MovieInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieInfo
        # 电影名称，海报，评分，别名，导演，演员，类型，地区，语言，上映时间，最后更新时间，简介，播放列表1，播放列表2
        fields = [
            "mname",
            "paper",
            "score",
            "other_name",
            "director",
            "actor",
            "type",
            "area",
            "language",
            "show_time",
            "update_time",
            "content",
            "playlist01",
            "playlist02",
        ]


class MovieCalcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = movieCalc
        # 资源总数   电影资源数   电视剧资源数  综艺资源数   卡通资源数
        fields = ["sum_count", "movie_count", "tv_count", "show_count", "cartoon_count"]


class MovieMonthGrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = movieMonthGrow
        # 月份  月份上传的资源数量
        fields = ["month", "month_count"]


class MovieTypeCalcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = movieTypeCalc
        # 月份  月份上传的资源数量
        fields = ["typename", "typename_count"]


class MovieScoreOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = movieScoreOrder
        # 资源名称  资源的评分
        fields = ["mname", "score"]


# 电影票房排行
class MovieBoxOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = movieBookingOfficeOrder
        # 资源名称  票房的排名
        fields = ["mname", "box_office"]


# 电影人气排行
class MoviePopularityOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = moviePopularityOrder
        # 资源名称  票房的人气
        fields = ["mname", "popularity"]