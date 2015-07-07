# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0009_auto_20150627_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentprogress',
            name='completecomp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentprogress',
            name='completeitr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentprogress',
            name='firstvisitcomp',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='currentprogress',
            name='firstvisititr',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='currentprogress',
            name='stepnocomp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currentprogress',
            name='stepnoitr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='currentprogress',
            name='progresscomp',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='currentprogress',
            name='progressitr',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 15, 42, 48, 64000)),
        ),
    ]
