from rest_framework.serializers import ModelSerializer
from .models import Constant


class ConstantSerializer(ModelSerializer):
    class Meta:
        model = Constant
        fields = ['id', 'key', 'value']