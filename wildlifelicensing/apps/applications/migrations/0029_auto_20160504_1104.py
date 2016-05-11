# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0028_auto_20160503_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillogentry',
            name='from_email',
            field=models.CharField(blank=True, max_length=200, verbose_name='From'),
        ),
        migrations.AddField(
            model_name='emaillogentry',
            name='subject',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='emaillogentry',
            name='to_email',
            field=models.CharField(blank=True, max_length=500, verbose_name='To'),
        ),
    ]
