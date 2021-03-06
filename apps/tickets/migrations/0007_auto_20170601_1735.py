# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 17:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170531_0256'),
        ('tickets', '0006_auto_20170531_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='MethodsPaymentEventOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_methods/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('message', models.TextField(max_length=250)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventModel')),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 1, 17, 35, 50, 225941)),
        ),
    ]
