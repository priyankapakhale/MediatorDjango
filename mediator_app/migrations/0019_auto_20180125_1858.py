# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0018_medicine_user_usermedicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='med_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermedicine',
            name='user_med_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
