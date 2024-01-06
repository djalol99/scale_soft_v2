from rest_framework.serializers import ModelSerializer
from .models import Weighing, VehicleTare


class WeighingSerializer(ModelSerializer):
    class Meta:
        model = Weighing
        fields = '__all__'


class VehicleTareSerializer(ModelSerializer):
    class Meta:
        model = VehicleTare
        fields = '__all__'