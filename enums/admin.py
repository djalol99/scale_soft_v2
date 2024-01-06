from django.contrib import admin

from .models import ScaleProtocol, VATRate


admin.site.register(ScaleProtocol)
admin.site.register(VATRate)
