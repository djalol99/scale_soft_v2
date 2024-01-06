from django.urls import path

from . import views


app_name = 'enums'

urlpatterns = [
    path('vatrates/<int:pk>', views.VatRateDetailView.as_view(), name='vat-rates'),
]