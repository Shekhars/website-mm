# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0017_auto_20150704_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 9, 55, 20, 706000)),
        ),
    ]
