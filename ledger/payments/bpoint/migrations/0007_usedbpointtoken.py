# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpoint', '0006_auto_20160919_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedBpointToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('DVToken', models.CharField(max_length=128)),
            ],
        ),
    ]
