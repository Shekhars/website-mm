# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import mudramantri.models


class Migration(migrations.Migration):

    dependencies = [
        ('mudramantri', '0004_auto_20150617_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itrform16',
            name='UploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 9, 29, 46, 202000)),
        ),
        migrations.AlterField(
            model_name='partner',
            name='AddressProof',
            field=models.FileField(upload_to=mudramantri.models.content_filecomp_name),
        ),
        migrations.AlterField(
            model_name='partner',
            name='PanCard',
            field=models.FileField(upload_to=mudramantri.models.content_filecomp_name),
        ),
        migrations.AlterField(
            model_name='partner',
            name='Photo',
            field=models.FileField(upload_to=mudramantri.models.content_filecomp_name),
        ),
    ]
