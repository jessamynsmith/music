from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse

from .models import Artist

def artist_list(request):

    artists = Artist.objects.all()

    context = {
        "artists": artists,
    }

    return render (request, "artists/index.html", context)


