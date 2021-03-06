# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_cashtransaction_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashtransaction',
            name='collection_point',
            field=models.TextField(default='Kensington'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cashtransaction',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cashtransaction',
            name='receipt_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='source',
            field=models.CharField(choices=[('cash', 'cash'), ('cheque', 'cheque'), ('eft', 'eft'), ('money_order', 'money_order')], max_length=11),
        ),
    ]
