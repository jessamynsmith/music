from django.db import models

class Artist (models.Model):
    #artist name
    name = models.CharField(max_length = 40)

