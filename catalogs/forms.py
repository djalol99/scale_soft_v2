from django.forms import ModelForm, TextInput, Select

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

