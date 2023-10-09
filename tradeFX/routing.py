from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from base.consumers import TraderConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/traders/", TraderConsumer.as_asgi()),
    ]),
})