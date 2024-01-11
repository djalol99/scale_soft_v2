from django.urls import re_path
from devices import consumers

websocket_urlpatterns = [
    re_path(r'^ws/truckscale/(?P<id>\d+)/$', consumers.TruckScaleConsumer.as_asgi()),
    re_path(r'^ws/ipcamera/(?P<id>\d+)/$', consumers.IPCameraConsumer.as_asgi()),
]
