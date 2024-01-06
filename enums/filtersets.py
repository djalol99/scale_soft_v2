import django_filters

from . import models

class ScaleProtocolFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.ScaleProtocol
        fields = {
            'name': ['exact', 'contains'],
        }