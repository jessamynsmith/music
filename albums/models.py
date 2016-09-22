from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Albums(models.Model):
    album_name = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
    collection_or_greatest_hits = models.CharField(max_length=8)
    studio_or_live = models.CharField(max_length=8)
    #year_released = models.DateField()
    default='draft'

class Meta:
    ordering = ('album_name',)
def __str__(self):
    return self.title
