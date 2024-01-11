from django.db import models
from django.utils import timezone
from enums.models import VATRate
from catalogs.models import (
    Organization, Warehouse, Contract, Driver, Counterparty, Product, Vehicle)
from devices.models import Scale


class Weighing(models.Model):
    date_gross = models.DateTimeField(default=timezone.localtime, blank=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.PROTECT, blank=True, null=True)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT, blank=True, null=True)
    counterparty = models.ForeignKey(
        Counterparty, on_delete=models.PROTECT, blank=True, null=True)
    contract = models.ForeignKey(
        Contract, on_delete=models.PROTECT, blank=True, null=True)
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    scale_gross = models.ForeignKey(
        Scale, on_delete=models.PROTECT, related_name='grosses', blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, blank=True, null=True)
    price = models.FloatField(default=0, blank=True, null=True)
    includes_vat = models.PositiveSmallIntegerField(default=0)
    summa = models.FloatField(default=0, blank=True, null=True)
    vat_rate = models.ForeignKey(
        VATRate, on_delete=models.PROTECT, blank=True, null=True)
    vat_summa = models.FloatField(default=0, blank=True, null=True)
    summa_with_vat = models.FloatField(default=0, blank=True, null=True)
    gross = models.IntegerField(default=0, blank=True, null=True)  # brutto
    tare = models.SmallIntegerField(default=0, blank=True, null=True)  # tara
    net = models.SmallIntegerField(default=0, blank=True, null=True)  # netto
    scale_tare = models.ForeignKey(
        Scale, on_delete=models.PROTECT, related_name='tares', blank=True, null=True)
    date_tare = models.DateTimeField(blank=True, null=True)
    photo_1 = models.ImageField(upload_to="images/", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.date_gross} {self.vehicle}: netto={self.net}, brutto={self.gross}, tara={self.tare}"


class VehicleTare(models.Model):
    date = models.DateTimeField(default=timezone.localtime, blank=True)
    tare = models.SmallIntegerField(default=0, blank=True, null=True)  # tara
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    scale = models.ForeignKey(
        Scale, on_delete=models.PROTECT, blank=True, null=True)
    photo_1 = models.ImageField(upload_to="images/", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.id}.Tara {self.tare} kg ({self.vehicle})"
