from django.contrib import admin
from django.core.urlresolvers import reverse
from . models import Album

class AlbumAdmin (admin.ModelAdmin):
	search_fields = ('artist_name', 'album_name')

class Meta:
    ordering = ["album_name"]
    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse('album_name:album_details', kwargs={'id':self.pk})
class AlbumAdmin (admin.ModelAdmin):
    list_display = ("artist_name", "album_name", "collection_or_greatest_hits", "studio_or_live",)
    search_fields = ('artist_name', 'album_name')

admin.site.register(Album, AlbumAdmin)
