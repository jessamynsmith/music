from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import Artist
from .forms import ArtistForm


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

    # return HttpResponse("Here are the artists")
    return render (request, "artists/artist_detail.html", context)


def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            messages.success(request, "Artist added!")
            return redirect("artists:artist_detail", id=artist.pk)
    else: 
        form = ArtistForm()

    context = {
        "form":form,
    }

    return render(request, "artists/artist_edit.html", context)


def artist_edit(request, id):
    artist = get_object_or_404(Artist, pk=id)

    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist=form.save()
            messages.success(request, "Artist updated!")
            return redirect("artists:artist_detail", id=artist.pk)

    else:
        form = ArtistForm(instance=artist)

    context = {
        "form": form,
        "artist": artist,
    }

    return render(request, "artists/artist_edit.html", context)























