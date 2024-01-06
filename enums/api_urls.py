from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ScaleProtocolViewSet, VATRateViewSet



router = DefaultRouter()
router.register(r'scaleprotocols', ScaleProtocolViewSet, basename='scaleprotocol')
router.register(r'vatrates', VATRateViewSet, basename='vatrate')

urlpatterns = [
    path('', include(router.urls))
]