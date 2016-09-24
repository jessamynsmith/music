# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_remove_albums_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=250)),
                ('artist_name', models.CharField(max_length=250)),
                ('collection_or_greatest_hits', models.CharField(max_length=8)),
                ('studio_or_live', models.CharField(max_length=8)),
                ('year_released', models.CharField(max_length=4)),
            ],
            options={
                'ordering': ('album_name', 'artist_name'),
            },
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
    ]
