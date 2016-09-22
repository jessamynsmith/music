# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='title',
            new_name='album_name',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='author',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='body',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='created',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='status',
        ),
        migrations.AddField(
            model_name='albums',
            name='artist_name',
            field=models.CharField(max_length=250, default=datetime.date(2014, 8, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='albums',
            name='collection_or_greatest_hits',
            field=models.CharField(max_length=8, default=datetime.date(2014, 8, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='albums',
            name='studio_or_live',
            field=models.CharField(max_length=8, default=datetime.date(2014, 8, 1)),
            preserve_default=False,
        ),
    ]
