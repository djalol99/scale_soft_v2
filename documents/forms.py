from django import forms

from . import models


class VehicleTareForm(forms.ModelForm):
    # date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
    #                      widget=forms.DateTimeInput(
    #                          attrs={
    #                             'class': 'form-control js-date-tare',
    #                             'type': 'datetime-local',
    #                         }, format='%Y-%m-%d %H:%M'), required=False
    #     )

    class Meta:
        model = models.VehicleTare
        fields = ['vehicle', 'scale', 'tare']
        widgets = {
            'vehicle': forms.Select(attrs={
                'class': 'form-select js-vehicle'
            }),
            'scale': forms.Select(attrs={
                'class': 'form-select js-select-scale-weight',
            }),
            'tare': forms.NumberInput(attrs={
                'class': 'form-control js-input-weight',
            }),
        }


class WeighingForm(forms.ModelForm):
    date_gross = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
                                     widget=forms.DateTimeInput(
        attrs={
            'class': 'form-control js-input-date-weight',
            'type': 'datetime-local',
        }, format='%Y-%m-%d %H:%M',), required=False
    )
    date_tare = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
                                    widget=forms.DateTimeInput(
        attrs={
            'class': 'form-control js-input-date-tare',
            'type': 'datetime-local',
        }, format='%Y-%m-%d %H:%M'), required=False
    )

    class Meta:
        model = models.Weighing
        fields = '__all__'
        widgets = {
            'organization': forms.Select(attrs={
                'class': 'form-select'
            }),
            'warehouse': forms.Select(attrs={
                'class': 'form-select'
            }),
            'counterparty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'contract': forms.Select(attrs={
                'class': 'form-select',
            }),
            'driver': forms.Select(attrs={
                'class': 'form-select'
            }),
            'vehicle': forms.Select(attrs={
                'class': 'form-select js-vehicle'
            }),
            'scale_gross': forms.Select(attrs={
                'class': 'form-select'
            }),
            'product': forms.Select(attrs={
                'class': 'form-select js-product'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control js-summa-dependency js-input-price',
                'type': 'number',
                'step': 0.01,
                "min": 0,
            }),
            'vat_rate': forms.Select(attrs={
                'class': 'form-select js-summa-dependency js-select-vat-rate'
            }),
            'includes_vat': forms.TextInput(attrs={
                'class': 'form-check-input js-summa-dependency js-checkbox',
                'type': 'checkbox'
            }),
            'summa': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'vat_summa': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'summa_with_vat': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'gross': forms.TextInput(attrs={
                'class': 'form-control fs-1 bg-primary text-white',
                'type': 'number',
            }),
            'tare': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'net': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'scale_tare': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
