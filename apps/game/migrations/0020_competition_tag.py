# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-25 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_auto_20180220_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='tag',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
