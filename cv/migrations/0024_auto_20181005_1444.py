# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0023_auto_20181005_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='lvl',
            field=models.CharField(blank=True, choices=[('novice', '1'), ('advanced-beginer', '2'), ('competent', '3'), ('professionnel', '4'), ('expert', '5')], max_length=100, null=True),
        ),
    ]