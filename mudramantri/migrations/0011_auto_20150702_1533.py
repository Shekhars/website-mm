# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0010_auto_20150701_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentprogress',
            name='progresscomp',
        ),
        migrations.RemoveField(
            model_name='currentprogress',
            name='progressitr',
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 15, 33, 18, 371000)),
        ),
    ]
