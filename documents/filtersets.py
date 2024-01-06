from django_filters import FilterSet

from . import models


class VehicleTareFilterSet(FilterSet):
    class Meta:
        model = models.VehicleTare
        fields = {
            'date': ['gte', 'lte'],
            'vehicle': ['exact'],
        }


class WeighingFilterSet(FilterSet):
    class Meta:
        model = models.Weighing
        fields = {
            'date_gross': ['gte', 'lte'],
            'vehicle': ['exact'],
            'organization': ['exact'],
            'counterparty': ['exact'],
            'product': ['exact'],
            'vehicle': ['exact'],
        }