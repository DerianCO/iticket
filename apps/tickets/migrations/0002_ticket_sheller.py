# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-22 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_planner', '0001_initial'),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='sheller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event_planner.ShellerModel'),
        ),
    ]
