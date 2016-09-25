from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AlbumListView.as_view(), name="album_list"),
    url(r'^(?P<id>\d+)/$', views.AlbumDetailview.as_view(), name="album_details"),
]
