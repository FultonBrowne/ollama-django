from django.urls import re_path

from django_streaming.channel import Channel

websocket_urlpatterns = [
    re_path(r'ws/livec/$', Channel.as_asgi()),
]
