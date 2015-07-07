# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mudramantri', '0015_auto_20150702_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprogressitr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstvisit', models.BooleanField(default=True)),
                ('complete', models.BooleanField(default=False)),
                ('step', models.CharField(default=b'0', max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 9, 30, 14, 987000)),
        ),
    ]
