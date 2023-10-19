from django.urls import re_path

from django_streaming.chatchannel import ChatChannel

websocket_urlpatterns = [
    re_path(r'ws/livec/$', ChatChannel.as_asgi()),
]
