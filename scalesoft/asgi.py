"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from devices.routing import websocket_urlpatterns
from devices.consumers import TruckScaleWorkerConsumer, IPCameraWorkerConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scalesoft.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )),
    'channel': ChannelNameRouter({
        'truckscale_1': TruckScaleWorkerConsumer.as_asgi(),
        'ipcamera_1': IPCameraWorkerConsumer.as_asgi(),
        'ipcamera_2': IPCameraWorkerConsumer.as_asgi(),
    })
})
