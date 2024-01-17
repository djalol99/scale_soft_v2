from django.db import models
from enums.models import ScaleProtocol


class Scale(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    port = models.CharField(blank=False, null=False)
    protocol = models.ForeignKey(
        ScaleProtocol, on_delete=models.PROTECT, related_name='protocols')

    def __str__(self):
        return f'{self.name} (port: {self.port})'


class IPCamera(models.Model):
    name = models.CharField(max_length=200, blank=False,
                            null=False)
    ip_address = models.CharField(max_length=15, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    anpr = models.BooleanField(default=False)

    def __str__(self):
        return self.name
