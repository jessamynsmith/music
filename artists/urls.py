from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.artist_list, name="artist_list"),
    url(r'^(?P<id>\d+)/$', views.artist_detail, name="artist_detail")

]