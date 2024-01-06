from rest_framework.generics import RetrieveAPIView

from . import models, serializers

class VatRateDetailView(RetrieveAPIView):
    serializer_class = serializers.VATRateSerializer
    queryset = models.VATRate.objects.all()