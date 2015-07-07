# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0002_auto_20150617_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcompany',
            name='NoOfPartners',
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 20, 18, 53, 817000)),
        ),
    ]
