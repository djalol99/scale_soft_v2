from django.urls import path

from . import views


app_name = 'documents'

urlpatterns = [
    path('tares/', views.VehicleTareListView.as_view(), name='vehicle-tares'),
    path('last-vehicle-tare/<int:vehicle>/',
         views.LastVehicleTareView.as_view(), name='vehicle-tare-detail'),
    path('tares/create/', views.VehicleTareCreateView.as_view(),
         name='vehicle-tare-create'),
    path('tares/update/<int:pk>/', views.VehicleTareUpdateView.as_view(),
         name='vehicle-tare-update'),
    path('tares/detail/<int:pk>/', views.VehicleTareDetailView.as_view(),
         name='vehicle-tare-detail'),
    path('tares/delete/<int:pk>/', views.VehicleTareDeleteView.as_view(),
         name='vehicle-tare-delete'),
    path('weighing/', views.WeighingListView.as_view(), name='weighing'),
    path('weighing/create/', views.WeighingCreateView.as_view(),
         name='weighing-create'),
    path('weighing/update/<int:pk>/',
         views.WeighingUpdateView.as_view(), name='weighing-update'),
    path('weighing/detail/<int:pk>/',
         views.WeighingDetailView.as_view(), name='weighing-detail'),
    path('weighing/delete/<int:pk>/',
         views.WeighingDeleteView.as_view(), name='weighing-delete'),
]
