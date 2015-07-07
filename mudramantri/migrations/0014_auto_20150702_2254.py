# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0013_auto_20150702_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentprogress',
            name='firstvisitcomp',
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 22, 54, 34, 791000)),
        ),
    ]
