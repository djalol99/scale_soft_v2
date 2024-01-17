from django.db import models


class ScaleProtocol(models.Model):
    name = models.CharField(primary_key=True,  max_length=50)

    def __str__(self):
        return f"{self.name}"


class VATRate(models.Model):
    rate = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.rate}%"
