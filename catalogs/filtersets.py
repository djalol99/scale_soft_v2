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


class OrganizationFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Organization
        fields = {'name': ['exact', 'icontains'],
                  'short_name': ['exact', 'icontains'],
                  'tin': ['exact'],
                  'address': ['exact', 'icontains'],
                  'phone': ['exact', 'contains'],
                  'email': ['exact', 'contains'],
                }                        
        

class WarehouseFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Warehouse
        fields = {'name': ['exact', 'icontains'],
            }  
        

class CounterpartyFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Counterparty
        fields = {'name': ['exact', 'icontains'],
                  'tin': ['exact'],
                  'address': ['exact', 'icontains'],
                  'phone': ['exact', 'contains'],
                }       


class ContractFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Contract
        fields = {'organization': ['exact'],
                  'counterparty': ['exact'],}             


class DriverFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Driver
        fields = {'name': ['exact', 'icontains'],
                  'tin': ['exact'],
                  'address': ['exact', 'icontains'],
                  'phone': ['exact', 'contains'],
                } 


class UOMFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.UOM
        fields = {'code': ['exact'],
                  'short_name': ['exact'],
                  'name': ['exact', 'icontains'],
                } 
        

class ProductFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Product
        fields = {'name': ['exact', 'icontains'],
                  'uom': ['exact'],
                  'vat_rate': ['exact'],
                } 
        
