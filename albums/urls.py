from django.conf.urls import urls

from . import views

urlpatters =[
    url(r'^$', views.album_list, name="album_list"),
    url(r'^(?P<id>\d+)/$', views.album_details, name="album_details"
]
