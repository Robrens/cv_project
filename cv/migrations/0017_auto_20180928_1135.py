# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0016_auto_20180928_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='address',
        ),
    ]
