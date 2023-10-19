"""
ASGI config for django_streaming project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django_streaming import wsurls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_streaming.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            wsurls.websocket_urlpatterns
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})
