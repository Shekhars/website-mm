# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0006_auto_20150625_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentprogress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.BinaryField(null=True)),
                ('progress', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 5, 20, 15, 941817)),
        ),
    ]
