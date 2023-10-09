import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tradeFX.settings')

from base.consumers import TraderConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/traders/", TraderConsumer.as_asgi()),
    ]),
    # "http": get_asgi_application(),
})
