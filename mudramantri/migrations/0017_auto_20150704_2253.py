# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mudramantri', '0016_auto_20150703_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprogresscomp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstvisit', models.BooleanField(default=True)),
                ('complete', models.BooleanField(default=False)),
                ('step', models.CharField(default=b'0', max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='currentprogress',
            name='user',
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 22, 53, 59, 567000)),
        ),
        migrations.DeleteModel(
            name='currentprogress',
        ),
    ]
