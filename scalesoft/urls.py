"""scalesoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import HomePageView

urlpatterns = i18n_patterns(
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalogs/', include('catalogs.urls')),
    path('devices/', include('devices.urls')),
    path('enums/', include('enums.urls')),
    path('documents/', include('documents.urls')),
    path('api/catalogs/', include('catalogs.api_urls')),
    path('api/devices/', include('devices.api_urls')),
    path('api/constants/', include('constants.api_urls')),
    path('api/enums/', include('enums.api_urls')),
    path('api/documents/', include('documents.api_urls')),
    # path('api/accounts/', include('accounts.api_urls')), # urls for token based authentication
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Administration"  
admin.site.site_title  =  "Site admin"
admin.site.index_title  =  "Administration"