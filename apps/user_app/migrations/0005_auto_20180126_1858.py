# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20180126_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.AddField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(related_name='travelers', to='user_app.Trip'),
        ),
    ]