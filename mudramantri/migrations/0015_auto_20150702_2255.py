# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0014_auto_20150702_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentprogress',
            name='firstvisitcomp',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 22, 55, 0, 344000)),
        ),
    ]
