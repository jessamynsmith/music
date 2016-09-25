from django.contrib import admin

from . models import Song
from artists.models import Artist


class SongAdmin (admin.ModelAdmin):
    search_fields = [
        "name", 
        "track_number",  
    ]

    list_display = [
        "artist_names",
        "name", 
        "length",
        "track_number",
    ]

    def artist_names(self, obj):
        names = [artist.name for artist in obj.artists.all()]
        return ", ".join(names)

    artist_names.short_description = "Artists"


admin.site.register(Song, SongAdmin)

