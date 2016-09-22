from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
from . models import Artist, Albums


def album_detail(request, id):
    album_list = get_object_or_404(Album, pk=id)
    
    context = {
        "album_detail": album_detail,
        "album_list": album_list,
        
    }

    return render(request, "/album_detail.html", context)

def album_list = (request, id):
    album_detail = get_object_or_404(Bookcase, pk=id)
    
    
    
    context = {
        "album_detail": album_detail,
        "album_list": album_list,
        
    }

    return render(request, "albums/album_list.html", context)
