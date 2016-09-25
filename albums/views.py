from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Album
from django.http import HttpResponse


def album_list(request):
    albums = Album.objects.all()
    
    context = {
        "albums":album_list

    }

    return render(request, "albums.album_list.html", context)

def album_list(request):
    album_list = get_object_or_404(Album, pk=id)
    album_list = Album.objects.all()

    context = {
        "albom'":album_details

    }

    return render(request, "album/album_detail.html", context)
