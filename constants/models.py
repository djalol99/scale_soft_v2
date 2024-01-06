from django.db import models

class Constant(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=250)
