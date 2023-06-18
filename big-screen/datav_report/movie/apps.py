from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movie"
    verbose_name = '电影管理'
    verbose_name_plural = verbose_name
