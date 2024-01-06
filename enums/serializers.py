from rest_framework import serializers
from .models import ScaleProtocol, VATRate


class ScaleProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleProtocol
        fields = ['id', 'name']


class VATRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VATRate
        fields = ['id', 'rate']