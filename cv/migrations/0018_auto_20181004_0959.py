# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0017_auto_20180928_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_the',
            field=models.DateField(blank=True, null=True, verbose_name='Date de fin'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_the',
            field=models.DateField(blank=True, null=True, verbose_name='Date de debut'),
        ),
    ]
