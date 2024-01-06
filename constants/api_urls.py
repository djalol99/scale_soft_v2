from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ConstantViewSet


router = DefaultRouter()
router.register(r'constants', ConstantViewSet, basename='constant')

urlpatterns = [
    path('', include(router.urls)),
]
