from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
    collection_or_greatest_hits = models.CharField(max_length=8)
    studio_or_live = models.CharField(max_length=8)
    year_released = models.CharField(max_length=4)
    default='draft'

    class Meta:
         ordering = ['artist_name', 'album_name', 'collection_or_greatest_hits', 'studio_or_live', 'year_released']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("album:album_list", kwargs={self.pk})