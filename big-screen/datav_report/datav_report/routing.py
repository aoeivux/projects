# chat/routing.py
from django.urls import re_path

from chat import consumers as chat_consumer
from movie import consumers as movie_consumer

websocket_urlpatterns = [
    re_path(r"ws/chat", chat_consumer.TailfConsumer.as_asgi()),
    re_path(r"ws/movie", movie_consumer.TailfConsumer.as_asgi()),
]