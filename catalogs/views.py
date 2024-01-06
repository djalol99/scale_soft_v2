from django.contrib import messages
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveAPIView
from django_filters.views import FilterView

from . import models, forms, filtersets
from .serializers import ProductSerializer

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


# Organization
class OrganizationListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/organization/organization_list.html'
    model = models.Organization
    filterset_class = filtersets.OrganizationFilterSet


class OrganizationCreateView(MyCustomCreateView):
    template_name = 'catalogs/organization/organization_form.html'
    model = models.Organization
    form_class = forms.OrganizationForm
    success_url = reverse_lazy('catalogs:organizations')


class OrganizationUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/organization/organization_form.html'
    model = models.Organization
    form_class = forms.OrganizationForm
    success_url = reverse_lazy('catalogs:organizations')
    

class OrganizationDeleteView(MyCustomDeleteView):
    model = models.Organization
    success_url = reverse_lazy('catalogs:organizations')


# Warehouse
class WarehouseListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/warehouse/warehouse_list.html'
    model = models.Warehouse
    filterset_class = filtersets.WarehouseFilterSet


class WarehouseCreateView(MyCustomCreateView):
    template_name = 'catalogs/warehouse/warehouse_form.html'
    model = models.Warehouse
    form_class = forms.WarehouseForm
    success_url = reverse_lazy('catalogs:warehouses')


class WarehouseUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/warehouse/warehouse_form.html'
    model = models.Warehouse
    form_class = forms.WarehouseForm
    success_url = reverse_lazy('catalogs:warehouses')
    

class WarehouseDeleteView(MyCustomDeleteView):
    model = models.Warehouse
    success_url = reverse_lazy('catalogs:warehouses')


# Counterparty
class CounterpartyListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/counterparty/counterparty_list.html'
    model = models.Counterparty
    filterset_class = filtersets.CounterpartyFilterSet


class CounterpartyCreateView(MyCustomCreateView):
    template_name = 'catalogs/counterparty/counterparty_form.html'
    model = models.Counterparty
    form_class = forms.CounterpartyForm
    success_url = reverse_lazy('catalogs:counterparties')


class CounterpartyUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/counterparty/counterparty_form.html'
    model = models.Counterparty
    form_class = forms.CounterpartyForm
    success_url = reverse_lazy('catalogs:counterparties')
    

class CounterpartyDeleteView(MyCustomDeleteView):
    model = models.Counterparty
    success_url = reverse_lazy('catalogs:counterparties')


# Contract
class ContractListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/contract/contract_list.html'
    model = models.Contract
    filterset_class = filtersets.ContractFilterSet


class ContractCreateView(MyCustomCreateView):
    template_name = 'catalogs/contract/contract_form.html'
    model = models.Contract
    form_class = forms.ContractForm
    success_url = reverse_lazy('catalogs:contracts')


class ContractUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/contract/contract_form.html'
    model = models.Contract
    form_class = forms.ContractForm
    success_url = reverse_lazy('catalogs:contracts')
    

class ContractDeleteView(MyCustomDeleteView):
    model = models.Contract
    success_url = reverse_lazy('catalogs:contracts')


# Driver
class DriverListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/driver/driver_list.html'
    model = models.Driver
    filterset_class = filtersets.DriverFilterSet


class DriverCreateView(MyCustomCreateView):
    template_name = 'catalogs/driver/driver_form.html'
    model = models.Driver
    form_class = forms.DriverForm
    success_url = reverse_lazy('catalogs:drivers')


class DriverUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/driver/driver_form.html'
    model = models.Driver
    form_class = forms.DriverForm
    success_url = reverse_lazy('catalogs:drivers')
    

class DriverDeleteView(MyCustomDeleteView):
    model = models.Driver
    success_url = reverse_lazy('catalogs:drivers')


# UOM
class UOMListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/uom/uom_list.html'
    model = models.UOM
    filterset_class = filtersets.UOMFilterSet


class UOMCreateView(MyCustomCreateView):
    template_name = 'catalogs/uom/uom_form.html'
    model = models.UOM
    form_class = forms.UOMForm
    success_url = reverse_lazy('catalogs:uom')


class UOMUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/uom/uom_form.html'
    model = models.UOM
    form_class = forms.UOMForm
    success_url = reverse_lazy('catalogs:uom')
    

class UOMDeleteView(MyCustomDeleteView):
    model = models.UOM
    success_url = reverse_lazy('catalogs:uom')


    # Product
class ProductListView(LoginRequiredMixin, FilterView):
    template_name = 'catalogs/product/product_list.html'
    model = models.Product
    filterset_class = filtersets.ProductFilterSet


class ProductCreateView(MyCustomCreateView):
    template_name = 'catalogs/product/product_form.html'
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('catalogs:products')


class ProductUpdateView(MyCustomUpdateView):
    template_name = 'catalogs/product/product_form.html'
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('catalogs:products')
    

class ProductDeleteView(MyCustomDeleteView):
    model = models.Product
    success_url = reverse_lazy('catalogs:products')


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = models.Product.objects.all()

