from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Album
from django.http import HttpResponse


def album_list(request):
    albums = Album.objects.all()

    context = {
        "albums":album_list

    }

    return render(request, "albums/album_list.html", context)


def album_details(request):
    album = get_object_or_404(Album, pk=id)

    context = {
        "album": album

    }

    return render(request, "albums/album_details.html", context)
