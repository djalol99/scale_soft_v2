from django.db import models


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

