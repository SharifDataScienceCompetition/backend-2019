# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-12 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180203_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
