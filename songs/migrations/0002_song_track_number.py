# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
