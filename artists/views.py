from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Artist

def artist_list(request):

    artists = Artist.objects.all()

    context = {
        "artists": artists,
    }
    # return HttpResponse("Here be I.")
    return render (request, "artists/index.html", context)




def artist_detail(request, id):
    artist = get_object_or_404(Artist, pk=id)

    context = {
        "artist": artist,
    }

    return render (request, "artists/artist_detail.html, context")


