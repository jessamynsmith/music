# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '__first__'),
        ('songs', '0002_song_track_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='artists.Artist'),
        ),
    ]
