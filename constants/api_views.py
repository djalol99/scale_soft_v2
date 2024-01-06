from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models  import Constant
from .serializers import ConstantSerializer


class ConstantViewSet(ModelViewSet):
    queryset = Constant.objects.all()
    serializer_class = ConstantSerializer
    permission_classes = [permissions.IsAuthenticated]