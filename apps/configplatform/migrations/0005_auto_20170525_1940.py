# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configplatform', '0004_auto_20170511_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='configplatform',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='configplatform',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
