from django.conf.urls import include, url
from django.contrib import admin

#from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^albums/', include('albums.urls', namespace='albums')),
    url(r'^artist/', include('artist.urls', namespace='artist')),
    ]
