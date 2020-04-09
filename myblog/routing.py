# myblog/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('ws/myblog/(?P<room_name>[^/]+)/', consumers.ChatConsumer),
]