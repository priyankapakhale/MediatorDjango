# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0025_auto_20180127_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='volunteer',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
