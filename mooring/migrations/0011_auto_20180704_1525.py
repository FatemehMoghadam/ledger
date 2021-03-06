# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-04 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0010_rate_mooring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mooringarea',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marineparks', to='mooring.MarinePark'),
        ),
        migrations.AlterModelTable(
            name='mooringareapricehistory',
            table='mooring_mooringarea_pricehistory_v',
        ),
    ]
