# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-05 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_auto_20180228_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='scoreboard_freeze_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='scoreboard_freeze_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
