# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0024_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mediator_app.Volunteer'),
        ),
    ]
