from django.contrib import admin

from . models import Albums

class AlbumsAdmin (admin.ModelAdmin):
	search_fields = ('artist_name', 'album_name')

class AlbumsAdmin (admin.ModelAdmin):
    list_display = (
        "artist_name", "album_name", "collection_or_greatest_hits", "studio_or_live",)
    search_fields = ('artist_name', 'album_name')
    

admin.site.register(Albums, AlbumsAdmin)
