# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0108_returnuseraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnLogEntry',
            fields=[
                ('communicationslogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wildlifecompliance.CommunicationsLogEntry')),
                ('returns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comms_logs', to='wildlifecompliance.Return')),
            ],
            bases=('wildlifecompliance.communicationslogentry',),
        ),
    ]
