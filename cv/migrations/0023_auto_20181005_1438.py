# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0022_remove_experience_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='lvl',
            field=models.CharField(blank=True, choices=[('novice', 1), ('advanced-beginer', 2), ('competent', 3), ('professionnel', 4), ('expert', 5)], max_length=100, null=True),
        ),
    ]