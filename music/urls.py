

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include ("artists.urls", namespace="artists")),
    url(r'^', include('core.urls', namespace="core"))
]






