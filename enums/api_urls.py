from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ScaleProtocolViewSet, VATRateViewSet



router = DefaultRouter()
router.register(r'scaleprotocols', ScaleProtocolViewSet, basename='scaleprotocol')

urlpatterns = [
    path('', include(router.urls))
]