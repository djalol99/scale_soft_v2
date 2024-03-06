from django.urls import path
from . import views


app_name = 'catalogs'

urlpatterns = [
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brands/update/<int:pk>/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brands/delete/<int:pk>/', views.BrandDeleteView.as_view(), name='brand-delete'),
    path('vehicles/', views.VehicleListView.as_view(), name='vehicles'),
    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/update/<int:pk>/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),
]

