# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0005_auto_20150618_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('question', models.TextField(blank=True)),
                ('step', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 6, 58, 0, 439357)),
        ),
    ]
