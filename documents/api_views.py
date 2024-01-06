from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Weighing, VehicleTare
from .serializers import WeighingSerializer, VehicleTareSerializer


class WeighingViewSet(ModelViewSet):
    queryset = Weighing.objects.all()
    serializer_class = WeighingSerializer
    permission_classes = (IsAuthenticated,)


class VehicleTareViewSet(ModelViewSet):
    queryset = VehicleTare.objects.all()
    serializer_class = VehicleTareSerializer
    permission_classes = (IsAuthenticated,)