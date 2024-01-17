from django.forms import ModelForm, TextInput, Select

from devices import models


class ScaleForm(ModelForm):
    class Meta:
        model = models.Scale
        fields = ['name', 'port', 'protocol']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'port': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Porti...'
            }),
            'protocol': Select(attrs={
                'class': "form-select",
            }),
        }


class IPCameraForm(ModelForm):
    class Meta:
        model = models.IPCamera
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomi...'
            }),
            'ip_address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'IPv4...'
            }),
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Login...'
            }),
            'password': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Parol...',
                "type": "password"
            }),
            'anpr': TextInput(attrs={
                'class': "form-check-input js-checkbox",
                "type": "checkbox"
            }),
        }
