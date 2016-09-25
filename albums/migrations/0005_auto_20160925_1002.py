# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_auto_20160924_0717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['artist_name', 'album_name', 'collection_or_greatest_hits', 'studio_or_live', 'year_released']},
        ),
    ]
