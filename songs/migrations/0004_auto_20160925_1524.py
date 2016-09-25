# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_song_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='artists',
        ),
    ]
