# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0008_delete_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=100)),
                ('med_use', models.CharField(max_length=255)),
                ('med_barcode', models.CharField(max_length=100)),
            ],
        ),
    ]
