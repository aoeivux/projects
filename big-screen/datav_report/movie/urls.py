

from django.urls import path, include
from rest_framework import routers
from . import views

#将我们movieInfo这个模型相关的api注册到我们视图中
router = routers.DefaultRouter()
router.register(r'movieList', views.MovieInfoViewS
urlpatterns = [
    path('', include(router.urls)),
    #自定义的接口
    path('movie_calc',views.movie_calc),
    path('movie_month_grow',views.movie_month_grow),
    path('movie_type_calc',views.movie_type_calc),
    path('movie_score_order',views.movie_score_order),
    path('movie_booking_office_order',views.movie_booking_office_order),
    path('movie_popularity_order',views.movie_popularity_order)
]