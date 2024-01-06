import django_filters
from devices import models


class ScaleFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Scale
        fields = {'name': ['exact', 'icontains'],
                  'port': ['exact'],
                  'protocol': ['exact']}


class IPCameraFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.IPCamera
        fields = {'name': ['exact', 'icontains'],
                  'ip_address': ['exact'],
                } 