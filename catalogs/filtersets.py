import django_filters
from . import models


class BrandFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.VehicleBrand
        fields = {'name': ['exact', 'icontains']}


class VehicleFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Vehicle
        fields = {'name': ['exact', 'icontains'],
                  'registration_plate': ['icontains'],
                  'brand': ['exact']}

