# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20180921_1415'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Me',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
    ]
