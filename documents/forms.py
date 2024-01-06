from django.forms import ModelForm, TextInput, Select, NumberInput, DateTimeInput, DateTimeField

from . import models


class VehicleTareForm(ModelForm):
    date = DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
                         widget=DateTimeInput(
                             attrs={
                                'class': 'form-control js-input-date-weight',
                                'type': 'datetime-local',
                            }, format='%Y-%m-%d %H:%M'), required=False
        )

    class Meta:
        model = models.VehicleTare
        fields = '__all__'
        widgets = {
            'vehicle': Select(attrs={
                'class': 'form-select'
            }),
            'scale': Select(attrs={
                'class': 'form-select js-select-scale-weight',
            }),
            'tare': NumberInput(attrs={
                'class': 'form-control js-input-weight',
            }), 
        }


class WeighingForm(ModelForm):
    date_gross = DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
                         widget=DateTimeInput(
                             attrs={
                                'class': 'form-control js-input-date-weight',
                                'type': 'datetime-local',
                            }, format='%Y-%m-%d %H:%M',), required=False
        )
    date_tare = DateTimeField(input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M'],
                         widget=DateTimeInput(
                             attrs={
                                'class': 'form-control js-input-date-tare',
                                'type': 'datetime-local',
                            }, format='%Y-%m-%d %H:%M'), required=False
        )
    
    class Meta:
        model = models.Weighing
        fields = '__all__'
        widgets = {
            'organization': Select(attrs={
                'class': 'form-select'
            }),
            'warehouse': Select(attrs={
                'class': 'form-select'
            }),
            'counterparty': Select(attrs={
                'class': 'form-select'
            }),
            'contract': Select(attrs={
                'class': 'form-select',
            }),
            'driver': Select(attrs={
                'class': 'form-select'
            }),
            'vehicle': Select(attrs={
                'class': 'form-select js-vehicle'
            }),
            'scale_gross': Select(attrs={
                'class': 'form-select'
            }),
            'product': Select(attrs={
                'class': 'form-select js-product'
            }),
            'price': TextInput(attrs={
                'class': 'form-control js-summa-dependency js-input-price',
                'type': 'number',
                'step': 0.01,
                "min": 0,
            }), 
            'vat_rate': Select(attrs={
                'class': 'form-select js-summa-dependency js-select-vat-rate'
            }),
            'includes_vat': TextInput(attrs={
                'class': 'form-check-input js-summa-dependency js-input-includes-vat',
                'type': 'checkbox'
            }), 
            'summa': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'vat_summa': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'summa_with_vat': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'gross': TextInput(attrs={
                'class': 'form-control fs-1 bg-primary text-white',
                'type': 'number',
            }),
            'tare': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'net': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'scale_tare': TextInput(attrs={
                'class': 'form-control',
            }),
        }