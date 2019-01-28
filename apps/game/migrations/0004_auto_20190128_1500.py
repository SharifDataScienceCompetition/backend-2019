# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-28 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190126_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('app', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PhaseInstructionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Competition')),
            ],
        ),
        migrations.AddField(
            model_name='instruction',
            name='phase_instruction_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.PhaseInstructionSet'),
        ),
    ]