from rest_framework import serializers
from .models import ScaleProtocol


class ScaleProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleProtocol
        fields = ['id', 'name']

