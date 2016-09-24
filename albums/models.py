from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
    collection_or_greatest_hits = models.CharField(max_length=8)
    studio_or_live = models.CharField(max_length=8)
    year_released = models.CharField(max_length=4)
    default='draft'

    class Meta:
         ordering = ('album_name', 'artist_name')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("album:album_details", args=[self.p])
