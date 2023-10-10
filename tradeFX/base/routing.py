from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/traders/$', consumers.TraderConsumer.as_asgi()),
]