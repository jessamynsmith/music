from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
from . models import Album
import django.http import HttpResponse


def album_details(request, id):
    album_details = get_object_or_404(Album, pk=id)
        album_details = Album.objects.all()

    context = {
        "album_details": album_details

    }

    return render(request, "album/album_detail.html", context)

def album_list(request):
    album_list = get_object_or_404(Album, pk=id)
    album = Album.objects.all()

    context = {
        "album_lst":album_list,

    }

    return render(request, "album/album_detail.html", context)
