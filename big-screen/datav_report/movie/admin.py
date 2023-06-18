from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MovieInfo

admin.site.site_header='数据大屏'
admin.site.site_title='数据大屏'
admin.site.index_title='数据大屏'

#注册我们电影信息的模型
#项目   django-admin startproject  项目
#模块   python manage.py startapp movie
#模型(功能)  在我们模块的models.py 添加模型
#在admin.py 全局的系统管理文件  注册我们模型
#对我们列表显示做个性化的配置
class movieInfoAdmin(admin.ModelAdmin):
    list_display = ('mname','director','actor','type','score','area','language')
admin.site.register(MovieInfo,movieInfoAdmin)
