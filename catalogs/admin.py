from django.contrib import admin

from catalogs import models


admin.site.register(models.VehicleBrand)
admin.site.register(models.Vehicle)
admin.site.register(models.Organization)
admin.site.register(models.Warehouse)
admin.site.register(models.Counterparty)
admin.site.register(models.Contract)
admin.site.register(models.Driver)
admin.site.register(models.UOM)
admin.site.register(models.Product)
