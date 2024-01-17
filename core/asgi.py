import os

from django.core.asgi import get_asgi_application
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import main.consumers


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()

websocket_urlpatterns = [
re_path(r'ws/live_stream/', main.consumers.LiveStreamConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
    URLRouter(
        websocket_urlpatterns
    )
),
})