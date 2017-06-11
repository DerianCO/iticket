# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('status', models.BooleanField(default=False)),
                ('location_name', models.CharField(blank=True, max_length=200, null=True)),
                ('location_address', models.CharField(blank=True, max_length=200, null=True)),
                ('location_address_latitude', models.CharField(blank=True, max_length=30, null=True)),
                ('location_address_longitude', models.CharField(blank=True, max_length=30, null=True)),
                ('location_address_two', models.CharField(blank=True, max_length=200, null=True)),
                ('location_address_two_latitude', models.CharField(blank=True, max_length=30, null=True)),
                ('location_address_two_longitude', models.CharField(blank=True, max_length=30, null=True)),
                ('location_state', models.CharField(blank=True, max_length=150, null=True)),
                ('location_postal_code', models.CharField(blank=True, max_length=12, null=True)),
                ('location_country', models.CharField(blank=True, max_length=150, null=True)),
                ('url_event', models.CharField(blank=True, max_length=180, null=True)),
                ('show_map', models.BooleanField()),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField(max_length=600)),
                ('privacy', models.BooleanField()),
                ('show_tickets_remaining', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EventSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('image', models.ImageField(upload_to='schedule_events/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventModel')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_events/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventModel')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_events/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventModel')),
            ],
        ),
        migrations.CreateModel(
            name='TypeEventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=255)),
                ('icon', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='location_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.TypeLocation'),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.TypeEventModel'),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
