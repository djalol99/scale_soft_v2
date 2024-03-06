from rest_framework import viewsets, permissions
from .models import ScaleProtocol, VATRate
from .serializers import ScaleProtocolSerializer, VATRateSerializer


class ScaleProtocolViewSet(viewsets.ModelViewSet):
    queryset = ScaleProtocol.objects.all()
    serializer_class = ScaleProtocolSerializer
    permission_classes = [permissions.IsAuthenticated]

