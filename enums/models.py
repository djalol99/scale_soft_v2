from django.db import models


class ScaleProtocol(models.Model):
    name = models.CharField(primary_key=True,  max_length=50)

    def __str__(self):
        return f"{self.name}"

