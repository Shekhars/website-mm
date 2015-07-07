# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0007_auto_20150627_0520'),
    ]

    operations = [
        migrations.DeleteModel(
            name='currentprogress',
        ),
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 6, 21, 46, 154358)),
        ),
    ]
