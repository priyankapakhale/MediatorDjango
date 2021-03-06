# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediator_app', '0010_usermedicine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermedicine',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='usermedicine',
            name='user',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='UserMedicine',
        ),
    ]
