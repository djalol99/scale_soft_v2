from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalogs import api_views


router = DefaultRouter()
router.register(r'brands', api_views.VehicleBrandViewSet, basename='brand')
router.register(r'vehicles', api_views.VehicleViewSet, basename='vehicle')
router.register(r'organizations', api_views.OrganizationViewSet,
                basename='organization')
router.register(r'warehouses', api_views.WarehouseViewSet,
                basename='warehouse')
router.register(r'counterparties', api_views.CounterpartyViewSet,
                basename='counterparty')
router.register(r'contracts', api_views.ContractViewSet, basename='contract')
router.register(r'drivers', api_views.DriverViewSet, basename='driver')
router.register(r'uoms', api_views.UOMViewSet, basename='uom')
router.register(r'products', api_views.ProductViewSet, basename='product')


urlpatterns = [
    path("existingobjects/<str:object>/",
         api_views.ExistingObjectListView.as_view(), name="existing-objects"),
    path("exchange/<str:object>/",
         api_views.ExchangeList.as_view(), name="brands-exchange"),
    path('', include(router.urls)),
    path("vehicles/detail/<str:registration_plate>/",
         api_views.VehicleDetailAPIView.as_view(), name="api-vehicle-detail")
]
