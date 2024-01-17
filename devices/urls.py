from django.urls import path
from devices import views


app_name = 'devices'

urlpatterns = [
    # truck scale urls
    path('scales/', views.ScaleListView.as_view(), name='scales'),
    path('scales/create/', views.ScaleCreateView.as_view(), name='scale-create'),
    path('scales/update/<int:pk>/',
         views.ScaleUpdateView.as_view(), name='scale-update'),
    path('scales/delete/<int:pk>/',
         views.ScaleDeleteView.as_view(), name='scale-delete'),
    path('scales/<int:pk>/', views.ScaleDetailAPIView.as_view(),
         name='api-scale-detail'),
    # IP camera urls
    path('cameras/', views.IPCameraListView.as_view(), name='cameras'),
    path('cameras/create/', views.IPCameraCreateView.as_view(), name='camera-create'),
    path('cameras/update/<int:pk>/',
         views.IPCameraUpdateView.as_view(), name='camera-update'),
    path('cameras/delete/<int:pk>/',
         views.IPCameraDeleteView.as_view(), name='camera-delete'),
]
