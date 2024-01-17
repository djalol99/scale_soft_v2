from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.http import Http404
from django.http.response import HttpResponse, HttpResponseNotFound
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import APIException
from collections import OrderedDict
import json

from exchange.models import Exchange
from .models import (VehicleBrand, Vehicle, Organization, Warehouse,
                     Counterparty, Contract, Driver, UOM, Product)
from .serializers import (VehicleBrandSerializer, VehicleSerializer, OrganizationSerializer,
                          WarehouseSerializer, CounterpartySerializer, ContractSerializer, DriverSerializer,
                          UOMSerializer, ProductSerializer)


class MyModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            key = 'id'
            id = self.request.data[key]
            serializer.save(id=id)
        except IntegrityError as error:
            raise APIException(f"Key (id={id}) already exists.")
        except MultiValueDictKeyError:
            raise APIException(f"Key ({key}) is not provided.")


def get_model_serializer_classes(name):
    clses = {"model": None, "serializer": None}
    if name == "brand":
        clses["model"] = VehicleBrand
        clses["serializer"] = VehicleBrandSerializer
    elif name == "vehicle":
        clses["model"] = Vehicle
        clses["serializer"] = VehicleSerializer
        # continue ...

    return clses


class ExistingObjectListView(APIView):
    def get(self, *args, **kwargs):
        obj = self.kwargs["object"]
        model = get_model_serializer_classes(obj)["model"]

        if model:
            data_qs = model.objects.values_list("id", flat=True)
        else:
            return HttpResponseNotFound(f"object ({obj}) not found.")

        data_json = json.dumps(list(data_qs))
        return HttpResponse(data_json)


class ExchangeList(ListAPIView):
    def get_serializer_class(self):
        self.serializer_class = get_model_serializer_classes(self.kwargs["object"])[
            "serializer"]
        if self.serializer_class:
            return self.serializer_class
        else:
            raise Http404

    def get_queryset(self):
        obj = self.kwargs["object"]
        model = get_model_serializer_classes(obj)["model"]
        if model:
            key = model.__module__ + "." + model.__name__
            self.exchange_data = Exchange.objects.filter(key=key)
            ids = self.exchange_data.values_list("id_object", flat=True)
            return model.objects.filter(id__in=ids)
        else:
            raise Http404

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        for obj in response.data:
            exchange_obj = self.exchange_data.get(id_object=obj["id"])
            obj["key"] = exchange_obj.key
            obj["action"] = exchange_obj.action

        deleted_objets = self.exchange_data.filter(action="deleted")
        for obj in deleted_objets:
            temp_obj = OrderedDict()
            temp_obj['id'] = obj.id_object
            temp_obj['key'] = obj.key
            temp_obj['action'] = obj.action
            response.data.append(temp_obj)

        return response


class VehicleBrandViewSet(MyModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer


class VehicleViewSet(MyModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailAPIView(RetrieveAPIView):
    lookup_field = "registration_plate"
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class OrganizationViewSet(MyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class WarehouseViewSet(MyModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class CounterpartyViewSet(MyModelViewSet):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartySerializer


class ContractViewSet(MyModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class DriverViewSet(MyModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class UOMViewSet(MyModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer


class ProductViewSet(MyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
