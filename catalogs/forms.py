from django.forms import ModelForm, TextInput, Select, Textarea

from . import models


class BrandForm(ModelForm):
    class Meta:
        model = models.VehicleBrand
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
        }


class VehicleForm(ModelForm):
    class Meta:
        model = models.Vehicle
        fields = ['name', 'registration_plate', 'brand']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'registration_plate': TextInput(attrs={
                'class': "form-control js-plate",
                'placeholder': 'Raqami...'
            }),
            'brand': Select(attrs={
                'class': "form-select",
            }),
        }


class OrganizationForm(ModelForm):
    class Meta:
        model = models.Organization
        fields = ['name', 'short_name', 'tin', 'address', 'phone', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'short_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Qisqacha nomi...'
            }),
            'tin': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'INN'
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Manzili...'
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Telefon raqami...'
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Elektron pochta...'
            }),
        }


class WarehouseForm(ModelForm):
    class Meta:
        model = models.Warehouse
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
        }


class CounterpartyForm(ModelForm):
    class Meta:
        model = models.Counterparty
        fields = ['name', 'tin', 'address', 'phone',]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'tin': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'INN'
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Manzili...'
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Telefon raqami...'
            }),
        }


class ContractForm(ModelForm):
    class Meta:
        model = models.Contract
        fields = ['date', 'number', 'organization', 'counterparty', 'comment']
        widgets = {
            'date': TextInput(attrs={
                'class': "form-control",
                'type': 'date',
                'placeholder': 'Sana...'
            }),
            'number': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Soni...'
            }),
            'organization': Select(attrs={
                'class': "form-select",
            }),
            'counterparty': Select(attrs={
                'class': "form-select",
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
            })
        }


class DriverForm(ModelForm):
    class Meta:
        model = models.Driver
        fields = ['name', 'tin', 'address', 'phone',]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'F.I.SH...'
            }),
            'tin': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'INN'
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Manzili...'
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Telefon raqami...'
            }),
        }


class UOMForm(ModelForm):
    class Meta:
        model = models.UOM
        fields = ['code', 'short_name', 'name',]
        widgets = {
            'code': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Xalqaro kodi...'
            }),
            'short_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Qisqacha nomi...'
            }),
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
        }


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'uom', 'vat_rate',]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'uom': Select(attrs={
                'class': "form-select",
            }),
            'vat_rate': Select(attrs={
                'class': "form-select",
            }),
        }
