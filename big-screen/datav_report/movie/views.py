from django.shortcuts import render
from requests import Response

# Create your views here.
# views.py 视图层  接收用户的请求

from rest_framework import viewsets
from rest_framework.decorators import api_view

#这里一定要使用相对路径 前面要加.
from .models import MovieInfo
#这里一定使用相对路径 前面要加.
from .serializers import MovieInfoSerializer




from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import MovieInfo
from .models import movieCalc
from .models import movieMonthGrow
from .models import movieTypeCalc
from .models import movieScoreOrder
from .models import movieBookingOfficeOrder
from .models import moviePopularityOrder
from .serializers import MovieInfoSerializer
from .serializers import MovieCalcSerializer
from .serializers import MovieMonthGrowSerializer
from .serializers import MovieTypeCalcSerializer
from .serializers import MovieScoreOrderSerializer
from .serializers import MovieBoxOrderSerializer
from .serializers import MoviePopularityOrderSerializer



class MovieInfoViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def movie_calc(request):
    """
    列出所有的code snippet，或创建一个新的snippet。
    """
    snippets = movieCalc.objects.all()
    serializer = MovieCalcSerializer(snippets, many=True)
    return JSONResponse(serializer.data)

# 月份上传资源数量
def movie_month_grow(request):
    snippets = movieMonthGrow.objects.all()
    serializer = MovieMonthGrowSerializer(snippets, many=True)
    return JSONResponse(serializer.data)

# 电影类型统计
def movie_type_calc(request):
    snippets = movieTypeCalc.objects.all()
    serializer = MovieTypeCalcSerializer(snippets, many=True)
    return JSONResponse(serializer.data)


# 评分人气榜
def movie_score_order(request):
    snippets = movieScoreOrder.objects.all()
    serializer = MovieScoreOrderSerializer(snippets, many=True)
    return JSONResponse(serializer.data)

# 票房排名榜
def movie_booking_office_order(request):
    snippets = movieBookingOfficeOrder.objects.all()
    serializer = MovieBoxOrderSerializer(snippets, many=True)
    return JSONResponse(serializer.data)

# 票房人气榜
def movie_popularity_order(request):
    snippets = moviePopularityOrder.objects.all()
    serializer = MoviePopularityOrderSerializer(snippets, many=True)
    return JSONResponse(serializer.data)
