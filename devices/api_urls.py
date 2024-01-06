from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices import api_views


router = DefaultRouter()
router.register(r'scales', api_views.ScaleViewSet, basename='scale')


urlpatterns = [
    path("existingobjects/<str:object>/", api_views.ExistingObjectListView.as_view(), name="existing-objects"),
    # path("exchange/<str:object>/", api_views.ExchangeList.as_view(), name="devices-exchange"),
    path('', include(router.urls)),
]