# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0019_auto_20180125_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediator_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediator_app.Volunteer'),
        ),
    ]
