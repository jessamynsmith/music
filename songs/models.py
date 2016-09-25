from django.db import models

class Song (models.Model):
    name = models.CharField(max_length=100)
    length = models.DurationField()
    track_number = models.IntegerField()
    artists = models.ManyToManyField("artists.Artist")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_artist_names(self):
        artist_names = [artist.name for artist in self.artists.all()]
        return ", ".join(artist_names)


