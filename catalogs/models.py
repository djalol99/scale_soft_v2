from django.db import models
from datetime import date
from enums.models import VATRate


class VehicleBrand(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    registration_plate = models.CharField(
        max_length=15, blank=False, null=False, unique=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.PROTECT,
                              blank=False, null=False, related_name="brands")

    def __str__(self):
        return f'{self.name} [{self.registration_plate}]'


class Organization(models.Model):
    short_name = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=250, blank=False, null=False)
    tin = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name} (INN: {self.tin})'


class Warehouse(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name


class Counterparty(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    tin = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return f'{self.name} (INN: {self.tin})'


class Contract(models.Model):
    date = models.DateField(default=date.today)
    number = models.IntegerField()
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='contracts')
    counterparty = models.ForeignKey(
        Counterparty, on_delete=models.CASCADE, related_name='contracts')
    comment = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'Shartnoma {self.number} dan {self.date}'


class Driver(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    tin = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name


class UOM(models.Model):
    code = models.CharField(max_length=3, blank=False, null=False)
    short_name = models.CharField(max_length=5, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    uom = models.ForeignKey(UOM, on_delete=models.PROTECT, related_name='uom')
    vat_rate = models.ForeignKey(
        VATRate, on_delete=models.PROTECT, related_name='vatrates')

    def __str__(self):
        return self.name
