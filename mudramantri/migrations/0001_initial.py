# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import mudramantri.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='ItrFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AcNo', models.CharField(max_length=20, blank=True)),
                ('IfscCode', models.CharField(max_length=20, blank=True)),
                ('OtherInfo', models.TextField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ITR File Info',
            },
        ),
        migrations.CreateModel(
            name='ItrFileMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FinYear', models.CharField(max_length=7)),
                ('totalamount', models.CharField(max_length=10, blank=True)),
                ('Pan', models.FileField(upload_to=mudramantri.models.content_file_user, blank=True)),
                ('PanStatus', models.BooleanField(default=False)),
                ('OtherIncome', models.FileField(upload_to=mudramantri.models.content_file_user, blank=True)),
                ('OtherIncomeStatus', models.BooleanField(default=False)),
                ('Deduction', models.FileField(upload_to=mudramantri.models.content_file_user, blank=True)),
                ('DeductionStatus', models.BooleanField(default=False)),
                ('itrfile', models.ForeignKey(to='mudramantri.ItrFile')),
            ],
        ),
        migrations.CreateModel(
            name='ItrForm16',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finyear', models.CharField(max_length=7, blank=True)),
                ('form16', models.FileField(upload_to=mudramantri.models.content_file_name, blank=True)),
                ('password', models.CharField(max_length=50, blank=True)),
                ('UploadedOn', models.DateTimeField(default=datetime.datetime(2015, 8, 5, 10, 27, 12, 256000))),
                ('ItrV', models.FileField(upload_to=mudramantri.models.content_file_name, blank=True)),
                ('ItrvStatus', models.BooleanField(default=False)),
                ('PaymentStatus', models.BooleanField(default=False)),
                ('ItrMeta', models.ForeignKey(to='mudramantri.ItrFileMeta')),
            ],
            options={
                'verbose_name_plural': 'Form 16',
            },
        ),
        migrations.CreateModel(
            name='newcompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NoOfPartners', models.IntegerField(default=2, blank=True)),
                ('AuthCapital', models.CharField(max_length=300)),
                ('State', models.CharField(max_length=120)),
                ('Cost', models.CharField(max_length=100)),
                ('Progress', models.IntegerField(default=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PanCard', models.FileField(upload_to=mudramantri.models.content_filecomp_name)),
                ('PanCardStatus', models.BooleanField(default=False)),
                ('AddressProof', models.FileField(upload_to=mudramantri.models.content_filecomp_name)),
                ('AddressProofStatus', models.BooleanField(default=False)),
                ('Photo', models.FileField(upload_to=mudramantri.models.content_filecomp_name)),
                ('PhotoStatus', models.BooleanField(default=False)),
                ('comp', models.ForeignKey(to='mudramantri.newcompany')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('partpayment', models.BooleanField(default=False)),
                ('partpaymentId', models.CharField(max_length=100, null=True)),
                ('partpaymentdate', models.DateTimeField(blank=True)),
                ('fullpayment', models.BooleanField(default=False)),
                ('fullpaymentstatus', models.CharField(max_length=100, null=True)),
                ('fullpaymentdate', models.DateTimeField(blank=True)),
                ('comp', models.OneToOneField(to='mudramantri.newcompany')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_type', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.datetime(2015, 8, 5, 10, 27, 12, 251000))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
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
    ]
