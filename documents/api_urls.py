from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import WeighingViewSet, VehicleTareViewSet


router = DefaultRouter()
router.register(r'weighing', WeighingViewSet, basename='weighing')
router.register(r'tares', VehicleTareViewSet, basename='tare')

urlpatterns = [
    path('', include(router.urls)),
]