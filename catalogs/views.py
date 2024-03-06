from django.contrib import messages
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

from . import models, forms, filtersets

class MyCustomDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'catalogs/confirm_delete.html'
    error_url = None
    success_message = "Muvaffaqiyatli o'chirildi."
    error_message = "O'chirishni amalga oshirib bo'lmadi, chunki katalogdan foydalanilgan"

    def delete(self, request, *args, **kwargs):
        response = None
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
        except ProtectedError:
            error_message = self.error_message
        except Exception:
            error_message = "O'chirishni amalga oshirib bo'lmadi."

        if response is None:
            messages.error(request, error_message, 'danger')
            if self.error_url is None:
                self.error_url = self.success_url
            response = HttpResponseRedirect(self.error_url)
        return response
    

class MyCustomCreateView(LoginRequiredMixin, CreateView):
    success_message = "Muvaffaqiyatli yaratildi"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form) 


class MyCustomUpdateView(LoginRequiredMixin, UpdateView):
    success_message = "Muvaffaqiyatli yangilandi"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    

# VehicleBrand
class BrandListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/brand/brand_list.html'
    model = models.VehicleBrand
    filterset_class = filtersets.BrandFilterSet
    ordering = ['-id']
    paginate_by = 10
    

class BrandCreateView(MyCustomCreateView):
    template_name = 'catalogs/brand/brand_form.html'
    model = models.VehicleBrand
    form_class = forms.BrandForm
    success_url = reverse_lazy('catalogs:brands')


class BrandUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/brand/brand_form.html'
    model = models.VehicleBrand
    form_class = forms.BrandForm
    success_url = reverse_lazy('catalogs:brands')
    

class BrandDeleteView(MyCustomDeleteView):
    model = models.VehicleBrand
    success_url = reverse_lazy('catalogs:brands')
    
    
# Vehicle
class VehicleListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/vehicle/vehicle_list.html'
    model = models.Vehicle
    filterset_class = filtersets.VehicleFilterSet


class VehicleCreateView(MyCustomCreateView):
    template_name = 'catalogs/vehicle/vehicle_form.html'
    model = models.Vehicle
    form_class = forms.VehicleForm
    success_url = reverse_lazy('catalogs:vehicles')


class VehicleUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/vehicle/vehicle_form.html'
    model = models.Vehicle
    form_class = forms.VehicleForm
    success_url = reverse_lazy('catalogs:vehicles')
    

class VehicleDeleteView(MyCustomDeleteView):
    model = models.Vehicle
    success_url = reverse_lazy('catalogs:vehicles')

