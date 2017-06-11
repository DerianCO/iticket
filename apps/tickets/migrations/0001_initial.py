# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('start_sales_date', models.DateField()),
                ('start_sales_time', models.TimeField()),
                ('end_sales_date', models.DateField()),
                ('end_sales_time', models.TimeField()),
                ('number_tickets_order_min', models.IntegerField()),
                ('number_tickets_order_max', models.IntegerField()),
                ('visibility', models.BooleanField()),
                ('start_visibility_date', models.DateField(blank=True, null=True)),
                ('start_visibility_time', models.TimeField(blank=True, null=True)),
                ('end_visibility_date', models.DateField(blank=True, null=True)),
                ('end_visibility_time', models.TimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventModel')),
            ],
        ),
        migrations.CreateModel(
            name='TypeTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='info_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketModel'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
