# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-09 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0040_auto_20190209_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialsubmission',
            name='is_final',
            field=models.NullBooleanField(),
        ),
    ]
