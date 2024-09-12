"""
URL configuration for vitaliza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from vitaliza import settings
## Core URLs
from core import urls
## Contact URLs
from contact import urls
## Developer Options URLs
from developer_options import urls
## Treatment URLs
from treatment import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    ## Core URLs
    path("", include("core.urls")),
    ## Contact URLs
    path("get_in_touch/", include("contact.urls")),
    ## Developer Options URLs
    path("developer_options/", include("developer_options.urls")),
    ## Treatment URLs
    path("treatment/", include("treatment.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)