# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-21 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_condition_obsolete'),
        ('applications', '0021_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Assessment')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Condition')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='conditions',
            field=models.ManyToManyField(through='applications.AssessmentCondition', to='main.Condition'),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentcondition',
            unique_together=set([('condition', 'assessment', 'order')]),
        ),
    ]
